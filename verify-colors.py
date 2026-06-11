#!/usr/bin/env python3
"""
Take a Playwright screenshot of both ticket pages and save to /tmp/ticket-verify.png
Run: python3 verify-colors.py
"""
import subprocess
import sys
import os

def ensure_server():
    result = subprocess.run(["lsof", "-ti:8000"], capture_output=True, text=True)
    if not result.stdout.strip():
        print("Starting server on port 8000...")
        subprocess.Popen(
            ["python3", "-m", "http.server", "8000"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        import time; time.sleep(1)
    else:
        print("Server already running on port 8000")

def screenshot():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        # reduced-motion disables CSS animations/transitions so colors render static
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            reduced_motion="reduce",
        )
        page = context.new_page()
        # index.html — compact view
        page.goto("http://localhost:8000/index.html")
        page.wait_for_timeout(500)
        page.screenshot(path="/tmp/ticket-index.png", animations="disabled")
        print("Saved /tmp/ticket-index.png")
        # ticket-details.html — full view with strip bar
        page.goto("http://localhost:8000/ticket-details.html")
        page.wait_for_timeout(500)
        page.screenshot(path="/tmp/ticket-details.png", full_page=True, animations="disabled")
        print("Saved /tmp/ticket-details.png")
        browser.close()

if __name__ == "__main__":
    ensure_server()
    screenshot()
    print("\nOpen screenshots to verify:")
    print("  open /tmp/ticket-index.png /tmp/ticket-details.png")
