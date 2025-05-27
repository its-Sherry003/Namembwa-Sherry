from multipledispatch import dispatch
class Person:
    def __init__(self, name):
        self.name = name
    
    
@dispatch(str)
def enroll(course):
    print(f"Enrolled in course {course}")

@dispatch(str, int)
def enroll(course,semester):
    print(f"Enrolled in course {course} for semester {semester}")

@dispatch(str, str)
def enroll(course1,course2):
    print(f"Enrolled in courses: {course1}, {course2}")

@dispatch(str, str, int)
def enroll(course1,course2,semester):
    print(f"Enrolled in courses: {course1}, {course2} for semester {semester}")

class Student(Person):
    def prompt(self):
        print('"Maximum number of courses to enroll for is 2"')
        course1 = input("Enter first course: \n")
        course2 = input("Enter second course(leave blank if none): \n")
        semester = input("Enter semester(leave blank if unknown): \n")
    
        if course1 and course2:
            enroll(course1,course2)
        elif course1 and course2 and semester:
            enroll(course1,course2,int(semester))
        elif course1 and semester:
            enroll(course1,int(semester))
        else:
            enroll(course1)
        
        
class Lecturer(Person):
    def prompt(self):
        student = input("Student name: \n")
        course = input("Course to grade: \n")
        grade = input("Grade: \n")
        print(f"Grade {grade} for {course} has been assigned to {student}")
        
        
while True:
    print("\n----------OPTIONS----------")
    print("1. Student")
    print("2. Lecturer")
    print("3. Exit")
    print("---------------------------\n")

    choice = input("\nType your option(1/2/3)\n").strip()
    
    if choice == "1":
        name = input("Enter your name: \n")
        s = Student(name)
        s.prompt()
    elif choice == "2":
        name = input("Enter your name: \n")
        lecturer = Lecturer(name)
        lecturer.prompt()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Select from the menu options")