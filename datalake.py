import requests
from pandas.io.json import json_normalize
import pandas as pd
import re
schools = {
    'ironhack': 10828,
    'app-academy': 10525,
    'springboard': 11035
}


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


# could you write this as a list comprehension? ;)
comments = []

for school in schools.keys():
    print(school)
    comments.append(get_comments_school(school))

comments = pd.concat(comments)


def get_school_info(school, school_id):
    url = 'https://www.switchup.org/chimera/v1/bootcamp-data?mainTemplate=bootcamp-data%2Fdescription&path=%2Fbootcamps%2F' + \
        str(school) + '&isDataTarget=false&bootcampId=' + str(school_id) + \
        '&logoTag=logo&truncationLength=250&readMoreOmission=...&readMoreText=Read%20More&readLessText=Read%20Less'

    data = requests.get(url).json()

    data.keys()

    courses = data['content']['courses']
    courses_df = pd.DataFrame(courses, columns=['courses'])

    locations = data['content']['locations']
    locations_df = json_normalize(locations)

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


locations_list = []
courses_list = []
badges_list = []
schools_list = []

for school, id in schools.items():
    print(school)
    a, b, c, d = get_school_info(school, id)

    locations_list.append(a)
    courses_list.append(b)
    badges_list.append(c)
    schools_list.append(d)

locations = pd.concat(locations_list)
courses = pd.concat(courses_list)
badges = pd.concat(badges_list)
schools = pd.concat(schools_list)
