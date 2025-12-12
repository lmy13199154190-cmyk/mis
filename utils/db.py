# utils/db.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data_roadshow.db"

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password_hash TEXT,
        role TEXT
    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS cabinets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cabinet_id TEXT UNIQUE,
        location TEXT,
        status TEXT
    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS cameras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        camera_id TEXT UNIQUE,
        cabinet_id TEXT,
        location TEXT,
        status TEXT
    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT UNIQUE,
        user_id TEXT,
        courier_id TEXT,
        cabinet_id TEXT,
        order_time TEXT,
        delivery_time TEXT,
        in_cabinet_time TEXT,
        out_cabinet_time TEXT,
        status TEXT,
        risk_score REAL,
        notes TEXT
    )''')
    con.commit()
    return con

def query(con, sql, params=(), fetch=False):
    cur = con.cursor()
    cur.execute(sql, params)
    if fetch:
        return cur.fetchall()
    con.commit()
    return None
