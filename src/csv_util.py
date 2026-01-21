import pandas as pd
from pathlib import Path

from db_util import create_vocabulary_table, insert_vocabulary

RESOURCES_DIR = Path(__file__).parent.parent / "resources"
CSV_FILE = RESOURCES_DIR / "japanese_vocabulary_2000.csv"


def import_vocabulary_from_csv():
    df = pd.read_csv(
        CSV_FILE,
        engine="python",
        sep="\t",
        encoding="utf-8"
    )
    create_vocabulary_table()
    for _, row in df.iterrows():
        word = row["Word"]
        meaning = row["Meaning"]
        transliteration = row["Transliteration"]
        sentences = row["Example Sentence"]
        insert_vocabulary(
            word=word,
            meaning=meaning,
            sentences=sentences,
            transliteration=transliteration
        )


if __name__ == "__main__":
    import_vocabulary_from_csv()