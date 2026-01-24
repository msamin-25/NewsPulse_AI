# app.py — Streamlit UI for AI News Summarizer

import streamlit as st
from news_api import fetch_news
from nlp import summarize_text
from db import log_article, get_history # ...existing code...
import streamlit as st
from news_api import fetch_news
from nlp import summarize_text
from db import log_article, get_history

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.title("📰 AI-Powered News Summarizer")
st.write("Get personalized, summarized news articles instantly.")

category = st.sidebar.selectbox("Choose a category", 
    ["technology", "business", "sports", "health", "science", "entertainment"])

st.sidebar.markdown("### Your History")
history = get_history() or []
for h in history:
    # support tuples/lists and single strings
    title = h[0] if isinstance(h, (list, tuple)) and len(h) > 0 else str(h)
    meta = h[1] if isinstance(h, (list, tuple)) and len(h) > 1 else ""
    st.sidebar.write(f"- {title} {f'({meta})' if meta else ''}")

if st.button("Fetch News"):
    articles = fetch_news(category=category)
    if not articles:
        st.error("No articles found. Check your API key or try again later.")
    else:
        for article in articles:
            title = article.get("title", "Untitled")
            source = (article.get("source") or {}).get("name", "Unknown")
            description = article.get("description") or article.get("content") or ""
            summary = summarize_text(description)
            st.subheader(title)
            st.caption(source)
            st.write("**Summary:**", summary)
            url = article.get("url")
            if url:
                st.markdown(f"[Read Full Article]({url})")
            log_article(title, category)

## Some duplicate code here to fix

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.title("📰 AI-Powered News Summarizer")
st.write("Get personalized, summarized news articles instantly.")

category = st.sidebar.selectbox("Choose a category", 
    ["technology", "business", "sports", "health", "science", "entertainment"])

st.sidebar.markdown("### Your History")
history = get_history() or []
for h in history:
    # support tuples/lists and single strings
    title = h[0] if isinstance(h, (list, tuple)) and len(h) > 0 else str(h)
    meta = h[1] if isinstance(h, (list, tuple)) and len(h) > 1 else ""
    st.sidebar.write(f"- {title} {f'({meta})' if meta else ''}")

if st.button("Fetch News"):
    articles = fetch_news(category=category)
    if not articles:
        st.error("No articles found. Check your API key or try again later.")
    else:
        for article in articles:
            title = article.get("title", "Untitled")
            source = (article.get("source") or {}).get("name", "Unknown")
            description = article.get("description") or article.get("content") or ""
            summary = summarize_text(description)
            st.subheader(title)
            st.caption(source)
            st.write("**Summary:**", summary)
            url = article.get("url")
            if url:
                st.markdown(f"[Read Full Article]({url})")
            log_article(title, category)
# ...existing

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.title("📰 AI-Powered News Summarizer")
st.write("Get personalized, summarized news articles instantly.")

category = st.sidebar.selectbox("Choose a category", 
    ["technology", "business", "sports", "health", "science", "entertainment"])

st.sidebar.markdown("### Your History") 
history = get_history()
for h in history:
    st.sidebar.write(f"- {h[0]} ({h[1]})")

if st.button("Fetch News"):
    articles = fetch_news(category=category)
    if not articles:
        st.error("No articles found. Check your API key or try again later.")
    else:
        for article in articles:
            st.subheader(article["title"])
            st.caption(article["source"]["name"])
            st.write("**Summary:**", summarize_text(article.get("description", "")))
            st.markdown(f"[Read Full Article]({article['url']})")
            log_article(article["title"], category)

            
