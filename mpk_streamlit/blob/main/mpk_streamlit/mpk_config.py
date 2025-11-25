# ----------------------------
# MPK Engine Configuration File
# ----------------------------

def load_config():
    """
    Returns global configuration settings for the MPK Engine.
    """
    return {
        "system_name": "MPK Engine",
        "max_memory_items": 200,

        # RSS News Sources
        "rss_sources": [
            "https://www.myanmar-now.org/en/rss",
            "https://www.bbc.com/news/world/asia/rss.xml",
            "https://www.irrawaddy.com/feed",
            "https://www.dvb.no/feed"
        ]
    }
