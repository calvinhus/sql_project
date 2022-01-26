import requests
import pandas as pd
import re

school = 'ironhack'


def remove_tags(x):
    return TAG_RE.sub('', x)


TAG_RE = re.compile(r'<[^>]+>')
# defines url to make api call to data -> dynamic with school if you want to scrape competition
url = "https://www.switchup.org/chimera/v1/school-review-list?mainTemplate=school-review-list&path=%2Fbootcamps%2F" + \
    school + "&isDataTarget=false&page=3&perPage=10000&simpleHtml=true&truncationLength=250"
# makes get request and converts answer to json
# url defines the page of all the information, request is made, and information is returned to data variable
data = requests.get(url).json()
print(data)
# converts json to dataframe
#reviews = pd.DataFrame(data['content']['reviews'])

# aux function to apply regex and remove tags

#reviews['review_body'] = reviews['body'].apply(remove_tags)
#reviews['school'] = school


# for i in range(0, 20):
#    print(reviews['review_body'][i])
