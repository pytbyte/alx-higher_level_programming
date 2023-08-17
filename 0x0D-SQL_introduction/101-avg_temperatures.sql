-- Displays the average temperature (in Fahrenheit)
-- the city can only get cloder
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;