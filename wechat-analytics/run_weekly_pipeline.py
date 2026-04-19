from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from common import REPO_ROOT, yesterday_str


def run_step(args: list[str]) -> None:
    subprocess.run(args, check=True, cwd=str(REPO_ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="执行微信公众号数据抓取与周复盘生成的一键流水线。")
    parser.add_argument("--date", default=yesterday_str(), help="抓取统计日期，默认昨天。")
    parser.add_argument("--week-of", default=yesterday_str(), help="按哪一天所在周输出周复盘。")
    parser.add_argument("--skip-fetch", action="store_true", help="跳过抓取，只做分析和渲染。")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    python_exe = sys.executable
    analytics_dir = Path("wechat-analytics")

    if not args.skip_fetch:
        run_step([python_exe, str(analytics_dir / "fetch_wechat_data.py"), "--date", args.date])

    run_step([python_exe, str(analytics_dir / "analyze_weekly.py"), "--week-of", args.week_of])
    run_step([python_exe, str(analytics_dir / "render_weekly_review.py")])
    print("周复盘自动化流水线执行完成。")


if __name__ == "__main__":
    main()
