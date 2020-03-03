-- Query that list all Comedy shows using inner join
SELECT tv.title FROM tv_shows tv INNER JOIN tv_show_genres sg ON tv.id = sg.show_id INNER JOIN tv_genres gen ON sg.genre_id = gen.id WHERE gen.name LIKE ("Comedy") ORDER BY tv.title ASC;
