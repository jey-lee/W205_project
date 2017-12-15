-- Create a new review table with minimum column
CREATE TABLE 
	review_compact 
AS 
SELECT 
	user_id, 
	text, 
	stars 
FROM 
	review 
WHERE text IS NOT NULL 
AND TEXT NOT IN ("1","2","3","4","5")
AND stars IN ("1","2","3","4","5") 
AND LENGTH(user_id) ==22
;


-- Tokenize review text to words
CREATE TABLE 
	review_words_temp 
AS 
SELECT 
	user_id, 
	words, 
	stars 
FROM 
	review_compact 
LATERAL VIEW EXPLODE(SPLIT(text," ")) texts AS words
;


-- Remove special character, lowercase all words
CREATE TABLE 
	review_words_temp_2 
AS 
SELECT
	user_id, 
	LOWER(regexp_replace(translate(words,'.',''),"\!\?","")) AS words, 
	stars 
FROM 
	review_words_temp
;


-- Create a new user table with minimum column
CREATE TABLE 
	user_compact 
AS 
SELECT 
	user_id, 
	average_stars 
FROM 
	user 
WHERE LENGTH(user_id) ==22
;



-- Join Review table and User table on user_id and apply weight based on user's average stars
CREATE TABLE 
	review_words_weighted 
AS 
SELECT 
	a.user_id, 
	a.words AS word, 
	a.stars stars, 
	(a.stars - b.average_stars + 5) AS weighted_stars 
FROM 
	review_words_temp_2 a, 
	user_compact b 
WHERE a.user_id = b.user_id
;


-- Generate review_words table with the aggregated stars, weighted stars value
CREATE TABLE 
	review_words 
AS 
SELECT 
	word, 
	avg(stars) average_stars, 
	avg(weighted_stars) AS weighted_average_stars, 
	count(word) count 
FROM 
	review_words_weighted 
GROUP BY word
;
