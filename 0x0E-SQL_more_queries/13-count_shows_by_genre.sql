-- Query that list all genres and displays the number of shows linked
-- to each using inner join and group by
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) as number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
