import sqlite3


def create_grammar_table():
    conn = sqlite3.connect("jp.db")
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


def insert_grammar(title,usage, meaning, explanation, sentences,level):
    conn = sqlite3.connect("jp.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO grammar (title,usage, meaning, explanation,sentences, level) VALUES (?,?, ?, ?, ? , ?)",
        (title,usage, meaning, explanation, sentences, level)
    )

    conn.commit()
    conn.close()



