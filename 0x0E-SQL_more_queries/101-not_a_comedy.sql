-- Query that list all tv shows not comedy genre using sub-querys
SELECT tv.title FROM tv_shows tv WHERE tv.id NOT IN (SELECT sg.show_id FROM tv_show_genres sg INNER JOIN tv_genres gen ON sg.genre_id = gen.id WHERE gen.name LIKE ("Comedy")) ORDER BY tv.title ASC;
