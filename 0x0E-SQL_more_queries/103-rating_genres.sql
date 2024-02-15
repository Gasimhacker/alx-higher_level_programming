-- List all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results are sorted in descending order by the rating
SELECT tg.name, SUM(tsr.rate) AS rating
  FROM tv_show_genres AS tsg
		INNER JOIN tv_show_ratings AS tsr
		ON tsg.show_id = tsr.show_id

		INNER JOIN tv_genres AS tg
		ON tg.id = tsg.genre_id
 GROUP BY tg.name
 ORDER BY rating DESC;
