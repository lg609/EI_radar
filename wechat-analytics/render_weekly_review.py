from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

from common import REPO_ROOT, markdown_escape


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="根据周分析 JSON 生成周复盘 Markdown。")
    parser.add_argument(
        "--analysis",
        default="wechat-analytics/data/exports/latest_weekly_analysis.json",
        help="analyze_weekly.py 输出的 JSON 路径。",
    )
    parser.add_argument(
        "--output",
        default="",
        help="输出 Markdown 路径。默认写入 reviews/weekly-review-YYYY-WW.md",
    )
    return parser.parse_args()


def top_source_ratio(source_summary: Dict[str, float], preferred_labels: List[str]) -> str:
    for label in preferred_labels:
        if label in source_summary:
            return f"{source_summary[label] * 100:.1f}%"
    return "待补充（可在 source_aliases.json 中映射来源代码）"


def render_table_rows(items: List[Dict[str, Any]], low: bool = False) -> List[str]:
    rows = []
    if not items:
        reason_col = "问题判断" if low else "原因判断"
        rows.append(f"| - | - | - | 无异常样本 | 本周暂无可自动识别的{'低表现' if low else '高表现'}文章 |")
        return rows

    for item in items:
        performance = item["performance"]
        reason = markdown_escape(item["reason"])
        title = markdown_escape(item["title"])
        rows.append(f"| {item['date']} | {title} | {item['topic_id']} | {performance} | {reason} |")
    return rows


def main() -> None:
    args = parse_args()
    analysis_path = Path(args.analysis)
    if not analysis_path.exists():
        raise FileNotFoundError(f"找不到分析结果：{analysis_path}，请先运行 analyze_weekly.py")

    payload = json.loads(analysis_path.read_text(encoding="utf-8"))
    week_start = date.fromisoformat(payload["week_start"])
    iso_year, iso_week, _ = week_start.isocalendar()
    default_output = REPO_ROOT / "reviews" / f"weekly-review-{iso_year}-{iso_week:02d}.md"
    output_path = Path(args.output) if args.output else default_output

    articles = payload.get("articles", [])
    read_uvs = [item["read_uv"] for item in articles]
    avg_read = round(sum(read_uvs) / len(read_uvs), 1) if read_uvs else 0
    max_read = max(read_uvs) if read_uvs else 0
    min_read = min(read_uvs) if read_uvs else 0
    share_total = sum(int(item["share_user"]) for item in articles)
    fav_total = sum(int(item["fav_user"]) for item in articles)

    source_summary = payload.get("source_summary", {})
    recommend_ratio = top_source_ratio(source_summary, ["recommend", "推荐", "订阅号推荐"])
    search_ratio = top_source_ratio(source_summary, ["search", "搜一搜", "微信搜一搜"])

    lines = [
        f"# 周复盘 {payload['week_start']} ~ {payload['week_end']}",
        "",
        "> 由 `wechat-analytics` 自动生成，可在此基础上继续补充人工判断。",
        "",
        "## 本周基本数据",
        "",
        "| 指标 | 数值 | 备注 |",
        "|------|------|------|",
        f"| 发文数 | {payload['article_count']} | 数据来自 `article_metrics` |",
        f"| 平均阅读 | {avg_read} | 按图文阅读人数计算 |",
        f"| 最高阅读 | {max_read} | 按图文阅读人数计算 |",
        f"| 最低阅读 | {min_read} | 按图文阅读人数计算 |",
        f"| 推荐流量占比 | {recommend_ratio} | 依赖 `source_aliases.json` 映射 |",
        f"| 搜索流量占比 | {search_ratio} | 依赖 `source_aliases.json` 映射 |",
        f"| 分享次数 | {share_total} | 当前使用分享用户数汇总 |",
        f"| 收藏 / 在看 / 留言 | 收藏 {fav_total} / 在看待补 / 留言待补 | 官方 datacube 不直接提供完整在看与留言 |",
        f"| 新增关注 | {payload['total_new_user']} | 来自 `getusersummary` |",
        "",
        "## 本周 3 条主线",
        "",
        "1. 待补：结合本周主条和持续追踪，补充最重要的一条行业主线。",
        "2. 待补：从高表现文章中挑选最值得持续追踪的 topic。",
        "3. 待补：从低表现文章中总结一个需要减少的表达模式。",
        "",
        "## 高表现文章",
        "",
        "| 日期 | 标题 | 主条 topic | 表现 | 原因判断 |",
        "|------|------|------------|------|----------|",
    ]
    lines.extend(render_table_rows(payload.get("high_performers", []), low=False))

    lines.extend(
        [
            "",
            "## 低表现文章",
            "",
            "| 日期 | 标题 | 主条 topic | 表现 | 问题判断 |",
            "|------|------|------------|------|----------|",
        ]
    )
    lines.extend(render_table_rows(payload.get("low_performers", []), low=True))

    lines.extend(
        [
            "",
            "## Topic 表现统计",
            "",
            "| Topic 编号 | 次数 | 平均表现 | 结论 |",
            "|------------|------|----------|------|",
        ]
    )
    for item in payload.get("topic_summary", []):
        lines.append(
            f"| {item['topic_id']} | {item['count']} | {item['avg_score']} | {markdown_escape(item['conclusion'])} |"
        )

    source_brief = ", ".join(
        f"{label}: {ratio * 100:.1f}%"
        for label, ratio in sorted(source_summary.items(), key=lambda x: x[1], reverse=True)[:5]
    ) or "待补充"

    lines.extend(
        [
            "",
            "## 标题与封面回看",
            "",
            "- 本周最有效的标题模式：待补，可优先查看高表现文章是否集中在“公司名 + 动作 + 数字”或“技术路线 + 行业影响”。",
            "- 本周最弱的标题模式：待补，可优先查看低表现文章是否存在亮点不聚焦、关键词不明确的问题。",
            "- 封面是否突出单一主信号：待补，可人工结合后台点击率判断。",
            "",
            "## 搜索与分享表现",
            "",
            f"- 本周已识别的来源分布：{source_brief}",
            "- 哪些关键词带来搜索：待补，若后台有搜一搜关键词面板，可人工补录。",
            "- 哪类文章更容易被转发：优先查看高表现文章中的分享率更高者。",
            "- 哪些内容适合抽成月度合集：优先选择高表现且收藏模块清晰的文章。",
            "",
            "## 收藏模块表现",
            "",
            "| 日期 | 收藏模块类型 | 是否被搜索/转发/收藏 | 结论 |",
            "|------|--------------|----------------------|------|",
        ]
    )
    if articles:
        for item in sorted(articles, key=lambda x: x["date"]):
            status = f"收藏 {item['fav_user']} / 分享 {item['share_user']}"
            lines.append(
                f"| {item['date']} | {markdown_escape(item.get('collection_type', '未记录'))} | {status} | 待人工补充搜索表现 |"
            )
    else:
        lines.append("| - | - | - | 本周暂无文章数据 |")

    lines.extend(
        [
            "",
            "## 下周动作",
            "",
            "- 保留：继续跟踪本周异常高的 topic 和标题模式。",
            "- 增强：给高分享主题补更强的收藏模块和系列化追踪。",
            "- 减少：避免重复写入本周异常低且无增量的表达方式。",
            "- 新增实验：补全 `source_aliases.json` 后复跑脚本，得到更清晰的推荐/搜索占比。",
            "",
        ]
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"已生成周复盘：{output_path}")


if __name__ == "__main__":
    main()
