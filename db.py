# db.py — handles SQLite database for user history

import sqlite3

DB_NAME = "news.db"

# Initialize database
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

# Create history table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT
)
""")
conn.commit()

# Function to log an article

def log_article(title, category):
    cursor.execute("INSERT INTO history (title, category) VALUES (?, ?)", (title, category))
    conn.commit()

# Function to fetch user history

def get_history():
    cursor.execute("SELECT title, category FROM history ORDER BY id DESC LIMIT 10")
    return cursor.fetchall()

# Function to recommend based on category

def recommend_articles(category):
    cursor.execute("SELECT title FROM history WHERE category = ? ORDER BY id DESC LIMIT 5", (category,))
    return [row[0] for row in cursor.fetchall()]

if __name__ == "__main__":
    # Quick test
    log_article("Test News Article", "Technology")
    print("History:", get_history())
    print("Recommendations for 'Technology':", recommend_articles("Technology"))