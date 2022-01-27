# -- Qual formato (FT/PT) os alunos melhor avaliam?

part_time_score = """SELECT program , AVG(overallScore)
FROM comments
WHERE program LIKE '%Part-Time%'
GROUP BY `program`;"""


full_time_score = """SELECT program , AVG(overallScore)
FROM comments
WHERE program LIKE '%bootcamp%'
GROUP BY `program`;"""

# Q3 - Overallscore ao longo do tempo (verificar esperialmente o curriculum e o jobsupport)
curriculum_time = """select AVG(curriculum), graduatingYear, count(curriculum)
from comments
group by graduatingYear
order by graduatingYear asc;"""

job_support_time = """select AVG(jobSupport), graduatingYear, count(jobSupport)
from comments
group by graduatingYear
order by graduatingYear asc;"""

overall_score_time = """select AVG(overallScore), graduatingYear, count(overallScore)
from comments
group by graduatingYear
order by graduatingYear asc;"""

# Q4 - Qual o perfil das pessoas que mais avaliam?
profile_by_program = """SELECT program, COUNT(review_body)
FROM comments
GROUP BY program;"""

profile_by_alumni = """SELECT isAlumni, COUNT(review_body)
FROM comments
GROUP BY isAlumni;"""

profile_by_workInField = """SELECT Work_inField, isAlumni, COUNT(review_body)
FROM comments
GROUP BY Work_inField, isAlumni;"""

# Q5 - Como os estudantes que trabalham na área avaliam a Ironhack para melhorar a carreira?
overall_student_rate = """SELECT AVG(overallscore), COUNT(overallScore)
FROM (SELECT * FROM comments
WHERE Work_inField = 1
AND isAlumni = 0) sub_1
GROUP BY school
ORDER BY AVG(overallScore) ASC;"""

curriculum_student_rate = """SELECT AVG(curriculum), COUNT(curriculum)
FROM (SELECT * FROM comments
WHERE Work_inField = 1
AND isAlumni = 0) sub_2
GROUP BY school
ORDER BY AVG(curriculum) ASC;"""

jobSupport_student_rate = """SELECT AVG(jobSupport), COUNT(jobSupport)
FROM (SELECT * FROM comments
WHERE Work_inField = 1
AND isAlumni = 0) sub_3
GROUP BY school
ORDER BY AVG(jobSupport) ASC;"""
