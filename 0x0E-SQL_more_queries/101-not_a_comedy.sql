-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS sg
       ON sg.`show_id` = tv.`id`

       LEFT JOIN `tv_genres` AS gnr
       ON gnr.`id` = sg.`genre_id`
       WHERE tv.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS tv
	             INNER JOIN `tv_show_genres` AS sg
		     ON sg.`show_id` = tv.`id`

		     INNER JOIN `tv_genres` AS gnr
		     ON gnr.`id` = sg.`genre_id`
		     WHERE gnr.`name` = "Comedy")
 ORDER BY `title`;