import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """This function iterates over the list of load queries that load the data from
    files in s3 bucket to the stage tables using COPY command.
    INPUTS:
    * cur the cursor variable of the database
    * conn the connection variable of the database"""
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """Insert data from staging tables (staging_events and staging_songs) into star schema analytics tables:
    * Fact table: songplays
    * Dimension tables: users, songs, artists, time
    Keyword arguments:
    * cur --    reference to connected db.
    * conn --   parameters (host, dbname, user, password, port) to connect the DB.
    Output:
    * Data inserted from staging tables to dimension tables.
    * Data inserted from staging tables to fact table."""
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Connect to DB and call
    * load_staging_tables to load data from JSON files
    (song_data and log_data in S3) to staging tables and
    * insert_tables to insert data to analysis tables.
    Keyword arguments:
    * None
    Output:
    * All input data processed in DB tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()