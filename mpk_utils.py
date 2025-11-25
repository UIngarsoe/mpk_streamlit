mpk_utils.py
# ----------------------------
# Utility functions: login validation, content parsing
# ----------------------------
from mpk_config import VIP_USERS

def validate_vip(username, code):
    """Check VIP login credentials"""
    return VIP_USERS.get(username) == code

def summarize_memory(memory_entries):
    """Return a structured summary of memory for 3-P style response"""
    summary = {"People": [], "Power": [], "Practice": []}
    for entry in memory_entries:
        content = entry.get("content", "")
        # Simple split: user can structure uploads with markers if desired
        if "People" in content:
            summary["People"].append(content)
        elif "Power" in content:
            summary["Power"].append(content)
        elif "Practice" in content:
            summary["Practice"].append(content)
        else:
            summary["Practice"].append(content)
    return summary

