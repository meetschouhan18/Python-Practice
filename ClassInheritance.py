class Parent:
    def P(self):
        print("Printing Parent Function")
        
class Student(Parent):
    def S(self):
        print("Printing Student Function")
        
c = Student()
c.S()
c.P()

#here Student class Inherit Parent class
#thus we can use functions of Psarent class
#using instance of Student class
