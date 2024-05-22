from ConstraintUtilities import select_general, unique_general, prompt_for_date
from Utilities import Utilities
from Menu import Menu
from menu_definitions import menu_main, add_select, list_select, select_select, delete_select
from Department import Department
from StudentMajors import StudentMajor
from LetterGrades import LetterGrade
from datetime import datetime
from Course import Course
from Sections import Section
from Students import Student
from Majors import Major
from Enrollment import Enrollment
from PassFails import PassFail


def menu_loop(menu: Menu):
    action: str = ''
    while action != menu.last_action():
        action = menu.menu_prompt()
        print('next action: ', action)
        exec(action)


def add():
    menu_loop(add_select)


def list_members():
    menu_loop(list_select)


def select():
    menu_loop(select_select)


def delete():
    menu_loop(delete_select)


def add_department():
    success: bool = False
    while not success:
        try:
            new_department = Department(
                                input('Name --> '),
                                input('Abbreviation --> '),
                                input('Chair name --> '),
                                input('building (ANAC, CDC, DC, ECS, EN2, EN3, EN4, EN5, ET, HSCI, NUR, VEC)--> '),
                                str(input('office --> ')),
                                input('Description --> '))
            violated_constraints = unique_general(new_department)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_department.save()
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            print(e)
            print("Try again.")


def add_course():
    success: bool = False
    while not success:
        try:
            new_course = Course(
                select_general(Department),
                int(input('Course number --> ')),
                input('Course name --> '),
                input('Description --> '),
                int(input('units --> ')))
            violated_constraints = unique_general(new_course)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_course.save()
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            print(e)
            print("Try again.")


def add_section():
    success: bool = False
    while not success:
        try:
            hour = int(input('Starting time hour --> '))
            minute = int(input('Starting time minute --> '))
            startTime = datetime(1, 1, 1, hour, minute, 0)
            new_section = Section(
                select_general(Course),
                int(input('Section number --> ')),
                input('Semester (Fall, Spring, Summer I, Summer II, Summer III, Winter)--> '),
                int(input('Year --> ')),
                input('Building (ANAC, CDC, DC, ECS, EN2, EN3, EN4, EN5, ET, HSCI, NUR, VEC)--> '),
                int(input('Room --> ')),
                input('Schedule (MW, TuTh, MWF, F, S)--> '),
                startTime,
                input('Instructor --> ')
            )
            violated_constraints = unique_general(new_section)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_section.save()
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            print(e)
            print("Try again.")


def add_student():
    success: bool = False
    while not success:
        try:
            new_student = Student(
                input('Last name --> '),
                input('First name --> '),
                input('Email --> '))
            violated_constraints = unique_general(new_student)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_student.save()
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            print(e)
            print("Try again.")


def add_major():
    success: bool = False
    while not success:
        try:
            new_major = Major(
                select_general(Department),
                input('Name --> '),
                input('Description --> '))
            violated_constraints = unique_general(new_major)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_major.save()
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            print(e)
            print("Try again.")


def add_student_major():
    success: bool = False
    while not success:
        try:
            new_student_major = StudentMajor(
                select_general(Student),
                select_general(Major),
                prompt_for_date('Enter date of registration:'), )
            violated_constraints = unique_general(new_student_major)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_student_major.save()
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            print(e)
            print("Try again.")


def add_enrollment():
    success: bool = False
    while not success:
        try:
            new_enrollment = Enrollment(
                                select_general(Section),
                                select_general(Student))
            violated_constraints = unique_general(new_enrollment)
            if len(violated_constraints) > 0:
                for violated_constraint in violated_constraints:
                    print('Your input violates constraint: ', violated_constraint)
                print('try again')
            else:
                try:
                    success = True
                    new_enrollment.save()
                    while True:
                        choice = int(input('What kind of enrollment is this?\n1.PassFail\n2.LetterGrade\n--> '))
                        if choice == 1:
                            new_pass_fail = PassFail(
                                                new_enrollment,
                                                prompt_for_date('Date of application'))
                            violated_constraints = unique_general(new_pass_fail)
                            if len(violated_constraints) > 0:
                                for violated_constraint in violated_constraints:
                                    print('Your input violates constraint: ', violated_constraint)
                                print('try again')
                            else:
                                try:
                                    new_pass_fail.save()
                                    break
                                except Exception as e:
                                    print(e)
                                    print("Try again.")
                        elif choice == 2:
                            new_letter_grade = LetterGrade(
                                                new_enrollment,
                                                input('Minimum Satisfactory grade (A, B, C)--> '))
                            violated_constraints = unique_general(new_letter_grade)
                            if len(violated_constraints) > 0:
                                for violated_constraint in violated_constraints:
                                    print('Your input violates constraint: ', violated_constraint)
                                print('try again')
                            else:
                                try:
                                    new_letter_grade.save()
                                    break
                                except Exception as e:
                                    print(e)
                                    print("Try again.")
                        else:
                            print('Not a valid option.')
                except Exception as e:
                    success = False
                    print(e)
                    print("Try again.")
        except Exception as e:
            success = False
            print(e)
            print("Try again.")


def delete_department():
    department = select_general(Department)
    try:
        department.delete()
    except Exception as e:
        print(e)


def delete_course():
    course = select_general(Course)
    try:
        course.delete()
    except Exception as e:
        print(e)


def delete_section():
    section = select_general(Section)
    try:
        section.delete()
    except Exception as e:
        print(e)


def delete_student():
    student = select_general(Student)
    try:
        student.delete()
    except Exception as e:
        print(e)


def delete_major():
    major = select_general(Major)
    try:
        major.delete()
    except Exception as e:
        print(e)


def delete_student_major():
    studentMajor = select_general(StudentMajor)
    try:
        studentMajor.delete()
    except Exception as e:
        print(e)


def delete_enrollment():
    enrollment = select_general(Enrollment)
    try:
        enrollment.delete()
    except Exception as e:
        print(e)


def list_department():
    for x in db.departments.find():
        print(x)


def list_course():
    for x in db.courses.find():
        print(x)


def list_section():
    for x in db.sections.find():
        print(x)


def list_student():
    for x in db.students.find():
        print(x)


def list_major():
    for x in db.majors.find():
        print(x)


def list_student_major():
    for x in db.student_majors.find():
        print(x)


def list_enrollment():
    for x in db.enrollments.find():
        print(x)


if __name__ == '__main__':
    db = Utilities.startup()
    main_action: str = ''
    while main_action != menu_main.last_action():
        main_action = menu_main.menu_prompt()
        print('next action: ', main_action)
        exec(main_action)


