import json

HISTORY_FILE = "history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_record(record):
    records = load_history()
    records.append(record)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def get_history(all: bool = False):
    records = load_history()
    total = len(records)
    records.reverse()
    if not all:
        records = records[:10]
    return {
        "records": records,
        "total": total,
    }

