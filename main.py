import psycopg2
import matplotlib.pyplot as plt

username = 'poliatska'
password = '111'
database = 'alina_lab2'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

query_1 = '''
create view MangaGenre as
select genre_name, count(distinct(manga_id)) from manga_genre group by genre_name
'''

query_2 = '''
create view MangaAuthor as
select name, count(title) from manga
join manga_author on manga.manga_id = manga_author.manga_id
join author on author.author_id = manga_author.author_id group by name
'''

query_3 = '''
create view MangaRating as
select genre_name, avg(rating) from manga
join manga_genre on manga.manga_id = manga_genre.manga_id group by genre_name
'''

cur = conn.cursor()


with conn:

    cur1 = conn.cursor()
    cur1.execute('DROP VIEW IF EXISTS MangaGenre')
    cur1.execute(query_1)
    cur1.execute('SELECT * FROM MangaGenre')
    countries = []
    sportsmen1 = []

    for row in cur1:
        countries.append(row[0])
        sportsmen1.append(row[1])

    cur2 = conn.cursor()
    cur2.execute('DROP VIEW IF EXISTS MangaAuthor')
    cur2.execute(query_2)
    cur2.execute('SELECT * FROM MangaAuthor')
    medals = []
    sportsmen2 = []

    for row in cur2:
        medals.append(row[0])
        sportsmen2.append(row[1])

    cur3 = conn.cursor()
    cur3.execute('DROP VIEW IF EXISTS MangaRating')
    cur3.execute(query_3)
    cur3.execute('SELECT * FROM MangaRating')
    games = []
    sportsmen3 = []

    for row in cur3:
        games.append(row[0])
        sportsmen3.append(row[1])


plt.bar(countries, sportsmen1, width=0.5)
plt.xlabel('Genre')
plt.ylabel('Number of manga')
plt.show()

fig, ax = plt.subplots()
ax.pie(sportsmen2, labels=medals, normalize=True)
plt.axis('equal')
plt.show()

plt.scatter(games, sportsmen3)
plt.show()
