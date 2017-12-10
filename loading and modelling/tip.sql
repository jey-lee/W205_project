CREATE EXTERNAL TABLE IF NOT EXISTS tip
(
	user_id string,
	text string,
	business_id string,
	likes string,
	date string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "," ESCAPED BY '\\'
STORED AS TEXTFILE
LOCATION '/user/w205/yelp_dataset/tip';
