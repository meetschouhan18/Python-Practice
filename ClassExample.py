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
        
employee1 = Employee('Meet','meetschouhan12@gmail.com','19')
employee1.displayInfo()
employee1.displayCount()

employee2 = Employee('Rohan','rohanschouhan@gmail.com','23')
employee2.displayInfo()
employee2.displayCount()

employee1.email = 'meetschouhan18@gmail.com'    #Updating email of employee1
employee1.displayInfo()

setattr(employee1, 'name', 'Meet Singh Chouhan')    #setattr - set sttribute is used to change attribute of a specified instance
employee1.displayInfo()

#del employee1.age     #Deleting attribute of an instance
#delattr(employee1, 'age')    #same

print(getattr(employee2, 'age'))        #getattr - get attribute means to get the specified attribute (ex - age) from specified instance(ex - employee2)

print(hasattr(employee1, 'phone-number'))    #hasattr - has attribute outputs boolean value showing whether the specified instance(employee1) has the specified attribute(phone-number) or not

print("Class name :- ", Employee.__name__)   #we can print various attributes of class ex- name using __attribute-name__
