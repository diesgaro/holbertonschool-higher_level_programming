-- Query that list the number of records with the same score using GROUP BY
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
