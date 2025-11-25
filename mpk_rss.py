mpk_rss.py
# ----------------------------
# RSS fetching & parsing for live updates
# ----------------------------
import feedparser
from mpk_config import RSS_FEEDS

def fetch_rss_headlines(limit=3):
    """Fetch latest headlines from configured RSS feeds"""
    updates = []
    for source_name, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        if feed.entries:
            for entry in feed.entries[:limit]:
                updates.append({
                    "source": source_name,
                    "title": entry.get("title", ""),
                    "link": entry.get("link", "")
                })
    return updates

