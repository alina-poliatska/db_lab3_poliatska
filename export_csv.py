import csv
from main import conn

OUTPUT_FILE_T = 'Poliatska_DB_{}.csv'

TABLES = [
    'manga',
    'author',
    'manga_author',
    'genre',
    'manga_genre',
]

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('select * from ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])

