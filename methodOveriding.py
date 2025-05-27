from multipledispatch import dispatch
class Person:
    def __init__(self, name):
        self.name = name
        
    def prompt(self):
        print(f"{self.name}, this is the General prompt to access system.")
    

class Student(Person):
    def prompt(self):
        print(f"{self.name}, this is the Student prompt to access system.")
        course = input("Enter course name: ")
        print(f"\n{self.name} enrolled in {course}\n")

        
class Lecturer(Person):
    def prompt(self):
        print(f"{self.name}, this is the Lecturer prompt to access system.")
        student = input("Enter Student name: \n")
        course = input("Enter course name: \n")
        grade = input("Enter grade: ")
        print(f"{self.name} has graded {student} with {grade} in {course}")
        
        
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
        print("-----Thank you!-----")
        break
    else:
        print("Select from the menu options")