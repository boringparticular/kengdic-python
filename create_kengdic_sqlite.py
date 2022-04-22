import sqlite3
import pandas as pd
import os


def mkdir_soft(*path):
    try:
        os.mkdir(os.path.join(*path))
    except OSError:
        pass


pkg_dir = "kengdic"
data_dir = "sqlite"
filename = "kengdic_2011.sqlite"
origin = "../kengdic_2011.tsv"

mkdir_soft(pkg_dir)
mkdir_soft(pkg_dir, data_dir)
dest = os.path.join(pkg_dir, data_dir, filename)

kengdic_fields = [
    "word_id",
    "korean",
    "synonym",
    "english",
    "part_of_speech_number",
    "part_of_speech",
    "submitter",
    "date_of_entry",
    "word_size",
    "hanja",
    "word_id2",
    "extra_data",
]


def import_tsv():
    data = pd.read_csv(
        origin, sep="\t", index_col=None, header=None, low_memory=False, encoding="utf8"
    )
    data.columns = kengdic_fields
    with sqlite3.connect(dest) as conn:
        c = conn.cursor()
        try:
            _ = c.execute("drop table kengdic;")
        except sqlite3.OperationalError:
            pass
        _ = c.execute("create table kengdic ({});".format(", ".join(kengdic_fields)))
        conn.commit()
        _ = c.execute(
            "create index index_wordid on kengdic ( word_id, korean, date_of_entry );"
        )
        conn.commit()
        entry_statement = "insert or fail into kengdic values ({})".format(
            ",".join(["?"] * data.shape[1])
        )
        for index, entry in data.iterrows():
            _ = c.execute(entry_statement, entry.values.tolist())
        count = next(c.execute("select count(word_id) from kengdic;"))[0]
        print("imported {} words".format(count))
        conn.commit()


if __name__ == "__main__":
    import_tsv()
