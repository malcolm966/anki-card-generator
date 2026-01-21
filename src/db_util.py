import sqlite3

def create_vocabulary_table():
    conn = sqlite3.connect("jp.db")
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

def insert_vocabulary(word, transliteration, meaning, sentences):
    conn = sqlite3.connect("jp.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vocabulary (word,transliteration, meaning, sentences) VALUES (?,?, ?, ?)",
        (word,transliteration, meaning, sentences)
    )

    conn.commit()
    conn.close()


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



