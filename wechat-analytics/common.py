from __future__ import annotations

import json
import sqlite3
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOT = REPO_ROOT / "content"
ANALYTICS_ROOT = REPO_ROOT / "wechat-analytics"
DATA_ROOT = ANALYTICS_ROOT / "data"
RAW_ROOT = DATA_ROOT / "raw"
EXPORT_ROOT = DATA_ROOT / "exports"
DB_PATH = DATA_ROOT / "wechat_analytics.db"
CONFIG_PATH = ANALYTICS_ROOT / "config" / "wechat_config.json"
TOPIC_OVERRIDE_PATH = ANALYTICS_ROOT / "config" / "article_topic_overrides.json"
SOURCE_ALIAS_PATH = ANALYTICS_ROOT / "config" / "source_aliases.json"


TOPIC_RULES = {
    "T01": ["数据", "数据集", "数据工厂", "采集", "无本体", "外骨骼"],
    "T02": ["VLA", "世界模型", "具身大脑", "大模型", "基础模型", "MoE"],
    "T03": ["控制", "小脑", "运动规划", "动作分块", "低延迟"],
    "T04": ["灵巧手", "触觉", "插接", "装配", "手部"],
    "T05": ["仿真", "benchmark", "评测", "评测基准", "Sim-to-Real"],
    "T06": ["芯片", "算力", "平台", "端侧", "推理"],
    "T07": ["公司", "产品", "机器人", "量产", "订单", "交付"],
    "T08": ["融资", "政策", "供应链", "交易", "产业园"],
}


@dataclass
class ArticleMeta:
    publish_date: str
    title: str
    topic_id: str
    main_keywords: str
    collection_type: str


def ensure_directories() -> None:
    CONTENT_ROOT.mkdir(parents=True, exist_ok=True)
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_config() -> Dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"缺少配置文件：{CONFIG_PATH}\n"
            "请先复制 wechat-analytics/config/wechat_config.example.json 为 wechat_config.json 并填入 appid/appsecret。"
        )
    return load_json(CONFIG_PATH, {})


def load_source_aliases() -> Dict[str, str]:
    return load_json(SOURCE_ALIAS_PATH, {})


def yesterday_str() -> str:
    return (date.today() - timedelta(days=1)).isoformat()


def iso_to_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def request_json(url: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if payload is not None else "GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body}") from exc


def explain_wechat_error(payload: Dict[str, Any]) -> str:
    errcode = payload.get("errcode")
    errmsg = payload.get("errmsg", "")
    if errcode == 40164:
        return (
            f"{payload}。\n"
            "当前运行机器的公网 IP 不在公众号开发者 IP 白名单里。\n"
            "请到微信公众平台 -> 开发 -> 基本配置 -> IP 白名单，加入报错中的 IP 后重试。"
        )
    return str(payload)


def get_access_token(appid: str, secret: str) -> str:
    query = urllib.parse.urlencode(
        {"grant_type": "client_credential", "appid": appid, "secret": secret}
    )
    url = f"https://api.weixin.qq.com/cgi-bin/token?{query}"
    payload = request_json(url)
    token = payload.get("access_token")
    if not token:
        raise RuntimeError(f"获取 access_token 失败: {explain_wechat_error(payload)}")
    return token


def datacube_post(access_token: str, endpoint: str, begin_date: str, end_date: str) -> Dict[str, Any]:
    url = f"https://api.weixin.qq.com/datacube/{endpoint}?access_token={access_token}"
    payload = request_json(url, {"begin_date": begin_date, "end_date": end_date})
    if payload.get("errcode", 0) != 0:
        raise RuntimeError(f"{endpoint} 调用失败: {explain_wechat_error(payload)}")
    return payload


def write_raw_response(stat_date: str, endpoint: str, payload: Dict[str, Any]) -> Path:
    target = RAW_ROOT / stat_date / f"{endpoint}.json"
    save_json(target, payload)
    return target


def connect_db() -> sqlite3.Connection:
    ensure_directories()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_api_logs (
            endpoint TEXT NOT NULL,
            begin_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            fetched_at TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            PRIMARY KEY (endpoint, begin_date, end_date, fetched_at)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS account_daily_metrics (
            stat_date TEXT PRIMARY KEY,
            new_user INTEGER DEFAULT 0,
            cancel_user INTEGER DEFAULT 0,
            net_user INTEGER DEFAULT 0,
            cumulate_user INTEGER DEFAULT 0,
            raw_json TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS article_metrics (
            stat_date TEXT NOT NULL,
            msgid TEXT NOT NULL,
            title TEXT NOT NULL,
            int_page_read_user INTEGER DEFAULT 0,
            int_page_read_count INTEGER DEFAULT 0,
            ori_page_read_user INTEGER DEFAULT 0,
            ori_page_read_count INTEGER DEFAULT 0,
            share_user INTEGER DEFAULT 0,
            share_count INTEGER DEFAULT 0,
            add_to_fav_user INTEGER DEFAULT 0,
            add_to_fav_count INTEGER DEFAULT 0,
            raw_json TEXT NOT NULL,
            PRIMARY KEY (stat_date, msgid, title)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS article_source_metrics (
            stat_date TEXT NOT NULL,
            title TEXT NOT NULL,
            msgid TEXT NOT NULL,
            source_type TEXT NOT NULL,
            source_label TEXT NOT NULL,
            read_user INTEGER DEFAULT 0,
            read_count INTEGER DEFAULT 0,
            share_user INTEGER DEFAULT 0,
            share_count INTEGER DEFAULT 0,
            fav_user INTEGER DEFAULT 0,
            fav_count INTEGER DEFAULT 0,
            raw_json TEXT NOT NULL,
            PRIMARY KEY (stat_date, msgid, title, source_type)
        )
        """
    )
    conn.commit()
    return conn


def persist_raw_log(
    conn: sqlite3.Connection,
    endpoint: str,
    begin_date: str,
    end_date: str,
    payload: Dict[str, Any],
) -> None:
    conn.execute(
        """
        INSERT INTO raw_api_logs (endpoint, begin_date, end_date, fetched_at, payload_json)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            endpoint,
            begin_date,
            end_date,
            datetime.now().isoformat(timespec="seconds"),
            json.dumps(payload, ensure_ascii=False),
        ),
    )
    conn.commit()


def upsert_account_daily_metrics(
    conn: sqlite3.Connection,
    stat_date: str,
    user_summary: Dict[str, Any],
    user_cumulate: Dict[str, Any],
) -> None:
    summary_list = user_summary.get("list", [])
    cumulate_list = user_cumulate.get("list", [])
    summary_row = summary_list[0] if summary_list else {}
    cumulate_row = cumulate_list[0] if cumulate_list else {}

    new_user = int(summary_row.get("new_user", 0) or 0)
    cancel_user = int(summary_row.get("cancel_user", 0) or 0)
    cumulate_user = int(cumulate_row.get("cumulate_user", 0) or 0)
    net_user = new_user - cancel_user
    raw_payload = {"getusersummary": user_summary, "getusercumulate": user_cumulate}

    conn.execute(
        """
        INSERT INTO account_daily_metrics (stat_date, new_user, cancel_user, net_user, cumulate_user, raw_json)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(stat_date) DO UPDATE SET
            new_user=excluded.new_user,
            cancel_user=excluded.cancel_user,
            net_user=excluded.net_user,
            cumulate_user=excluded.cumulate_user,
            raw_json=excluded.raw_json
        """,
        (stat_date, new_user, cancel_user, net_user, cumulate_user, json.dumps(raw_payload, ensure_ascii=False)),
    )
    conn.commit()


def normalize_article_rows(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = payload.get("list", [])
    normalized = []
    for row in rows:
        normalized.append(
            {
                "stat_date": row.get("ref_date", ""),
                "msgid": str(row.get("msgid", "")),
                "title": row.get("title", "").strip(),
                "int_page_read_user": int(row.get("int_page_read_user", 0) or 0),
                "int_page_read_count": int(row.get("int_page_read_count", 0) or 0),
                "ori_page_read_user": int(row.get("ori_page_read_user", 0) or 0),
                "ori_page_read_count": int(row.get("ori_page_read_count", 0) or 0),
                "share_user": int(row.get("share_user", 0) or 0),
                "share_count": int(row.get("share_count", 0) or 0),
                "add_to_fav_user": int(row.get("add_to_fav_user", 0) or 0),
                "add_to_fav_count": int(row.get("add_to_fav_count", 0) or 0),
                "raw_json": json.dumps(row, ensure_ascii=False),
            }
        )
    return normalized


def upsert_article_metrics(conn: sqlite3.Connection, rows: Iterable[Dict[str, Any]]) -> None:
    for row in rows:
        conn.execute(
            """
            INSERT INTO article_metrics (
                stat_date, msgid, title, int_page_read_user, int_page_read_count,
                ori_page_read_user, ori_page_read_count, share_user, share_count,
                add_to_fav_user, add_to_fav_count, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(stat_date, msgid, title) DO UPDATE SET
                int_page_read_user=excluded.int_page_read_user,
                int_page_read_count=excluded.int_page_read_count,
                ori_page_read_user=excluded.ori_page_read_user,
                ori_page_read_count=excluded.ori_page_read_count,
                share_user=excluded.share_user,
                share_count=excluded.share_count,
                add_to_fav_user=excluded.add_to_fav_user,
                add_to_fav_count=excluded.add_to_fav_count,
                raw_json=excluded.raw_json
            """,
            (
                row["stat_date"],
                row["msgid"],
                row["title"],
                row["int_page_read_user"],
                row["int_page_read_count"],
                row["ori_page_read_user"],
                row["ori_page_read_count"],
                row["share_user"],
                row["share_count"],
                row["add_to_fav_user"],
                row["add_to_fav_count"],
                row["raw_json"],
            ),
        )
    conn.commit()


def upsert_source_metrics(
    conn: sqlite3.Connection,
    stat_date: str,
    rows: Iterable[Dict[str, Any]],
    aliases: Dict[str, str],
) -> None:
    for row in rows:
        source_key = str(row.get("user_source", row.get("share_source", "all")))
        source_label = aliases.get(source_key, source_key)
        conn.execute(
            """
            INSERT INTO article_source_metrics (
                stat_date, title, msgid, source_type, source_label,
                read_user, read_count, share_user, share_count, fav_user, fav_count, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(stat_date, msgid, title, source_type) DO UPDATE SET
                source_label=excluded.source_label,
                read_user=excluded.read_user,
                read_count=excluded.read_count,
                share_user=excluded.share_user,
                share_count=excluded.share_count,
                fav_user=excluded.fav_user,
                fav_count=excluded.fav_count,
                raw_json=excluded.raw_json
            """,
            (
                stat_date,
                row.get("title", "").strip(),
                str(row.get("msgid", "")),
                source_key,
                source_label,
                int(row.get("int_page_read_user", 0) or 0),
                int(row.get("int_page_read_count", 0) or 0),
                int(row.get("share_user", 0) or 0),
                int(row.get("share_count", 0) or 0),
                int(row.get("add_to_fav_user", 0) or 0),
                int(row.get("add_to_fav_count", 0) or 0),
                json.dumps(row, ensure_ascii=False),
            ),
        )
    conn.commit()


def load_topic_overrides() -> Dict[str, Any]:
    return load_json(TOPIC_OVERRIDE_PATH, {})


def extract_collection_type(body: str) -> str:
    marker = "**模块类型：**"
    if marker not in body:
        return ""
    remainder = body.split(marker, 1)[1].strip()
    return remainder.splitlines()[0].strip()


def infer_topic(title: str, body: str) -> str:
    haystack = f"{title}\n{body}"
    for topic_id, keywords in TOPIC_RULES.items():
        if any(keyword.lower() in haystack.lower() for keyword in keywords):
            return topic_id
    return "T07"


def extract_keywords(body: str) -> str:
    lines = body.splitlines()
    keyword_lines: List[str] = []
    in_keywords = False
    for line in lines:
        if line.strip() == "## 关键词索引":
            in_keywords = True
            continue
        if in_keywords and line.startswith("## "):
            break
        if in_keywords and line.strip():
            keyword_lines.append(line.strip())
    return " | ".join(keyword_lines)


def load_article_metadata() -> Dict[str, ArticleMeta]:
    overrides = load_topic_overrides()
    metadata: Dict[str, ArticleMeta] = {}

    for path in sorted(CONTENT_ROOT.glob("Robot_Intel_*.md")):
        body = path.read_text(encoding="utf-8")
        lines = body.splitlines()
        title = ""
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                break
        if not title:
            continue

        publish_date = path.stem.replace("Robot_Intel_", "")
        override = overrides.get(publish_date, {})
        topic_id = override.get("topic_id") or infer_topic(title, body)
        main_keywords = override.get("main_keywords") or extract_keywords(body)
        collection_type = override.get("collection_type") or extract_collection_type(body) or "未记录"
        metadata[title] = ArticleMeta(
            publish_date=publish_date,
            title=title,
            topic_id=topic_id,
            main_keywords=main_keywords,
            collection_type=collection_type,
        )

    return metadata


def week_bounds(any_day: date) -> tuple[date, date]:
    start = any_day - timedelta(days=any_day.weekday())
    end = start + timedelta(days=6)
    return start, end


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()
