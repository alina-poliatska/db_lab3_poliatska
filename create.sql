create table manga(
	manga_id int primary key not null,
	title varchar(50) not null,
	date date,
	rating decimal(8,2)
);

create table author(
	author_id int primary key not null,
	name varchar(30) not null
);


create table manga_author(
	id int primary key not null,
	manga_id int references manga(manga_id),
	author_id int references author(author_id)
);

create table genre(
	name varchar(30) primary key not null
);

create table manga_genre(
	id int primary key not null,
	manga_id int references manga(manga_id),
	genre_name varchar(30) references genre(name)
);
