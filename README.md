# W205 Project : Sentiment Analysis on Yelp Dataset

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

### Loading and Modelling

#### Get the Yelp Dataset
wget https://s3.amazonaws.com/jelyee/yelp_dataset.tar

#### Convert json to csv using json_to_csv_converter.py
python json_to_csv_converter.py business.json

#### Move csv files to HDFS and create tables using Hive
Run create table scrips
