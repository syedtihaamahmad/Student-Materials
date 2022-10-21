import pytest
import System
import Staff
import Professor
import Student
import json

username = 'akend3'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'databases'
assignment = 'assignment1'
assignment_name='assignment1'
profUser = 'goggins'
profPass = 'augurrox'
due_date= '2/5/20'
submission_date= "2/5/20"
submission = "Blah Blah Blah"
grade=99

with open('./Data/users.json') as f:
    users = json.load(f)

with open('./Data/courses.json') as f2:
    courses = json.load(f2)

#Tests if the program can handle a wrong username


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


def test_login(grading_system):
	grading_system.login(username,password)
	with open('./Data/users.json') as f:
		data = json.load(f)

	if username not in data:
		assert False

def test_check_password(grading_system):
    test = grading_system.check_password('calyam',password)
    test2 = grading_system.check_password('calyam','#yeet')
    test3 = grading_system.check_password('calyam','#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False





def test_change_grade():
    staff_user= Staff.Staff()
    staff_user.change_grade(username,course,assignment,grade)

    with open('Data/users.json') as f:
        data = json.load(f)
        #self.users[user]['courses'][course][assignment]['grade'] = 0
        grade2 = data[username]['courses'][course][assignment][grade]
    if grade == grade2:
        assert True
    else:
        assert False    
    

def test_create_assignment():
    staff_user= Staff.Staff()
    staff_user.create_assignment(assignment,due_date,course)
    with open('Data/courses.json') as f:
        data = json.load(f)
    if assignment in data:
        assert True
    else:
        assert False    


def test_add_student():
    prof_user= Professor.Professor(profUser,users,courses)
    prof_user.add_student(username,course)
    with open('./Data/users.json') as f:
    	userss = json.load(f)
    
    if username in userss:
        assert True    
    else:
        assert False  



def test_drop_student():

    prof_user= Professor.Professor(profUser,users,courses)
    prof_user.drop_student(username,course)

    with open('./Data/users.json') as f:
        userss = json.load(f)
    
    if username in userss:
        assert True    
    else:
        assert False  



def test_submit_assignment():
    student_user= Student.Student(username,users,courses)
    student_user.submit_assignment(course,assignment,submission,submission_date)
    with open('Data/courses.json') as f:
        coursess = json.load(f)
    
    if coursess[course]['assignments'][assignment][submission_date]:
        assert True
    else:
        assert False  

def test_check_ontime():
    student_user= Student.Student(username,users,courses)
    if student_user.check_ontime(submission_date,due_date):
    	assert True
    else:
    	assert False


def test_check_grades():
	#check if grades returned are same as in database
    student_user= Student.Student(username,users,courses)
    gradess= student_user.check_grades(course)
    with open('Data/users.json') as f:
        userss = json.load(f)
    assignments = userss[username]['courses'][course]
    grades = []
    for key in assignments:
        grades.append([key, assignments[key]['grade']])    
    if gradess==grades:
        assert True
    else:
        assert False 



def test_view_assignments():
	#check if assignment can be viewed 
    student_user= Student.Student(username,users,courses)
    assigns= student_user.view_assignments(course)

    with open('Data/courses.json') as f:
        coursess = json.load(f)
    coursesss = coursess[course]['assignments']
    assignments = []
    for key in coursesss:
        assignments.append([key,coursesss[key]['due_date']])
    
    if assignments:
        assert True
    else:
        assert False   



def test_check_ontime_typo():
	#check ontime submission of student not in class
    student_user= Student.Student("sdasd",users,courses)
    if student_user.check_ontime(submission_date,due_date):
    	assert True
    else:
    	assert False

def test_verify_assignments():
	#check if assignment viewed are same as stored in database
    student_user= Student.Student(username,users,courses)
    assigns= student_user.view_assignments(course)

    with open('Data/courses.json') as f:
        coursess = json.load(f)
    coursesss = coursess[course]['assignments']
    assignments = []
    for key in coursesss:
        assignments.append([key,coursesss[key]['due_date']])
    
    if assigns == assignments:
        assert True
    else:
        assert False   



def test_view_grades():
	#check if grades can be viewed
    student_user= Student.Student(username,users,courses)
    gradess= student_user.check_grades(course)
    if gradess:
        assert True
    else:
        assert False 

def test_check_password_student(grading_system):
	#check student password
    test = grading_system.check_password(username,password)
    if not test:
        assert False



def test_drop_student_typo():
	#check dropping student who doesnot exist
    prof_user= Professor.Professor(profUser,users,courses)
    prof_user.drop_student(profUser,course)

    with open('./Data/users.json') as f:
        userss = json.load(f)
    
    if username in userss:
        assert True    
    else:
        assert False  