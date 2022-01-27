import os
import pandas as pd
import mysql.connector

# Import our modules
import database as db
import datacleaning as dc

# Variable declaration
badges_values = ""
courses_values = ""
locations_values = ""
school_values = ""
comments_values = ""


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
    c.execute('SET SQL_SAFE_UPDATES = 0;')

    clean_job_title = """UPDATE datalake.comments
                         SET jobTitle = 'No info'
                         WHERE jobTitle  = '' OR jobTitle IS NULL;"""
    c.execute(clean_job_title)

    comments_df['program'] = comments_df.apply(dc.program_clean, axis=1)
    comments_df['price'] = comments_df.apply(dc.price_program, axis=1)
    comments_df['duration'] = comments_df.apply(dc.price_program, axis=1)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_DA_clean)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_UXUI_clean)

    # Call method to create database and all tables
    db.db_structure(conn)
    print("\nDatabase and tables created.\n")

    # Insert in the newly created tables
    # db.db_insert(badges_values, courses_values,
    #             locations_values, school_values, comments_values)
    #print("\nDatabase tables updated.\n")

except mysql.connector.Error as err:
    print(f"\nSorry. Smething went wrong :(\n{format(err)}\n")
