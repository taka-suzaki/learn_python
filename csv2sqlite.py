import pandas as pd
import sqlite3

path = "../taka-suzaki/aozora_bunko/data/list_person_all_extract_utf8.csv"
savepath = "./data/sqlite3/books.db"
table_name = "books"


df = pd.read_csv(path)
with sqlite3.connect(savepath) as conn:
    df.to_sql(table_name, con=conn)