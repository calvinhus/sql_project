import os
import pandas as pd
import mysql.connector

# Fetch mySQL password from env variable
sql_pass = os.environ["MYSQL_PASSWORD"]

conn = mysql.connector.connect(user='root', password=sql_pass,
                               host='127.0.0.1',
                               database='datalake')

# Check if connection is successful
try:
    flag = conn.is_connected()
    print("\nConnected!\n")
except:
    print("Could not connect to database.")

# Create a cursor
c = conn.cursor()


def db_structure():
    """This method creates the database and the necessary tables. It takes no parameters."""

    # Create database
    create_db = "CREATE DATABASE IF NOT EXISTS ironhack_db;"
    c.execute(create_db)

    badges_table = """CREATE TABLE IF NOT EXISTS ironhack_db.badges
                        (
                            index INT NOT NULL PRIMARY KEY,
                            name VARCHAR(30),
                            keyword VARCHAR(30),
                            description VARCHAR(250),
                            school VARCHAR(10),
                            school_id SMALLINT
                        );    
                """
    c.execute(badges_table)

    courses_table = """CREATE TABLE IF NOT EXISTS ironhack_db.courses
                        (
                            index INT NOT NULL PRIMARY KEY,
                            courses VARCHAR(50),
                            school VARCHAR(10),
                            school_id SMALLINT
                        );    
                """
    c.execute(courses_table)

    locations_table = """CREATE TABLE IF NOT EXISTS ironhack_db.locations
                        (
                            index INT NOT NULL PRIMARY KEY,
                            id INT,
                            description VARCHAR(30)
                            country_id INT,
                            country_name VARCHAR(30)
                            country_code VARCHAR(2),
                            city_id INT,
                            city_name VARCHAR(20),
                            school VARCHAR(10),
                            school_id SMALLINT
                        );    
                """
    c.execute(locations_table)

    school_table = """CREATE TABLE IF NOT EXISTS ironhack_db.school
                        (
                            index INT NOT NULL PRIMARY KEY,
                            website VARCHAR(30),
                            description VARCHAR(300),
                            school VARCHAR(10),
                            school_id SMALLINT
                        );    
                """
    c.execute(school_table)

    comments_table = """CREATE TABLE IF NOT EXISTS ironhack_db.comments
                        (
                            index INT PRIMARY KEY,
                            name VARCHAR(100),
                            anonymous BIT(1),
                            is_alumni BIT(1),
                            program VARCHAR(50),
                            duration VARCHAR(3),
                            grad_year DATE,
                            job_title VARCHAR(50),
                            review TEXT,
                            overall FLOAT,
                            curriculum FLOAT,
                            job_support FLOAT,
                            avg_rating FLOAT AS ((overall + curriculum + job_support) / 3)
                        );    
                """
    c.execute(comments_table)


def db_insert(badges_values, courses_values, locations_values, school_values, comments_values):
    """This method inserts new records in the database each time the datalake is updated"""

    c.execute("USE ironhack_db;")

    insert_query = """DELETE FROM badges_table;
                      INSERT INTO badges_table ()
                      VALUES (%s, %s, %s);
                """
    badges_values = (10, 20, 30)
    c.execute(insert_query, badges_values)
    conn.commit()

    insert_query = """DELETE FROM courses_table;
                      INSERT INTO courses_table ()
                      VALUES (%s, %s, %s);
                """
    courses_values = (10, 20, 30)
    c.execute(insert_query, courses_values)
    conn.commit()

    insert_query = """DELETE FROM locations_table;
                      INSERT INTO locations_table ()
                      VALUES (%s, %s, %s);
                """
    locations_values = (10, 20, 30)
    c.execute(insert_query, locations_values)
    conn.commit()

    insert_query = """DELETE FROM school_table;
                      INSERT INTO school_table ()
                      VALUES (%s, %s, %s);
                """
    school_values = (10, 20, 30)
    c.execute(insert_query, school_values)
    conn.commit()

    insert_query = """DELETE FROM comments_table;
                      INSERT INTO comments_table ()
                      VALUES (%s, %s, %s);
                """
    comments_values = (10, 20, 30)
    c.execute(insert_query, comments_values)
    conn.commit()


# Close the cursor and the connection
c.close()
conn.close()
