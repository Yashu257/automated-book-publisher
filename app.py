# app.py

from pathlib import Path
from scraper.scrape_chapter import scrape_chapter
from agents.writer import ai_writer
from agents.reviewer import ai_reviewer
from interface.human_editor import human_review_interface  # ✅ CORRECT
from storage.store_version import store_version

# Configs
CHAPTER_URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
SCREENSHOT_PATH = Path("screenshots/chapter1.png")
TEXT_PATH = Path("data/chapter1_original.txt")
CHAPTER_ID = "GatesOfMorning_Book1_Chapter1"

def run_workflow():
    print(" Step 1: Scraping Chapter...")
    content = scrape_chapter(CHAPTER_URL, SCREENSHOT_PATH, TEXT_PATH)

    print("\n Step 2: AI Writing...")
    rewritten = ai_writer(content)

    print("\n Step 3: AI Reviewing...")
    reviewed = ai_reviewer(rewritten)

    print("\n Step 4: Human-in-the-Loop Editing...")
    final = human_review_interface(content, rewritten, reviewed)  #  use correct function

    print("\n Step 5: Storing Final Version...")
    store_version(doc_id=CHAPTER_ID, final_text=final)

    print("\n Workflow Complete! Screenshot saved, chapter rewritten, reviewed, edited & stored.")

if __name__ == "__main__":
    run_workflow()
