"""Open local DOOCS Markdown editor and paste a generated Markdown file into it.

Usage:
    python D:\RobotGPT\robot-intel-collector\script\open_doocs_editor.py D:\RobotGPT\content\Robot_Intel_YYYY-MM-DD.md

What it does:
1. Ensures the local DOOCS dev server is running at http://localhost:5173/md/
2. Opens the editor in a browser via Playwright
3. Pastes the Markdown file into the left editor pane
4. Leaves the browser open for preview / copy-to-WeChat operation
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

DOOCS_DIR = Path(r"D:\RobotGPT\HTML\doocs-md-local")
DOOCS_URL = "http://localhost:5173/md/"


def is_url_ready(url: str, timeout: float = 2.0) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return 200 <= resp.status < 500
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def start_doocs_server() -> subprocess.Popen | None:
    """Start DOOCS dev server if it is not already running."""
    if is_url_ready(DOOCS_URL):
        print(f"DOOCS editor is already running: {DOOCS_URL}")
        return None

    if not DOOCS_DIR.exists():
        raise FileNotFoundError(f"DOOCS directory not found: {DOOCS_DIR}")

    print(f"Starting local DOOCS editor in: {DOOCS_DIR}")
    env = os.environ.copy()
    env["CI"] = "true"  # Prevent pnpm from blocking on no-TTY prompts
    proc = subprocess.Popen(
        ["cmd", "/c", "pnpm web dev -- --host 127.0.0.1 --port 5173 --strictPort"],
        cwd=str(DOOCS_DIR),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
    )

    deadline = time.time() + 120  # longer timeout for cold-start install
    while time.time() < deadline:
        if is_url_ready(DOOCS_URL):
            print(f"DOOCS editor started: {DOOCS_URL}")
            return proc
        if proc.poll() is not None:
            print("pnpN/web dev exited early (likely need pnpm install) — retrying once...")
            proc = subprocess.Popen(
                ["cmd", "/c", "pnpm web dev -- --host 127.0.0.1 --port 5173 --strictPort"],
                cwd=str(DOOCS_DIR),
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
            )
        time.sleep(1)

    raise TimeoutError(f"Timed out waiting for DOOCS editor: {DOOCS_URL}")


def open_and_paste_markdown(md_path: Path, keep_open_seconds: int | None = None) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Playwright is required. Install with: pip install playwright && playwright install chromium") from exc

    md_text = md_path.read_text(encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
        page = context.new_page()
        page.goto(DOOCS_URL, wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_selector(".cm-content, textarea", timeout=60_000)

        page.evaluate("async text => await navigator.clipboard.writeText(text)", md_text)

        if page.locator(".cm-content").count() > 0:
            page.locator(".cm-content").first.click()
        else:
            page.locator("textarea").first.click()

        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        page.keyboard.press("Control+V")

        time.sleep(2)
        print("Markdown has been pasted into the local DOOCS editor.")
        print(f"Preview URL: {DOOCS_URL}")
        print("Please confirm the right-side WeChat preview, then click the DOOCS copy button and paste into WeChat.")

        if keep_open_seconds is None:
            keep_open_seconds = 24 * 60 * 60
        time.sleep(keep_open_seconds)
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Open local DOOCS editor and paste Markdown into it.")
    parser.add_argument("md_file", help="Path to generated Robot_Intel_YYYY-MM-DD.md")
    parser.add_argument("--keep-open-seconds", type=int, default=None, help="How long to keep browser open. Default: 24 hours.")
    args = parser.parse_args()

    md_path = Path(args.md_file)
    if not md_path.exists():
        print(f"Markdown file not found: {md_path}", file=sys.stderr)
        return 1

    start_doocs_server()
    open_and_paste_markdown(md_path, args.keep_open_seconds)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
