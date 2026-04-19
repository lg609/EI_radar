from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import (
    connect_db,
    datacube_post,
    ensure_directories,
    get_access_token,
    load_config,
    load_source_aliases,
    normalize_article_rows,
    persist_raw_log,
    upsert_account_daily_metrics,
    upsert_article_metrics,
    upsert_source_metrics,
    write_raw_response,
    yesterday_str,
)


ARTICLE_ENDPOINTS = [
    "getarticlesummary",
    "getarticletotal",
    "getuserread",
    "getuserreadhour",
    "getusershare",
    "getusersharehour",
]

ACCOUNT_ENDPOINTS = [
    "getusersummary",
    "getusercumulate",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="抓取微信公众号 datacube 数据并保存到本地。")
    parser.add_argument("--date", default=yesterday_str(), help="统计日期，格式 YYYY-MM-DD，默认昨天。")
    parser.add_argument(
        "--skip-hourly",
        action="store_true",
        help="跳过分时接口，减少调用量。",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="只打印返回结果，不写入数据库。",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_directories()
    config = load_config()
    token = get_access_token(config["appid"], config["appsecret"])
    aliases = load_source_aliases()

    endpoints = ACCOUNT_ENDPOINTS + ARTICLE_ENDPOINTS
    if args.skip_hourly:
        endpoints = [ep for ep in endpoints if not ep.endswith("hour")]

    responses = {}
    for endpoint in endpoints:
        payload = datacube_post(token, endpoint, args.date, args.date)
        responses[endpoint] = payload
        write_raw_response(args.date, endpoint, payload)

    if args.print_only:
        print(json.dumps(responses, ensure_ascii=False, indent=2))
        return

    conn = connect_db()
    for endpoint, payload in responses.items():
        persist_raw_log(conn, endpoint, args.date, args.date, payload)

    upsert_account_daily_metrics(
        conn,
        args.date,
        responses["getusersummary"],
        responses["getusercumulate"],
    )

    article_rows = normalize_article_rows(responses.get("getuserread", {}))
    upsert_article_metrics(conn, article_rows)

    userread_rows = responses.get("getuserread", {}).get("list", [])
    usershare_rows = responses.get("getusershare", {}).get("list", [])
    upsert_source_metrics(conn, args.date, userread_rows, aliases)
    upsert_source_metrics(conn, args.date, usershare_rows, aliases)

    summary_path = Path("wechat-analytics") / "data" / "exports" / f"fetch_summary_{args.date}.json"
    summary_path.write_text(json.dumps({"date": args.date, "endpoints": endpoints}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已抓取 {args.date} 的公众号数据，并写入数据库与原始 JSON。")


if __name__ == "__main__":
    main()
