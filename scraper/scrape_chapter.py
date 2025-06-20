# scraper/scrape_chapter.py

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from pathlib import Path

def scrape_chapter(url: str, screenshot_path: Path, text_path: Path) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Take screenshot
        page.screenshot(path=screenshot_path, full_page=True)

        # Extract HTML content
        html = page.content()
        browser.close()

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.select_one("div#mw-content-text")

    if not content_div:
        raise ValueError("Content not found on page.")

    chapter_text = content_div.get_text(separator="\n", strip=True)

    # Save extracted text
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(chapter_text)

    return chapter_text
