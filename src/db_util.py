import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path(__file__).parent.parent / "jp.db"
RESOURCES_DIR = Path(__file__).parent.parent / "resources"



def export_db():

    conn = sqlite3.connect(DB_PATH)
    grammar_sql = "SELECT title,usage,meaning,explanation,sentences,level FROM grammar"
    grammar_file = "grammar.csv"
    vocabulary_sql = "SELECT word,transliteration,meaning,sentences FROM vocabulary"
    vocabulary_file = "vocabulary.csv"
    df = pd.read_sql_query(
        grammar_sql,
        conn
    )
    CSV_FILE = RESOURCES_DIR / grammar_file
    df.to_csv(
        CSV_FILE,
        index=False,
        sep="|",
        encoding="utf-8"
    )

    conn.close()


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



export_db()