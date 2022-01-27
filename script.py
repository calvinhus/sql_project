import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
# Import our modules
import database as db
import datacleaning as dc

# Variable declaration
badges_values = []
courses_values = []
locations_values = []
school_values = []
comments_values = []

# Fetch mySQL password from env variable
sql_pass = os.environ["MYSQL_PASSWORD"]

try:
    # Create the connection
    conn = mysql.connector.connect(user='root', password=sql_pass,
                                   host='127.0.0.1',
                                   database='datalake')

    # Create cursor
    c = conn.cursor()

    c.execute("USE datalake;")
    c.execute('SET SQL_SAFE_UPDATES = 0;')

    clean_job_title = """UPDATE datalake.comments
                            SET jobTitle = 'No info'
                            WHERE jobTitle  = '' OR jobTitle IS NULL;"""
    c.execute(clean_job_title)

    clean_program_name = """UPDATE datalake.comments
                            SET hostProgramName = 'No info'
                            WHERE hostProgramName  = '' OR hostProgramName IS NULL;"""
    c.execute(clean_program_name)

    clean_program = """UPDATE datalake.comments
                            SET program = 'No info'
                            WHERE program  = '' OR program IS NULL;"""
    c.execute(clean_program)

    del_nulls = """DELETE FROM datalake.comments
                            WHERE jobSupport IS NULL OR curriculum IS NULL;"""
    c.execute(del_nulls)
    # Write queries to fetch data from datalake
    badges_query = "SELECT * FROM datalake.badges;"
    courses_query = "SELECT * FROM datalake.courses;"
    locations_query = "SELECT * FROM datalake.locations;"
    school_query = "SELECT * FROM datalake.school;"
    comments_query = "SELECT * FROM datalake.comments;"

    # Execute queries and save the result in a DataFrame
    c.execute(badges_query)
    badges_df = pd.DataFrame(c.fetchall())

    c.execute(courses_query)
    courses_df = pd.DataFrame(c.fetchall())

    c.execute(locations_query)
    locations_df = pd.DataFrame(c.fetchall())

    c.execute(school_query)
    school_df = pd.DataFrame(c.fetchall())

    c.execute(comments_query)
    comments_df = pd.DataFrame(c.fetchall(), columns=[
        name[0] for name in c.description])

    # Data Cleaning
    comments_df['program'] = comments_df.apply(dc.program_clean, axis=1)
    comments_df['price'] = comments_df.apply(dc.price_program, axis=1)
    comments_df['duration'] = comments_df.apply(dc.price_program, axis=1)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_DA_clean)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_UXUI_clean)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_WD_clean)

    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_CS_clean)

    # Call method to create database and all tables
    db.db_structure(conn)
    print("\nDatabase and tables created.\n")
    c.close()
    conn.close()

    # row['queryDate']), type(row['program']), type(row['overallScore']), type(row['overall']), type(row['curriculum']), type(row['jobSupport']), type(row['review_body']), type(row['school']), type(row['price']), type(row['duration']), type(row['Work_inField']))

    def insert_func(df):
        global sql_pass
        conn2 = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                              .format(user="root",
                                      pw=sql_pass,
                                      db="ironhack_db"))

        comments_df.to_sql('commentsnewtable', con=conn2,
                           if_exists='replace', chunksize=1000)

    print("\nDatabase tables updated.\n")
    insert_func(comments_df)

except mysql.connector.Error as err:
    print(f"\nSorry. Smething went wrong :(\n{format(err)}\n")

finally:
    if conn.is_connected():
        c.close()
        print("MySQL connection is closed")
