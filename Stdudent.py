 # Create class "Student"
class Student:
 
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
 
    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
        file = open("student.txt", "w")
        for i in ls:
            file.write(f"{i}")
 
# list to add Students
ls = []

# object of Student class
obj = Student('', 0, 0, 0)
 
print("\nChoices are, ")
print("\n1.Enter Student details\n2.Display Student Details\n3.Search Details of a Student\n")
 
ch = int(input("Enter choice:"))
if(ch == 1):
    obj.accept(input("Enter student name: "), int(input("Enter roll no: ")), int(input("Enter Sem 1 marks: ")), int(input("Enter Sem 2 marks: ")))    
    obj.accept(input("Enter student name: "), int(input("Enter roll no: ")), int(input("Enter Sem 1 marks: ")), int(input("Enter Sem 2 marks: ")))    
    obj.accept(input("Enter student name: "), int(input("Enter roll no: ")), int(input("Enter Sem 1 marks: ")), int(input("Enter Sem 2 marks: ")))

elif(ch == 2):
    print("\n")
    print("\nList of Students\n")
    file = open("student.txt", "r")
    text = file.read()
    print(text)
 
elif(ch == 3):
    student = input("Enter student name to search: ")
    file = open("student.txt", "r")
    text = file.read()
    if student in text:
        print("\n Student Found, ")
        print(student)
 
else:
    print("Enter correct choice")