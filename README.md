# News.ai 🗞️🤖
# Stay tuned more updates coming soon.
**News.ai** is an AI-powered news aggregator that fetches real-time headlines using **NewsAPI**, summarizes articles with **NLP**, saves your reading history in **SQLite**, can read summaries aloud with **gTTS**, and supports a **daily email digest** (SMTP).

> Built with **Python + Streamlit + NewsAPI + SQLite + gTTS + SMTP Email**.

---

## ✨ What Employers Will Like
- Clean separation of concerns (API layer, NLP layer, DB layer, UI layer)
- Real-world integrations (NewsAPI + SMTP)
- Persistent storage (SQLite)
- User-facing product (Streamlit UI)
- Extensible architecture (easy to swap summarizer or add personalization)

---

## 🚀 Features
- **Real-time news fetching** via **NewsAPI**
- **AI/NLP summarization** for quick reading
- **Streamlit UI** for interactive browsing
- **Reading history + saved items** stored in **SQLite**
- **Text-to-Speech (TTS)** with **gTTS**
- **Email digest** (daily headlines via **SMTP**)
- Optional: basic recommendations / personalization module (if enabled)

---

## 🧰 Tech Stack
- **Language:** Python  
- **UI:** Streamlit  
- **News Source:** NewsAPI  
- **Database:** SQLite  
- **Summarization:** NLP summarizer module (upgradeable to transformer models)  
- **Text-to-Speech:** gTTS  
- **Email Digest:** SMTP (Gmail/Outlook compatible with app passwords)

---

## 🧠 System Overview
```mermaid
flowchart LR
  UI[Streamlit UI] --> API[NewsAPI Fetcher]
  API --> NLP[NLP Summarizer]
  NLP --> UI
  UI --> DB[(SQLite History)]
  NLP --> TTS[gTTS Audio]
  NLP --> MAIL[SMTP Email Digest]
