-- List all genres of the show Dexter
-- Each record should display: tv_genres.name
-- Results are sorted in ascending order by the genre name
SELECT tv_genres.name
  FROM tv_genres INNER JOIN
		tv_show_genres
		ON tv_show_genres.genre_id = tv_genres.id
 WHERE tv_show_genres.show_id IN (SELECT id
				    FROM tv_shows
				   WHERE title = 'Dexter')
 ORDER BY tv_genres.name;
