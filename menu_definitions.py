from Menu import Menu
from Option import Option


menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add new object", "add()"),
    Option("Delete existing object", "delete()"),
    Option("List existing object", "list_members()"),
    Option("Select existing object", "select()"),
    Option("Exit", "pass")
])


add_select = Menu('add select', 'Which type of object do you want to add?:', [
    Option("Department", "add_department()"),
    Option("Course", "add_course()"),
    Option("Section", "add_section()"),
    Option("Student", "add_student()"),
    Option("Major", "add_major()"),
    Option("Student Major", "add_student_major()"),
    Option("Enrollment", "add_enrollment()"),
    Option("Exit", "pass")
])


list_menu = Menu('list', 'Please indicate what object you want to list:', [
    Option("Department", "list_department(db)"),
    Option("Course", "list_course(db)"),
    Option("Major", "list_major(db)"),
    Option("Student", "list_student(db)"),
    Option("Student to Major", "list_student_major(db)"),
    Option("Major to Student", "list_major_student(db)"),
    Option("Exit", "pass")
])


delete_select = Menu('delete select', 'Which type of object do you want to delete?:', [
    Option("Department", "delete_department()"),
    Option("Course", "delete_course()"),
    Option("Major", "delete_major()"),
    Option("Student", "delete_student()"),
    Option("Section", "delete_section()"),
    Option("Enrollment", "delete_enrollment()"),
    Option("Major from Student", "delete_student_major()"),
    Option("Exit", "pass")
])

list_select = Menu('list select', 'Which type of object do you want to list?:', [
    Option("Department", "list_department()"),
    Option("Course", "list_course()"),
    Option("Section", "list_section()"),
    Option("Student", "list_student()"),
    Option("Major", "list_major()"),
    Option("Student Major", "list_student_major()"),
    Option("Enrollment", "list_enrollment()"),
    Option("Exit", "pass")
])


select_select = Menu('select select', 'Which type of object do you want to select:', [
    Option("Department", "print(select_general(Department))"),
    Option("Course", "print(select_general(Course))"),
    Option("Section", "print(select_general(Section))"),
    Option("Student", "print(select_general(Student))"),
    Option("Major", "print(select_general(Major))"),
    Option("Student Major", "print(select_general(StudentMajor))"),
    Option("Enrollment", "print(select_general(Enrollment))"),
    Option("Exit", "pass")
])
