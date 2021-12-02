create table manga_copy as select * from manga
delete from manga_copy

DO $$
DECLARE
    manga_id int;
	title varchar(50);
	date date;
	rating decimal(8,2);
BEGIN
    manga_id = 100;
    title = 'manga';
	date = '1950-01-01';
	rating = '0.0';
    FOR counter IN 1..10
        LOOP
            INSERT INTO manga_copy(manga_id, title, date, rating)
            VALUES (manga_id + counter, title || counter, date, rating + counter);
        END LOOP;
END;
$$