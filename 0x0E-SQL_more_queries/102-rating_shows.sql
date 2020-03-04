-- Query that list shows rating using inner join and group by
SELECT tv.title, SUM(rt.rate) AS rating FROM tv_shows tv INNER JOIN tv_show_ratings rt ON tv.id = rt.show_id GROUP BY tv.title ORDER BY rating DESC;
