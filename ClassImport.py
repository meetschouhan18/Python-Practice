#since both class file and this program is in the same directory
#we do not need to change our directory
import Class
employee1 = Class.Employee("Meet","meetschouhan12@gmail.com","19")
employee1.displayInfo()
#we define instance employee1 as 1st we write file name then . then class name and then in brackets comes attributes

print("Operating Manual")
print("Q -- Quit the program\nAdd -- Add Student\nDisplay -- Display Student's Information\nCount -- No. of students info available")
while True:
    option = input("Enter the option you desire :- ")
    option = option.lower()
    if option == 'q':
        print("Exiting")
        break
    elif option == 'add':
        firstn = input("Enter Student's First name :- ")
        lastn = input("Enter Student's Last name :- ")
        sub = input("Enter Student's Subject :- ")
        grad = input("Enter Student's Grades :- ")
        student1 = Class.Student(firstn,lastn,sub,grad)
        print("Student's Information added successfully")
    elif option == 'display':
        try:
            student1.studentInfo()
        except:
            print("You should add information first")
    elif option == 'count':
        print("Total Number of Students are :- " , Class.Student.count)
    else:
        print("Wrong Choice, Provide proper Input !!!!!...")
