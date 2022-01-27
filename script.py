import database as db
import os
import pandas as pd
import mysql.connector

# Fetch mySQL password from env variable
sql_pass = os.environ["MYSQL_PASSWORD"]

# Create the connection
conn = mysql.connector.connect(user='root', password=sql_pass,
                               host='127.0.0.1',
                               database='datalake')

# Check if connection is successful
try:
    flag = conn.is_connected()
    print("\nConnected!\n")
except:
    print("Could not connect to database.")

badges_values = ""
courses_values = ""
locations_values = ""
school_values = ""
comments_values = ""

# Call method to create database and all tables
db.db_structure(conn)
print("\nDatabase and tables created.\n")

# Insert in the newly created tables
db.db_insert(badges_values, courses_values,
             locations_values, school_values, comments_values)
