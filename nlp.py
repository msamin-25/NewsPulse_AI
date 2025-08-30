from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


CATEGORIES = {
   "Technology": ["ai", "software", "tech", "apple", "google", "microsoft", "startup", "chip", "robot", "cyber"],
   "Finance": ["stock", "market", "bitcoin", "crypto", "fed", "inflation", "earnings", "revenue", "bank"],
   "Sports": ["match", "tournament", "goal", "nba", "mlb", "nfl", "soccer", "football", "cricket", "tennis"],
   "Science": ["research", "study", "scientist", "space", "nasa", "climate", "quantum", "biology", "physics"],
   "Health": ["vaccine", "hospital", "covid", "medical", "disease", "health", "drug"],
   "Entertainment": ["movie", "film", "tv", "netflix", "celebrity", "music", "game", "box office"],
   "Politics": ["election", "president", "parliament", "policy", "minister", "senate", "bill", "congress"],
   "Business": ["merger", "acquisition", "startup", "funding", "deal", "company", "industry"],
}


def summarize(text: str, sentences: int = 3) -> str:
   if not text:
      return ""
   try:
      parser = PlaintextParser.from_string(text, Tokenizer("english"))
      summarizer = LsaSummarizer()
      sents = summarizer(parser.document, sentences)
      out = " ".join(str(s) for s in sents)
      return out or (text[:400] + "...")
   except Exception:
      # fallback: return the beginning of the text
      return (text or "")[:400]


def classify(text: str) -> str:
   t = (text or "").lower()
   best, best_score = "General", 0
   for cat, keys in CATEGORIES.items():
      score = sum(1 for k in keys if k in t)
      if score > best_score:
         best, best_score = cat, score
   return best