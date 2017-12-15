# W205 Project : Sentiment Analysis on Yelp Dataset

### Project Directory Structure
* aggregation : SQL file for data processing
* app : Apache Storm App - Tweet Monitor
* loading and modelling	: sctiops for database setup
* screenshot : Screenshots for key use-case

---
### Environment Setup
* Launch EC2
* Mount EBS
```
mount -t ext4 /dev/XXX /data
```
* Start Hadoop
```
/root/start-hadoop.sh
```
* Start Postgres
```
/data/start_postgres.sh
```
* Switch User
```
su - w205
```


---
### Loading and Modelling

#### Get the Yelp Dataset
```
wget https://s3.amazonaws.com/jelyee/yelp_dataset.tar
```

#### Convert json to csv using json_to_csv_converter.py
json_to_csv_converter.py loacted under folder /loading and modeling

```
python json_to_csv_converter.py business.json
python json_to_csv_converter.py checkin.json
python json_to_csv_converter.py review.json
python json_to_csv_converter.py tip.json
python json_to_csv_converter.py user.json
```

#### Move csv files to HDFS and create tables using Hive
Run create table scrips under folder /loading and modeling


---
### Data Processing
Run SQL script 'word_score.sql' under folder /aggregation


---
### Run sample sql to verify data processing
SELECT word, average_stars, count FROM review_words WHERE count > 100 ORDER BY aerage_stars DESC LIMIT 50;

![Top Positive Words](https://github.com/jey-lee/W205_project/blob/master/screenshot/screenshot-top_positive_words.png "Top Positive Words")


---
### Export Table to CSV, import to Postgres
#### Export table from Hive to CSV
```
hive -e 'select * from review_words_avg' | sed 's/[\t]/,/g' > review_words_avg.csv
```

#### Create Table in Postgres
```
CREATE TABLE review_words_avg 
(word varchar, score double precision, count double precision);
```

#### Import CSV to Postgres
```
COPY 
        review_words_avg(word, score, count)
FROM '/data/yelp_dataset/review_words_avg/review_words_avg.csv' DELIMITER ',' CSV HEADER;
```


---
### Run Sentiment classifier on words
```
python sentiment_classifier.py amazing
```
![Sentiment Classifier](https://github.com/jey-lee/W205_project/blob/master/screenshot/screenshot-sentiment_classifier.png "Sentiment classifier")

---
### Run Apache Storm - Tweet Monitor
Apache Storm Tweet Monitor App set up under folder app/tweetmonitor
Use below command under app/tweetmonitor to run
```
sparse run
```



