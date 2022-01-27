# Import libraries
import requests
import pandas as pd
import re
from sqlalchemy import create_engine
import os

# Fetch mySQL password from env variable
sql_pass = os.environ["MYSQL_PASSWORD"]

# Create a connection to the database
conn = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                     .format(user="root",
                             pw=sql_pass,
                             db="datalake"))

# Variable declaration
school_dict = {'ironhack': 10828}
locations_list = []
courses_list = []
badges_list = []
school_list = []


def get_comments_school(school):
    TAG_RE = re.compile(r'<[^>]+>')
    # defines url to make api call to data -> dynamic with school if you want to scrape competition
    url = "https://www.switchup.org/chimera/v1/school-review-list?mainTemplate=school-review-list&path=%2Fbootcamps%2F" + \
        school + "&isDataTarget=false&page=3&perPage=10000&simpleHtml=true&truncationLength=250"
    # makes get request and converts answer to json
    # url defines the page of all the information, request is made, and information is returned to data variable
    data = requests.get(url).json()
    # converts json to dataframe
    reviews = pd.DataFrame(data['content']['reviews'])

    # aux function to apply regex and remove tags
    def remove_tags(x):
        return TAG_RE.sub('', x)
    reviews['review_body'] = reviews['body'].apply(remove_tags)
    reviews['school'] = school
    return reviews


def get_school_info(school, school_id):
    url = 'https://www.switchup.org/chimera/v1/bootcamp-data?mainTemplate=bootcamp-data%2Fdescription&path=%2Fbootcamps%2F' + \
        str(school) + '&isDataTarget=false&bootcampId=' + str(school_id) + \
        '&logoTag=logo&truncationLength=250&readMoreOmission=...&readMoreText=Read%20More&readLessText=Read%20Less'

    data = requests.get(url).json()

    data.keys()

    courses = data['content']['courses']
    courses_df = pd.DataFrame(courses, columns=['courses'])

    locations = data['content']['locations']
    locations_df = pd.json_normalize(locations)

    badges_df = pd.DataFrame(data['content']['meritBadges'])

    website = data['content']['webaddr']
    description = data['content']['description']
    logoUrl = data['content']['logoUrl']
    school_df = pd.DataFrame([website, description, logoUrl]).T
    school_df.columns = ['website', 'description', 'LogoUrl']

    locations_df['school'] = school
    courses_df['school'] = school
    badges_df['school'] = school
    school_df['school'] = school

    locations_df['school_id'] = school_id
    courses_df['school_id'] = school_id
    badges_df['school_id'] = school_id
    school_df['school_id'] = school_id

    return locations_df, courses_df, badges_df, school_df


def create_datalake():
    """Create tables and populate them with data from the corresponding dataframe"""

    # Create cursor and datalake db
    #cur = conn.cursor()
    #cur.execute("CREATE DATABASE datalake;")
    #cur.execute("USE datalake;")
    # Drop tables to be able to insert data
    comments.drop(['user', 'body', 'rawBody', 'comments'],
                  inplace=True, axis=1)
    comments.to_sql('comments', con=conn,
                    if_exists='replace', chunksize=1000)

    locations.to_sql('locations', con=conn,
                     if_exists='replace', chunksize=1000)
    courses.to_sql('courses', con=conn, if_exists='replace', chunksize=1000)
    badges.to_sql('badges', con=conn, if_exists='replace', chunksize=1000)
    school.to_sql('school', con=conn, if_exists='replace', chunksize=1000)


for school, id in school_dict.items():
    a, b, c, d = get_school_info(school, id)

    locations_list.append(a)
    courses_list.append(b)
    badges_list.append(c)
    school_list.append(d)

# could you write this as a list comprehension? ;)
# YES WE CAN!
comments_list = [get_comments_school(s) for s in school_dict.keys()]

comments = pd.concat(comments_list)
locations = pd.concat(locations_list)
courses = pd.concat(courses_list)
badges = pd.concat(badges_list)
school = pd.concat(school_list)

# Call function to populate tables in datalake database
create_datalake()
print("Datalake created! Time to clean it (:")
#######################################################################################################################
