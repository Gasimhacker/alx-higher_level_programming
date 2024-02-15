-- List all shows contained in the database that without a genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows LEFT JOIN
                tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
 WHERE tv_show_genres.genre_id IS NULL
 ORDER BY tv_shows.title, tv_show_genres.genre_id;
