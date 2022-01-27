
def program_clean(row):
    """This method normalizes every row of the cohort name."""
    if (row['program'] == 'Full-time UX/UI Design Bootcamp') | (row['program'] == 'Web Design'):
        return 'UX/UI Design Bootcamp'
    elif (row['program'] == 'Part-time UX/UI Design') | (row['program'] == 'Part-time UX/UI Design '):
        return 'UX/UI Design Part-Time'
    elif (row['program'] == 'Full-time Web Development Bootcamp') | (row['program'] == 'Full-time Web Development Bootcamp '):
        return 'Web Development Bootcamp'
    elif (row['program'] == 'Part-time Web Development'):
        return 'Web Development Part-Time'
    elif (row['program'] == ''):
        return None
    else:
        return row['program']


def price_program(row):
    """This method sets the correct price of every cohort"""
    if row['program'] == 'UX/UI Design Bootcamp':
        return 6000
    elif row['program'] == 'Cyber Security Bootcamp':
        return 7500
    elif row['program'] == 'Data Analytics Bootcamp':
        return 6000
    elif row['program'] == 'Web Development Bootcamp':
        return 6000
    elif row['program'] == 'UX/UI Design Part-Time':
        return 7500
    elif row['program'] == 'Cyber Security Part-Time':
        return 7500
    elif row['program'] == 'Data Analytics Part-Time':
        return 6500
    elif row['program'] == 'Web Development Part-Time':
        return 7500
    else:
        return 'check price'


def duration_program(row):
    """This method sets the correct duration of every cohort"""
    if row['program'] == 'UX/UI Design Bootcamp':
        return '9 months'
    elif row['program'] == 'Cyber Security Bootcamp':
        return '12 months'
    elif row['program'] == 'Data Analytics Bootcamp':
        return '9 months'
    elif row['program'] == 'Web Development Bootcamp':
        return '9 months'
    elif row['program'] == 'UX/UI Design Part-Time':
        return '24 months'
    elif row['program'] == 'Cyber Security Part-Time':
        return '-'
    elif row['program'] == 'Data Analytics Part-Time':
        return '24 months'
    elif row['program'] == 'Web Development Part-Time':
        return '24 months'
    else:
        return 'check duration'


def jobTitle_DA_clean(row):
    """This method normalizes the job title for Data Analytics"""
    jobTitle_DA = ['Data', 'dados', 'analyst',
                   'Software', 'Manager', 'Junior', 'Innovation']
    for element in jobTitle_DA:
        if element in row:
            return 1
        else:
            return 0


def jobTitle_UXUI_clean(row):
    """This method normalizes the job title for UX/UI"""
    jobTitle_UXUI = ['Student', 'student', 'Unemployed', 'Leemur', 'Owner']
    for element in jobTitle_UXUI:
        if element in row:
            return 0
        else:
            return 1

# WEBDEV

# web ft 6000

# nivel satisfacao curriculum
# perfil das pessoas que fazem mais reviews (nivel de review/curso)
#


# CYBERSEC

#calendar=['janeiro', 'fevereiro', "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# def month(row):
#    for element in calendar:
#        if element in row:
#            return calendar.index(element)+1

#df1["Month"] = df1["DIM CALENDAR.DATE.1"].apply(month)


# comments2[(comments2['school']=='ironhack')&((comments2['program']=='UX/UI Design Bootcamp')|(comments2['program']=='UX/UI Design Part-Time')))]['jobTitle'].unique()
