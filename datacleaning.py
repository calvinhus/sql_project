
def program_clean(row):
    """This method normalizes every row of the cohort name"""
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
        return '9 weeks'
    elif row['program'] == 'Cyber Security Bootcamp':
        return '12 weeks'
    elif row['program'] == 'Data Analytics Bootcamp':
        return '9 weeks'
    elif row['program'] == 'Web Development Bootcamp':
        return '9 weeks'
    elif row['program'] == 'UX/UI Design Part-Time':
        return '24 weeks'
    elif row['program'] == 'Cyber Security Part-Time':
        return '-'
    elif row['program'] == 'Data Analytics Part-Time':
        return '24 weeks'
    elif row['program'] == 'Web Development Part-Time':
        return '24 weeks'
    else:
        return 'check duration'


def jobTitle_DA_clean(row):
    """This method normalizes the job title for Data Analytics cohort"""
    jobTitle_DA = ['Data', 'dados', 'analyst',
                   'Software', 'Manager', 'Junior', 'Innovation']
    for element in jobTitle_DA:
        if element in row:
            return 1
        else:
            return 0


def jobTitle_UXUI_clean(row):
    """This method normalizes the job title for UX/UI cohort"""
    jobTitle_UXUI = ['Student', 'student', 'Unemployed', 'Leemur', 'Owner']
    for element in jobTitle_UXUI:
        if element in row:
            return 0
        else:
            return 1


def jobTitle_WD_clean(row):
    """This method normalizes the job title for WebDev cohort"""
    jobTitle_WD = ['Senior Associate', 'unemployed', 'Botcave', 'Finance Analyst', 'Program Manager', 'Estudiante', 'Therapist', 'Student', 'student',
                   'Partner @Orion', 'Founder', 'Student', 'COO at Tender.co', 'Entrepreneur']

    for element in jobTitle_WD:
        if element in row:
            return 0
        else:
            return 1


def jobTitle_CS_clean(row):
    """This method normalizes the job title for CyberSec cohort"""
    jobTitle_CS = ['analyst']
    for element in jobTitle_CS:
        if (element in row):
            return 1
        else:
            return 0
