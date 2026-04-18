import sqlite3
import pandas as pd
import os
import datetime

DB_FILE = "car_data.csv"
DB_SQL = "car_system.db"

# --- User Auth Database ---
def init_db(db_path: str = DB_SQL):
    """Initialize the SQLite DB. If the DB file is corrupted, back it up and recreate a fresh DB.

    Returns True on success.
    """
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS system_logs (id INTEGER PRIMARY KEY, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()
        conn.close()
        return True
    except sqlite3.DatabaseError as e:
        # DB is malformed/corrupted. Move it aside and create a new DB.
        try:
            conn.close()
        except Exception:
            pass

        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupt_name = f"{db_path}.corrupt.{ts}"
        try:
            if os.path.exists(db_path):
                os.replace(db_path, corrupt_name)
        except Exception:
            # best-effort; if we can't move, ignore and continue to recreate
            pass

        # Create a fresh DB
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS system_logs (id INTEGER PRIMARY KEY, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
            conn.commit()
            conn.close()
            return True
        except Exception:
            return False

def add_user(username, password):
    conn = sqlite3.connect(DB_SQL)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def check_user(username, password):
    conn = sqlite3.connect(DB_SQL)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

# --- Car Inventory Database (CSV) ---
def get_all_cars():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    return pd.DataFrame()

def add_new_car(car_data):
    df = get_all_cars()
    new_df = pd.concat([df, pd.DataFrame([car_data])], ignore_index=True)
    new_df.to_csv(DB_FILE, index=False)
    return True

# 🔥 NAYA FEATURE: Database se gaadi delete karne ka logic
def delete_car(index):
    df = get_all_cars()
    if not df.empty and index in df.index:
        df = df.drop(index)
        df.to_csv(DB_FILE, index=False)
        return True
    return False