CREATE EXTERNAL TABLE IF NOT EXISTS review
(
	funny string,
	user_id string,
	review_id string,
	text string,
	business_id string,
	stars string,
	date string,
	useful string,
	cool string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "," ESCAPED BY '\\'
STORED AS TEXTFILE
LOCATION '/user/w205/yelp_dataset/review';