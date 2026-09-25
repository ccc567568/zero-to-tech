import json

HISTORY_FILE = "history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_record(sid, record):
    records = load_history()
    records.append({"sid": sid, "record": record})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def get_history(sid, limit=10):
    records = load_history()
    total = len(records)
    records.reverse()
    records = records[:10]
    


