-- Query that list the genres to the tv_show Dexter using inner join
SELECT gen.name FROM tv_genres gen INNER JOIN tv_show_genres sg ON gen.id = sg.genre_id INNER JOIN tv_shows tv ON sg.show_id = tv.id WHERE tv.title LIKE("Dexter") ORDER BY gen.name ASC;
