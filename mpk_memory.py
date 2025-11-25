mpk_memory.py
# ----------------------------
# VIP Memory storage for uploads
# ----------------------------
import os
import json
from datetime import datetime

MEMORY_DIR = "memory"
os.makedirs(MEMORY_DIR, exist_ok=True)

def save_upload(uploader_id, title, content, upload_type):
    """Save a single upload into VIP memory JSON"""
    filepath = os.path.join(MEMORY_DIR, f"{uploader_id}.json")
    memory = []

    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            memory = json.load(f)

    entry = {
        "title": title,
        "content": content,
        "type": upload_type,
        "timestamp": str(datetime.now())
    }
    memory.append(entry)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def load_memory(uploader_id):
    """Load all memory uploads for a VIP uploader"""
    filepath = os.path.join(MEMORY_DIR, f"{uploader_id}.json")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

