import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, text

#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages
# Import our modules
import database as db
import datacleaning as dc
import queries as q
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
    comments_df['duration'] = comments_df.apply(dc.duration_program, axis=1)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_DA_clean)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_UXUI_clean)
    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_WD_clean)

    comments_df['Work_inField'] = comments_df['jobTitle'].apply(
        dc.jobTitle_CS_clean)

    comments_df['overallScore'] = comments_df['overallScore'].astype(float)
    labels = ['E', 'D', 'C', 'B', 'A']
    comments_df["Ranking"] = pd.cut(
        comments_df['overallScore'], 5, labels=labels)

    # Call method to create database and all tables
    db.db_structure(conn)
    # print("\nDatabase and tables created.\n")
    c.close()
    conn.close()

    conn2 = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                          .format(user="root",
                                  pw=sql_pass,
                                  db="ironhack_db"))

    comments_df.to_sql('comments', con=conn2,
                       if_exists='replace', chunksize=1000)

    print("\nDatabase tables updated.\n")

    # Queries
    curriculum_time = conn2.execute(text(q.curriculum_time))
    curriculum_time_df = pd.DataFrame(curriculum_time)

    job_support_time = conn2.execute(text(q.job_support_time))
    job_support_time_df = pd.DataFrame(job_support_time)

    overall_score_time = conn2.execute(text(q.overall_score_time))
    overall_score_time_df = pd.DataFrame(overall_score_time)

    part_time_score = conn2.execute(text(q.part_time_score))
    part_time_score_df = pd.DataFrame(part_time_score)

    full_time_score = conn2.execute(text(q.full_time_score))
    full_time_score_df = pd.DataFrame(full_time_score)

    profile_by_program = conn2.execute(text(q.profile_by_program))
    profile_by_program_df = pd.DataFrame(profile_by_program)

    profile_by_alumni = conn2.execute(text(q.profile_by_alumni))
    profile_by_alumni_df = pd.DataFrame(profile_by_alumni)

    profile_by_workInField = conn2.execute(text(q.profile_by_workInField))
    profile_by_workInField_df = pd.DataFrame(profile_by_workInField)

    overall_student_rate = conn2.execute(text(q.overall_student_rate))
    overall_student_rate_df = pd.DataFrame(overall_student_rate)

    curriculum_student_rate = conn2.execute(text(q.curriculum_student_rate))
    curriculum_student_rate_df = pd.DataFrame(curriculum_student_rate)

    jobSupport_student_rate = conn2.execute(text(q.jobSupport_student_rate))
    jobSupport_student_rate_df = pd.DataFrame(jobSupport_student_rate)
    # Queries done

    print(curriculum_time_df.head())
    print(job_support_time_df.head())
    print(overall_score_time_df.head())
    # average overall score by part time course
    print(part_time_score_df.head())
    # average overall score by part time course
    print(full_time_score_df.head())
    print(profile_by_program_df.head())
    print(profile_by_alumni_df.head())
    print(profile_by_workInField_df.head())
    print(overall_student_rate_df.head())
    print(curriculum_student_rate_df.head())
    print(jobSupport_student_rate_df.head())

    # create a PdfPages object
    # f1 = plt.figure()
    # pdf = PdfPages('report.pdf')
    # f1 = plt.figure()
    # curriculum_time_df.plot(kind='bar', x='graduatingYear',
    #                        y = 'AVG(curriculum)', legend = False)
    # pdf.savefig(f1)

    # plt.close("all")
    # pdf.close()

except mysql.connector.Error as err:
    print(f"\nSorry. Smething went wrong :(\n{format(err)}\n")

finally:
    if conn.is_connected():
        c.close()
        print("MySQL connection is closed")
