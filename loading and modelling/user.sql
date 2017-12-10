CREATE EXTERNAL TABLE IF NOT EXISTS user
(
	yelping_since string,
	useful string,
	compliment_photos string,
	compliment_list string,
	compliment_funny string,
	compliment_plain string,
	review_count string,
	elite string,
	fans string,
	compliment_note string,
	funny string,
	compliment_writer string,
	compliment_cute string,
	average_stars string,
	user_id string,
	compliment_more string,
	friends string,
	compliment_hot string,
	cool string,
	name string,
	compliment_profile string,
	compliment_cool string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "," ESCAPED BY '\\'
STORED AS TEXTFILE
LOCATION '/user/w205/yelp_dataset/user';


