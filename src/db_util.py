import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "jp.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_vocabulary_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            transliteration TEXT,
            meaning TEXT,
            sentences TEXT
        )
        """)
        conn.commit()


def insert_vocabulary(word, transliteration, meaning, sentences):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO vocabulary (word, transliteration, meaning, sentences) VALUES (?, ?, ?, ?)",
            (word, transliteration, meaning, sentences)
        )
        conn.commit()


def create_grammar_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS grammar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            usage TEXT,
            meaning TEXT,
            explanation TEXT,
            sentences TEXT,
            level TEXT
        )
        """)
        conn.commit()


def insert_grammar(title, usage, meaning, explanation, sentences, level):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO grammar (title, usage, meaning, explanation, sentences, level) VALUES (?, ?, ?, ?, ?, ?)",
            (title, usage, meaning, explanation, sentences, level)
        )
        conn.commit()



