#this program works for a student. It takes the student's score, unit and grade for a semester,
#assigns the grade and computes the semester GPA.
import time
#lists to store user input
name = []
registration_no = []
course = []
unit = []
score = []
point = []
grade = []
total_point = []
total_load_points = []
semester_GPA = []
class_of_degree = []
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
#take student's name, registration number and store in a list
student_name = input('Enter your name: ')
if student_name == '':
    print('You must enter your name to continue. Try again.')
    exit()
name.append(student_name.upper())
reg_no = input('Enter your registration number: ')
if reg_no == '':
    print('You must enter your registration number to continue. Try again.')
    exit()
registration_no.append(reg_no.upper())
#take the number of courses taken in a semester by the student
no_of_course = input('Please enter the number of courses taken this semester: ')
while no_of_course.isnumeric() == False:
    print('Please enter a number!')
    no_of_course = input('Please enter the number of courses taken this semester: ')
no_of_course = int(no_of_course)
#take the code, unit and score for each course taken by the student
while True:
    #stop accepting input after student enters the last course for the semester
    if len(course) == no_of_course:
        break
    #course_code = input('Enter the code of course ' + str(len(course) + 1) + ', or enter nothing to stop: ')
    course_code = input('Enter the code for ' + ordinal((len(course) + 1)) + ' course, or enter nothing to stop: ')
    if course_code == '':
        print('Operation aborted')
        exit()
    course.append(course_code.upper())
    #course_unit = int(input('Enter the unit for course ' + str(len(unit) + 1) + ', or enter nothing to stop: '))
    course_unit = int(input('Enter the unit for ' + course_code + ', or enter nothing to stop: '))
    if course_unit == '':
        print('Operation aborted')
        exit()
    unit.append(course_unit)
    #student_score = int(input('Enter your score for course ' + str(len(score) + 1) + ', or enter nothing to stop: '))
    student_score = int(input('Enter your score for ' + course_code + ', or enter nothing to stop: '))
    if student_score == '':
        print('Operation aborted')
        exit()
    while student_score > 100:
        print('You can\'t score more than 100 in a course. Try again & enter your score correctly.') 
        student_score = int(input('Enter your score for ' + course_code + ', or enter nothing to stop: '))
    score.append(student_score)
    #assign grade and total point earned to each score
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
print('Computing semster grade...')
time.sleep(3)
#calculate the semester GPA
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
print('...............................................')
for student_name, reg_no in zip(name, registration_no):
    print(f'STUDENT NAME: {student_name}, REGISTRATION NO: {reg_no}')

print('COURSE' + '\t' + 'UNIT' + '\t' + 'SCORE' + '\t' + 'GRADE' + '\t' + 'POINT')

for course, unit, score, grade, point in zip(course, unit, score, grade, point):
    print(course, unit, score, grade, point, sep='\t ')

print('Total unit: ', total_unit)
print('Total point: ', total_points)
print('Semester GPA: ', present_gpa)
print('Class of Degree: ', degree_class)
print('...............................................')
print ('END OF SEMESTER REPORT')

