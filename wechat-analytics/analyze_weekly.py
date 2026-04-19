from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import median
from typing import Any, Dict, List

from common import (
    connect_db,
    iso_to_date,
    load_article_metadata,
    markdown_escape,
    week_bounds,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="分析一周公众号数据，输出高表现/低表现文章和 topic 聚合结果。")
    parser.add_argument(
        "--week-of",
        default=date.today().isoformat(),
        help="给定任意一天，按其所在周生成统计，格式 YYYY-MM-DD。",
    )
    parser.add_argument(
        "--output",
        default="wechat-analytics/data/exports/latest_weekly_analysis.json",
        help="分析结果 JSON 输出路径。",
    )
    return parser.parse_args()


def article_score(row: Dict[str, Any]) -> float:
    read_uv = int(row["int_page_read_user"] or 0)
    share_user = int(row["share_user"] or 0)
    fav_user = int(row["add_to_fav_user"] or 0)
    ori_user = int(row["ori_page_read_user"] or 0)

    share_rate = (share_user / read_uv) if read_uv else 0.0
    fav_rate = (fav_user / read_uv) if read_uv else 0.0
    ori_rate = (ori_user / read_uv) if read_uv else 0.0

    return (read_uv * 0.5) + (share_rate * 1000 * 0.25) + (fav_rate * 1000 * 0.15) + (ori_rate * 1000 * 0.10)


def compute_baselines(conn, metadata: Dict[str, Any], week_start: str, week_end: str) -> Dict[str, float]:
    rows = conn.execute(
        """
        SELECT stat_date, title, int_page_read_user, share_user, add_to_fav_user, ori_page_read_user
        FROM article_metrics
        WHERE stat_date < ? AND stat_date >= date(?, '-28 day')
        """,
        (week_start, week_start),
    ).fetchall()

    topic_scores = defaultdict(list)
    for row in rows:
        meta = metadata.get(row["title"])
        topic = meta.topic_id if meta else "T07"
        topic_scores[topic].append(
            article_score(dict(row))
        )

    baselines = {}
    for topic, scores in topic_scores.items():
        baselines[topic] = median(scores) if scores else 0.0
    return baselines


def summarize_source_metrics(conn, start_date: str, end_date: str) -> Dict[str, float]:
    rows = conn.execute(
        """
        SELECT source_label, SUM(read_user) AS read_user, SUM(share_user) AS share_user
        FROM article_source_metrics
        WHERE stat_date BETWEEN ? AND ?
        GROUP BY source_label
        """,
        (start_date, end_date),
    ).fetchall()

    source_totals = {row["source_label"]: float(row["read_user"] or 0) for row in rows}
    total = sum(source_totals.values())
    if total <= 0:
        return {}
    return {key: value / total for key, value in source_totals.items()}


def main() -> None:
    args = parse_args()
    any_day = iso_to_date(args.week_of)
    week_start_date, week_end_date = week_bounds(any_day)
    week_start = week_start_date.isoformat()
    week_end = week_end_date.isoformat()

    conn = connect_db()
    metadata = load_article_metadata()
    baselines = compute_baselines(conn, metadata, week_start, week_end)

    rows = conn.execute(
        """
        SELECT stat_date, title, msgid, int_page_read_user, int_page_read_count,
               ori_page_read_user, ori_page_read_count, share_user, share_count,
               add_to_fav_user, add_to_fav_count
        FROM article_metrics
        WHERE stat_date BETWEEN ? AND ?
        ORDER BY stat_date, title
        """,
        (week_start, week_end),
    ).fetchall()

    article_items: List[Dict[str, Any]] = []
    topic_buckets = defaultdict(list)
    for row in rows:
        row_dict = dict(row)
        meta = metadata.get(row_dict["title"])
        topic_id = meta.topic_id if meta else "T07"
        score = article_score(row_dict)
        baseline = baselines.get(topic_id, 0.0)
        if baseline > 0 and score >= baseline * 1.5:
            performance = "异常高"
            reason = f"综合分 {score:.1f}，高于近 4 周 {topic_id} 中位数 {baseline:.1f}"
        elif baseline > 0 and score <= baseline * 0.6:
            performance = "异常低"
            reason = f"综合分 {score:.1f}，低于近 4 周 {topic_id} 中位数 {baseline:.1f}"
        else:
            performance = "正常"
            reason = f"综合分 {score:.1f}"

        item = {
            "date": row_dict["stat_date"],
            "title": row_dict["title"],
            "topic_id": topic_id,
            "score": round(score, 2),
            "performance": performance,
            "reason": reason,
            "keywords": meta.main_keywords if meta else "",
            "collection_type": meta.collection_type if meta else "未记录",
            "read_uv": int(row_dict["int_page_read_user"] or 0),
            "share_user": int(row_dict["share_user"] or 0),
            "fav_user": int(row_dict["add_to_fav_user"] or 0),
        }
        article_items.append(item)
        topic_buckets[topic_id].append(score)

    high_performers = sorted(
        [item for item in article_items if item["performance"] == "异常高"],
        key=lambda x: x["score"],
        reverse=True,
    )
    low_performers = sorted(
        [item for item in article_items if item["performance"] == "异常低"],
        key=lambda x: x["score"],
    )

    topic_summary = []
    for topic_id in [f"T0{i}" for i in range(1, 9)]:
        scores = topic_buckets.get(topic_id, [])
        avg_score = round(sum(scores) / len(scores), 2) if scores else 0.0
        baseline = baselines.get(topic_id, 0.0)
        if not scores:
            conclusion = "本周无数据"
        elif baseline and avg_score >= baseline * 1.2:
            conclusion = "整体强于近 4 周基线"
        elif baseline and avg_score <= baseline * 0.8:
            conclusion = "整体弱于近 4 周基线"
        else:
            conclusion = "与近 4 周基线接近"
        topic_summary.append(
            {
                "topic_id": topic_id,
                "count": len(scores),
                "avg_score": avg_score,
                "baseline": round(baseline, 2),
                "conclusion": conclusion,
            }
        )

    account_rows = conn.execute(
        """
        SELECT stat_date, new_user, cancel_user, net_user, cumulate_user
        FROM account_daily_metrics
        WHERE stat_date BETWEEN ? AND ?
        ORDER BY stat_date
        """,
        (week_start, week_end),
    ).fetchall()

    total_new_user = sum(int(row["new_user"] or 0) for row in account_rows)
    source_summary = summarize_source_metrics(conn, week_start, week_end)

    payload = {
        "week_start": week_start,
        "week_end": week_end,
        "article_count": len(article_items),
        "articles": article_items,
        "high_performers": high_performers[:5],
        "low_performers": low_performers[:5],
        "topic_summary": topic_summary,
        "total_new_user": total_new_user,
        "source_summary": source_summary,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已输出周分析结果：{output_path}")


if __name__ == "__main__":
    main()
