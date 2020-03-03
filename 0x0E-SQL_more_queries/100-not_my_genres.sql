-- Query that list the genres not linked by the show dexter using sub query
SELECT gen.name from tv_genres gen WHERE gen.id NOT IN (SELECT sg.genre_id FROM tv_show_genres sg INNER JOIN tv_shows tv ON sg.show_id = tv.id WHERE tv.title = "Dexter") ORDER BY gen.name ASC;
