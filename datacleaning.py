#Função para limpar os nomes dos programas

def program_clean(row):
    if (row['program']=='Full-time UX/UI Design Bootcamp')|(row['program']=='Web Design'):
        return 'UX/UI Design Bootcamp'
    elif (row['program']=='Part-time UX/UI Design')|(row['program']=='Part-time UX/UI Design '):
        return 'UX/UI Design Part-Time'
    elif (row['program']=='Full-time Web Development Bootcamp')|(row['program']=='Full-time Web Development Bootcamp '):
        return 'Web Development Bootcamp'
    elif (row['program']=='Part-time Web Development'):
        return 'Web Development Part-Time'
    elif (row['program']==''):
        return None
    else:
        return row['program']


comments2['program']=comments2.apply(program_clean, axis=1)

#Função para inserir o preço de acordo com cada curso

def price_program(row):
    if row['program'] == 'UX/UI Design Bootcamp':
        return 6.000
    elif row['program'] == 'Cyber Security Bootcamp':
        return 7.500
    elif row['program'] == 'Data Analytics Bootcamp':
        return 6.000
    elif row['program'] == 'Web Development Bootcamp':
        return 6.000
    elif row['program'] == 'UX/UI Design Part-Time':
        return 7.500
    elif row['program'] == 'Cyber Security Part-Time':
        return 7.500
    elif row['program'] == 'Data Analytics Part-Time':
        return 6.500
    elif row['program'] == 'Web Development Part-Time':
        return 7.500
    else:
        return 'check price'


comments2['price']=comments2.apply(price_program, axis=1)

#Função para inserir a duração

def duration_program(row):
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


comments2['duration']=comments2.apply(price_program, axis=1)


#Função para limpar o jobTitle

#DA
jobTitle_DA =['Data', 'dados', 'analyst', 'Software', 'Manager', 'Junior', 'Innovation']
def jobTitle_DA_clean(row):
    for element in jobTitle_DA:
        if element in row:
            return 1
        else:
            return 0

comments2['Work_inField']=comments2['jobTitle'].apply(jobTitle_DA_clean)

#UXUI
jobTitle_UXUI =['Student', 'student', 'Unemployed', 'Leemur', 'Owner']
def jobTitle_UXUI_clean(row):
    for element in jobTitle_UXUI:
        if element in row:
            return 0
        else:
            return 1

comments2['Work_inField']=comments2['jobTitle'].apply(jobTitle_UXUI_clean)

#WEBDEV

jobTitle_WD =['Senior Associate', 'unemployed', 'Botcave', 'Finance Analyst', 'Program Manager', 'Estudiante', 'Therapist', 'Student', 'student',
'Partner @Orion', 'Founder', 'Student', 'COO at Tender.co', 'Entrepreneur']
def jobTitle_WD_clean(row):
    for element in jobTitle_WD:
        if element in row:
            return 0
        else:
            return 1

comments2['Work_inField']=comments2['jobTitle'].apply(jobTitle_WD_clean)


#nivel satisfacao curriculum
#perfil das pessoas que fazem mais reviews (nivel de review/curso)
#


#CYBERSEC

def jobTitle_CS_clean(row):
    jobTitle_CS =['analyst']
    for element in jobTitle_CS:
        if (element in row):
            return 1
        else:
            return 0

comments2['Work_inField']=comments2['jobTitle'].apply(jobTitle_CS_clean)


