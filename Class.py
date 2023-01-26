class Employee:
    emp = 0
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        Employee.emp += 1
        
    def displayCount(self):
        print("Total Number of Employee is :- " , Employee.emp)
        
    def displayInfo(self):
        print("Name :- " , self.name , " Email :- " , self.email , " Age :- " , self.age)

        
class Student:
    count = 0
    def __init__(self,fname,lname,subject,grade):
        self.fname = fname
        self.lname = lname
        self.subject = subject
        self.grade = grade
        Student.count += 1
        
    def studentInfo(self):
        print("First name :- " , self.fname)
        print("Last name :- " , self.lname)
        print("Subject :- " , self.subject)
        print("Grades :- " , self.grade)
