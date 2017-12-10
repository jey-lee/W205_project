CREATE TABLE review_compact 
AS 
SELECT 
	text, 
	stars
FROM review 
WHERE text IS NOT NULL
AND text NOT IN ("1","2","3","4","5")
AND stars IN ("1","2","3","4","5")
;

CREATE TABLE review_words 
AS 
SELECT 
	words, 
	stars 
from review_compact 
LATERAL VIEW EXPLODE(SPLIT(text," ")) TEXTS AS WORDS
;


CREATE TABLE review_words_avg
AS 
SELECT  
	words, 
	AVG(stars) 
	average_stars, 
	COUNT(words) count 
FROM review_words 
GROUP BY words
;
	
