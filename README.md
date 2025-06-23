#  Automated Book Publication Workflow

A Python-based system that automates the process of:
- Scraping book content from online sources
- Taking screenshots of web pages
- Using AI agents to rewrite ("spin") and review content
- Allowing human-in-the-loop editing
- Saving finalized chapters with versioning using ChromaDB

---

##  Features

-  **Web Scraping** using Playwright & BeautifulSoup  
-  **Full-page Screenshot** of source chapter page  
-  **AI Writer Agent** (simulated using Python logic)  
-  **AI Reviewer Agent** (simulated logic with feedback)  
-  **Human-in-the-Loop Interface** via terminal  
-  **ChromaDB Integration** for storing final versions  
-  Structured Python modules for clean architecture

---

##  Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Main language |
| Playwright | Web scraping and screenshot |
| BeautifulSoup | HTML parsing |
| ChromaDB | Versioning and storage |
| pathlib, input() | I/O and CLI interaction |

---

##  Project Structure
automated-book-publisher/
├── agents/
│ ├── writer.py
│ └── reviewer.py
├── scraper/
│ └── scrape_chapter.py
├── storage/
│ └── store_version.py
├── interface/
│ └── human_editor.py
├── data/
│ └── chapter1_original.txt
├── screenshots/
│ └── chapter1.png
├── chroma_storage/
├── app.py
├── requirements.txt
└── README.md



---

## 🚀 How to Run

1. **Install dependencies**:
```bash
pip install -r requirements.txt
python app.py
Follow the CLI prompts:

Preview AI outputs

Choose to edit, approve, or give a summary

Final version is stored using ChromaDB

📸 Output Example
Screenshot saved at: screenshots/chapter1.png

AI rewritten text: chapter1_original.txt

Versioned copy stored in: chroma_storage/

📚 Source Chapter
The Gates of Morning – Book 1, Chapter 1

 Author
K. Yashwanth
 Final Year BCA, AI Engineering Enthusiast
 LinkedIn
 GitHub

📜 License
This submission is made purely for academic and evaluation purposes.
All original book content is sourced from the public domain.
```
Demo Link : https://drive.google.com/file/d/1PDFtB1FIWaoFyf_TmPC1yS99ZN9lp_t9/view?usp=drive_link


