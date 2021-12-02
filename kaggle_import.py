import csv
from main import conn

INPUT_CSV_FILE = 'top500mangaMAL.csv'

query_create_table = '''
create table manga_new(
    manga_id int,
    title varchar(100) not null,
    rating decimal(8,2)
);
'''

query_insert_data = '''
insert into manga_new (manga_id, title, rating) values (%s, %s, %s)
'''

with conn:
    cur = conn.cursor()
    cur.execute(query_create_table)
    with open(INPUT_CSV_FILE, 'r', encoding="utf-8") as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (row['Manga ID'], row['English Title'], row['Score'])
            cur.execute(query_insert_data, values)

    conn.commit()
