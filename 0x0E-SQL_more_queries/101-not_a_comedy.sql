-- List all shows without the genre Comedy
-- Each record should display: tv_shows.title
-- Results are sorted in ascending order by the show title
SELECT DISTINCT ts.title
  FROM tv_shows AS ts
		LEFT JOIN tv_show_genres AS tsg
		ON tsg.show_id = ts.id
 WHERE tsg.show_id NOT IN (
			   SELECT tsg.show_id
			   FROM tv_genres AS tg
			   INNER JOIN tv_show_genres AS tsg
			   ON tsg.genre_id = tg.id
			   WHERE tg.name = 'Comedy'
		)
		OR tsg.genre_id IS NULL
 ORDER BY ts.title;
