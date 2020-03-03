-- Query that list all the tv shows and all genres using left join
SELECT tv.title, gen.name FROM tv_shows tv LEFT JOIN tv_show_genres sg ON tv.id = sg.show_id LEFT JOIN tv_genres gen ON sg.genre_id = gen.id ORDER BY tv.title, gen.name ASC;
