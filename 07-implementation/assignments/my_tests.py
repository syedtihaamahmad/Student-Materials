import pytest
import System
import Staff
import Professor
import Student
import json

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
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

def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False




def test_change_grade():
    staff_user= Staff.Staff()
    staff_user.change_grade(username,course,assignment,grade)
    

def test_create_assignment():
    staff_user= Staff.Staff()
    staff_user.create_assignment(assignment,due_date,course)


def test_add_student():
    prof_user= Professor.Professor(profUser,users,courses)
    prof_user.add_student(username,course)



def test_drop_student():
    prof_user= Professor.Professor(profUser,users,courses)
    prof_user.drop_student(username,course)




def test_submit_assignment():
    student_user= Student.Student(username,users,courses)
    student_user.submit_assignment(course,assignment,submission,submission_date)

def test_check_ontime():
    student_user= Student.Student(username,users,courses)
    student_user.check_ontime(submission_date,due_date)


def test_check_grades():
    student_user= Student.Student(username,users,courses)
    student_user.check_grades(course)

def test_view_assignments():
    student_user= Student.Student(username,users,courses)
    student_user.view_assignments(course)