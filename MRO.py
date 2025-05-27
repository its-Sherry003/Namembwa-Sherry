#Method Resolution Order

from multipledispatch import dispatch
class University:
    def prompt(self):
        print("Prompt from University.")
        

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

class Person:
    def __init__(self, name):
        self.name = name
    
    def prompt(self):
        print(f"Prompt from Person: Hello {self.name}, please enter your details.")
        course1 = input("First course: \n")
        course2 = input("Second course(leave blank if none): \n")
        semester = input("Semester(leave blank if unknown): \n")
    
        if course1 and course2:
            enroll(course1,course2)
        elif course1 and course2 and semester:
            enroll(course1,course2,int(semester))
        elif course1 and semester:
            enroll(course1,int(semester))
        else:
            enroll(course1)

class Student(Person, University):
    def __init__(self, name):
        super().__init__(name)
        
name = input("Enter name: \n")

s = Student(name)
s.prompt()

print(Student.__mro__)