import sqlite3
import os
from app.config import DB_PATH

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY,
        name TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS versions (
        id INTEGER PRIMARY KEY,
        document_id INTEGER,
        version_number INTEGER,
        created_at TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS nodes (
        id INTEGER PRIMARY KEY,
        version_id INTEGER,
        heading TEXT,
        level INTEGER,
        body TEXT,
        parent_id INTEGER,
        hash TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS selections (
        id INTEGER PRIMARY KEY,
        name TEXT,
        node_ids TEXT,
        created_at TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS generated_tests (
        id INTEGER PRIMARY KEY,
        selection_id INTEGER,
        version_id INTEGER,
        tests_json TEXT,
        prompt TEXT,
        generated_at TEXT,
        node_hashes TEXT
    )''')

    conn.commit()
    conn.close()

def get_db():
    return sqlite3.connect(DB_PATH)

def insert_document(name):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO documents (name) VALUES (?)", (name,))
    conn.commit()
    doc_id = c.lastrowid
    conn.close()
    return doc_id

def insert_version(doc_id, ver_num, created_at):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO versions (document_id, version_number, created_at) VALUES (?, ?, ?)",
              (doc_id, ver_num, created_at))
    conn.commit()
    ver_id = c.lastrowid
    conn.close()
    return ver_id

def insert_node(version_id, heading, level, body, parent_id, hash_val):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO nodes (version_id, heading, level, body, parent_id, hash) VALUES (?, ?, ?, ?, ?, ?)",
              (version_id, heading, level, body, parent_id, hash_val))
    conn.commit()
    node_id = c.lastrowid
    conn.close()
    return node_id

def get_nodes(version_id=None):
    conn = get_db()
    c = conn.cursor()
    if version_id:
        c.execute("SELECT * FROM nodes WHERE version_id = ?", (version_id,))
    else:
        c.execute("SELECT * FROM nodes")
    rows = c.fetchall()
    conn.close()
    return rows

def get_node(node_id):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM nodes WHERE id = ?", (node_id,))
    row = c.fetchone()
    conn.close()
    return row

def search_nodes(term):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM nodes WHERE heading LIKE ? OR body LIKE ?", (f"%{term}%", f"%{term}%"))
    rows = c.fetchall()
    conn.close()
    return rows

def insert_selection(name, node_ids, created_at):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO selections (name, node_ids, created_at) VALUES (?, ?, ?)",
              (name, str(node_ids), created_at))
    conn.commit()
    sel_id = c.lastrowid
    conn.close()
    return sel_id

def get_selection(sel_id):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM selections WHERE id = ?", (sel_id,))
    row = c.fetchone()
    conn.close()
    return row

def insert_generated_test(selection_id, version_id, tests_json, prompt, generated_at, node_hashes):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO generated_tests (selection_id, version_id, tests_json, prompt, generated_at, node_hashes) VALUES (?, ?, ?, ?, ?, ?)",
              (selection_id, version_id, tests_json, prompt, generated_at, node_hashes))
    conn.commit()
    test_id = c.lastrowid
    conn.close()
    return test_id

def get_generated_test(selection_id):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM generated_tests WHERE selection_id = ? ORDER BY generated_at DESC LIMIT 1", (selection_id,))
    row = c.fetchone()
    conn.close()
    return row

def get_versions():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM versions")
    rows = c.fetchall()
    conn.close()
    return rows
