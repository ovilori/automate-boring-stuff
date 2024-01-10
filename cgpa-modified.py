import sys
import pyodbc

""" #connect to the Database storing student's grades
server = 'localhost\sqlexpress' 
database = 'PythonDB' 
username = 'sa' 
password = '' 
try:
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
        ';DATABASE='+database+
        ';UID='+username+
        ';PWD='+ password,
        autocommit=True)
    print('Connection to MSSQL DB successful!')
except pyodbc.OperationalError as e:
    print(f"The error '{e}' occurred")
cursor = cnxn.cursor() """
sn = 0
name = []
registration_no = []
course = []
unit = []
score = []
point = []
grade = []
report = []
total_point = []
total_load_points = []
semester_GPA = []
class_of_degree = []
#take student name and registration number
student_name = input('Enter your name: ')
#if student_name == '':
    #break
name.append(student_name.upper())
#cursor.execute('''INSERT INTO Result(STUDENT_NAME) VALUES(?)''',(student_name))
reg_no = input('Enter your registration number: ')
#if reg_no == '':
    #break
registration_no.append(reg_no.upper())
#cursor.execute('''INSERT INTO Result(REGISTRATION_NO) VALUES(?)''',(reg_no))
while True:
    student_course = input('Enter the name of course ' + str(len(course) + 1) + ', or enter nothing to stop: ')
    if student_course == '':
        break
    #course = course + [student_course]
    course.append(student_course.upper())
    course_unit = int(input('Enter the unit for course ' + str(len(unit) + 1) + ', or enter nothing to stop: '))
    if course_unit == '':
        break
    #unit = unit + [course_unit]
    #course_unit = int(course_unit)
    unit.append(course_unit)
    student_score = int(input('Enter your score for course ' + str(len(score) + 1) + ', or enter nothing to stop: '))
    if student_score == '':
        break
    #score = score + [student_score]
    #student_score = int(student_score)
    score.append(student_score)
    #assign grades to each course
    if int(student_score) in range(70,101):
        point.append(5)
        grade.append('A')
        total_point.append(5 * course_unit)
    elif int(student_score) in range(60,70):
        point.append(4)
        grade.append('B')
        total_point.append(4 * course_unit)
    elif int(student_score) in range(50,60):
        point.append(3)
        grade.append('C')
        total_point.append(3 * course_unit)
    elif int(student_score) in range(40, 50):
        point.append(2)
        grade.append('D')
        total_point.append(2 * course_unit)
    elif int(student_score) in range(30, 40):
        point.append(1)
        grade.append('E')
        total_point.append(1 * course_unit)
    elif int(student_score) in range (1, 30) or int(student_score) == 0:
        point.append(0)
        grade.append('F')
        total_point.append(0 * course_unit)
    else:
        print('You can\'t score more than 100 in a course. Try again & enter your score correctly.') 
        sys.exit()

#calculate the semester point
#sum of all units 
total_unit = sum(unit)
#total load point value (i.e sum of unit * points)
total_points = sum(total_point)
total_load_points.append(total_points)
#semster GPA calculation (i.e total_points/total_unit) to 2 dp
present_gpa = round((total_points/total_unit),2)
present_gpa = float(present_gpa)
semester_GPA.append(present_gpa)

#decide the class of degree
if present_gpa == 4.50 and present_gpa <= 5.00:
    degree_class = 'First Class'
    class_of_degree.append(degree_class)
elif present_gpa >= 3.50 and present_gpa <= 4.49:
    degree_class = 'Second Class Upper'
    class_of_degree.append(degree_class)
elif present_gpa >= 2.40 and present_gpa <= 3.49:
    degree_class = 'Second Class Lower'
    class_of_degree.append(degree_class)
elif present_gpa >= 1.50 and present_gpa <= 2.39:
    degree_class = 'Third Class'
    class_of_degree.append(degree_class)
else:
    degree_class = 'Pass'
    class_of_degree.append(degree_class)

#print the details of the semester report
print ('SEMESTER REPORT')
for student_name, reg_no in zip(name, registration_no):
    print(f'STUDENT NAME: {student_name}, REGISTRATION NO: {reg_no}')

print('COURSE' + '\t' + 'UNIT' + '\t' + 'SCORE' + '\t' + 'GRADE' + '\t' + 'POINT')

for course, unit, score, grade, point in zip(course, unit, score, grade, point):
    print(course, unit, score, grade, point, sep='\t ')

print('Total unit: ', total_unit)
print('Total point: ', total_points)
print('Semester GPA: ', present_gpa)
print('Class of Degree: ', degree_class)

print ('END OF SEMESTER REPORT')

#store the student record in the database

""" #connect to the Database storing student's grades
server = 'localhost\sqlexpress' 
database = 'PythonDB' 
username = 'sa' 
password = 'xxxxxxxxxxxxxxxxxxxxx' 
try:
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
        ';DATABASE='+database+
        ';UID='+username+
        ';PWD='+ password,
        autocommit=True)
    print('Connection to MSSQL DB successful!')
except pyodbc.OperationalError as e:
    print(f"The error '{e}' occurred")
cursor = cnxn.cursor()
add_record = '''INSERT INTO Result(SN, STUDENT_NAME,\
                    REGISTRATION_NO, COURSE,\
                    UNIT, SCORE,\
                    POINT, GRADE,\
                    TOTAL_UNITS, TOTAL_LOAD_POINTS,\
                    SEMESTER_GPA, CLASS_OF_DEGREE)\
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
        
values = sn + 1, name, registration_no, course, unit, score,\
            point, grade, total_unit, total_points, semester_GPA, class_of_degree
try:
    cursor.execute(add_record, values)           
    print(cursor.rowcount, 'record added successfully')
except pyodbc.ProgrammingError as e:
    print('Unable to add record to database.')
    print(f"The error '{e}' occured")
 """
