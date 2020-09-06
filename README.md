PROJECT-3: Data Warehouse

This project is the third project for Udacity Data Engineering Nanodegree Program. The project aims to test the understanding of Data warehousing concepts. The task includes facilitating the Sparkify start up in setting up a data warehouse that would have the songs data to which the users are listening to. This would help Sparkify analyze the user activities.

The project is written in python and uses Amazon s3 for file storage and Amazon Redshift for database storage and data warehouse purpose.
Source Data

The source data is in log files given the Amazon s3 bucket at s3://udacity-dend/log_data and s3://udacity-dend/song_data containing log data and songs data respectively.

Log files contains songplay events of the users in json format while song_data contains list of songs details.
Database Schema

Following are the fact and dimension tables made for this project:
Dimension Tables:

    users
        columns: user_id, first_name, last_name, gender, level
    songs
        columns: song_id, title, artist_id, year, duration
    artists
        columns: artist_id, name, location, lattitude, longitude
    time
        columns: start_time, hour, day, week, month, year, weekday

Fact Table:

    songplays
        columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
        
There is an ERD attached for sparkify DB schema.


How to run the project:

Fill in AWS acces key (KEY) and secret (SECRET) in DWH.cfg file.

To access AWS, you need to do in AWS the following:

    create IAM user (e.g. sparkify)
    create IAM role (e.g. sparkifydwhRole) with AmazonS3ReadOnlyAccess access rights
    get ARN
    create and run Redshift cluster (e.g. SparkifyCluster => HOST)
    Create clients for IAM, S3 and Redshift

For creating IAM role, getting ARN and running cluster, you can use create_cluster.ipynb.

Run python create_tables.py. This will create the database and all the required tables.

Run python etl.py. This will start pipeline which will read the data from files and populate the tables.




