-- List all shows by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating
SELECT ts.title, SUM(tsr.rate) AS rating
  FROM tv_shows AS ts
		INNER JOIN tv_show_ratings AS tsr
		ON ts.id = tsr.show_id
 GROUP BY ts.title
 ORDER BY rating DESC;
