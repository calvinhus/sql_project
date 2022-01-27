import os
import mysql.connector

# Fetch mySQL password from env variable
sql_pass = os.environ["MYSQL_PASSWORD"]


def db_structure(connection):
    """This method creates the database and the necessary tables. It takes the connection to the database as a parameter."""

    # Create a cursor
    c = connection.cursor()
    # Create database
    create_db = "CREATE DATABASE IF NOT EXISTS ironhack_db;"
    c.execute(create_db)

    # Table: badges
    badges_table = """CREATE TABLE IF NOT EXISTS ironhack_db.badges
                        (
                            `index` INT NOT NULL PRIMARY KEY,
                            `name` VARCHAR(30),
                            `keyword` VARCHAR(30),
                            `description` VARCHAR(250),
                            `school` VARCHAR(10),
                            `school_id` SMALLINT
                        );    
                """
    c.execute(badges_table)

    # Table: courses
    courses_table = """CREATE TABLE IF NOT EXISTS ironhack_db.courses
                        (
                            `index` INT NOT NULL PRIMARY KEY,
                            `courses` VARCHAR(50),
                            `school` VARCHAR(10),
                            `school_id` SMALLINT
                        );    
                """
    c.execute(courses_table)

    # Table: locations
    locations_table = """CREATE TABLE IF NOT EXISTS ironhack_db.locations
                        (
                            `index` INT NOT NULL PRIMARY KEY,
                            `id` INT,
                            `description` VARCHAR(30),
                            `country_id` INT,
                            `country_name` VARCHAR(30),
                            `country_code` VARCHAR(2),
                            `city_id` INT,
                            `city_name` VARCHAR(20),
                            `school` VARCHAR(10),
                            `school_id` SMALLINT
                        );    
                """
    c.execute(locations_table)

    # Table: school
    school_table = """CREATE TABLE IF NOT EXISTS ironhack_db.school
                        (
                            `index` INT NOT NULL PRIMARY KEY,
                            `website` VARCHAR(30),
                            `description` VARCHAR(300),
                            `school` VARCHAR(10),
                            `school_id` SMALLINT
                        );    
                """
    c.execute(school_table)

    # Table: commments
    comments_table = """CREATE TABLE IF NOT EXISTS ironhack_db.comments
                        (
                            `index` INT PRIMARY KEY,
                            `name` VARCHAR(100),
                            `anonymous` BIT(1),
                            `is_alumni` BIT(1),
                            `program` VARCHAR(50),
                            `duration` VARCHAR(3),
                            `grad_year` DATE,
                            `job_title` VARCHAR(50),
                            `Work_inField` BIT(1),
                            `review` TEXT,
                            `overall` FLOAT,
                            `curriculum` FLOAT,
                            `job_support` FLOAT,
                            `avg_rating` FLOAT AS ((overall + curriculum + job_support) / 3)
                        );    
                """
    c.execute(comments_table)

    # Close cursor and connection
    c.close()
    connection.close()


def db_insert(comments_values):
    """This method inserts the cleaned data from the datalake database into ironhack_db"""
    connection = mysql.connector.connect(user='root', password=sql_pass,
                                         host='127.0.0.1',
                                         database='ironhack_db')
    # Create a cursor
    c = connection.cursor()

    c.execute("USE ironhack_db;")

    # Table: badges
    insert_query = """DELETE FROM badges;
                        INSERT INTO badges (index, name, keyword, description, school, school_id )
                        VALUES (%s, %s, %s, %s, %s, %s);
                """
    badges_values = (10, 20, 30)
    c.executemany(insert_query, badges_values)

    # Table: courses
    insert_query = """DELETE FROM courses;
                        INSERT INTO courses (index, courses, school, school_id)
                        VALUES (%s, %s, %s, %s);
                """
    courses_values = (10, 20, 30)
    c.executemany(insert_query, courses_values)

    # Table: locations
    insert_query = """DELETE FROM locations;
                        INSERT INTO locations (index, id, description, country_id, country_name, country_code, city_id, city_name, school, school_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
    locations_values = (10, 20, 30)
    c.executemany(insert_query, locations_values)

    # Table: school
    insert_query = """DELETE FROM school;
                        INSERT INTO school (index, website, description, school, school_id)
                        VALUES (%s, %s, %s, %s, %s);
                """
    school_values = (10, 20, 30)
    c.executemany(insert_query, school_values)

    # Table: comments
    insert_query = """DELETE FROM comments;
                        INSERT INTO ironhack_db.comments (`index`, `name`) 
                        VALUES (%s, %s); 
                """
    c.executemany(insert_query, comments_values)

    # Commit the transaction
    connection.commit()

    # Close cursor and connection
    c.close()
    connection.commit()
