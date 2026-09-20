import sqlite3

DB_FILE = "history.db"

def get_conn():   # 获取数据库连接
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row # 让查询结果带上字段名
    return conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            score REAL NOT NULL,
            label TEXT NOT NULL,
            pinyin TEXT NOT NULL,
            created_at DATETIME NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_record(record):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (text, score, label, pinyin, created_at) VALUES (?, ?, ?, ?, ?)", (record['text'], record['score'], record['label'], record['pinyin'], record['created_at']))
    conn.commit()
    conn.close()

def get_history(limit):
    conn = get_conn()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM history ORDER BY created_at DESC LIMIT ?", (limit,)).fetchall()
    conn.close()    # 关闭数据库连接
    
    records = []
    for row in records:
        records.append(dict(row))
    return records



