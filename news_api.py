import requests
from dotenv import load_dotenv
from utils import get_secret


load_dotenv()
API_KEY = get_secret("NEWSAPI_KEY")
BASE = "https://newsapi.org/v2"




def fetch_top_headlines(country="us", q=None, category=None, page_size=20):
   """Return a list of normalized article dicts fetched from NewsAPI's top-headlines endpoint.
   Each article has: title, description, content, url, source, publishedAt
   """
   if not API_KEY:
      raise RuntimeError("NEWSAPI_KEY not set. Copy .env.example to .env and add your key.")


   url = f"{BASE}/top-headlines"
   params = {
      "apiKey": API_KEY,
      "country": country,
      "pageSize": page_size,
   }
   if q:
      params["q"] = q
   if category:
      params["category"] = category


   r = requests.get(url, params=params, timeout=20)
   r.raise_for_status()
   data = r.json()
   articles = data.get("articles", [])


   normalized = []
   for a in articles:
      normalized.append({
         "title": a.get("title") or "",
         "description": a.get("description") or "",
         "content": a.get("content") or "",
         "url": a.get("url"),
         "source": (a.get("source") or {}).get("name"),
         "publishedAt": a.get("publishedAt"),
      })
   return normalized