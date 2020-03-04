-- Query that list the ranting by genre usin inner join and group by
SELECT gen.name, SUM(rt.rate) AS rating FROM tv_genres gen INNER JOIN tv_show_genres sg ON gen.id = sg.genre_id INNER JOIN tv_shows tv ON sg.show_id = tv.id INNER JOIN tv_show_ratings rt ON tv.id = rt.show_id GROUP BY gen.name ORDER BY rating DESC;
