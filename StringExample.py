def x():
    for i in str.lower():    #str.lower convert all character present in str in lower case
        if i in vowels:
            str1 = str.replace(i,"")
    print("New String After removing all Vowels is :- ",str1)

str = input("Enter any String :- ")
vowels = ['a','e','i','o','u']
try:
    x()
except:
    print("No Vowels Present")
    print("String is :- " , str)


#To make list form a string 
strng = 'Meet'
lst = list(strng)
print(lst)

# st = 'I'm good today' have error. Thus
st = 'I\'m good today'
print(st)
s = 'Today\tis\ta\tgood\tday.\nYeah!!!'
print(s)

#To print \ write \\ ex - s = 'Hello \\ World gives Hello \ World


#Multi-line String
p = '''Hello My name is Meet
I'm a student
Studying Python'''
print(p)


#Trick to compare strings
q = "Today is Monday"
print(q.upper())
print(q.lower())
#today and TODAY both are not equal to Today . Thus it can create confusion while comparing
#therefore, to compare simply use-
w = "TODay"
if w.lower() in q.lower(): #same can be done with upper()
    print("Present in both strings")


#Isupper , Islower - To check wether string is lower or upper
a = "TODAY"
print(a.isupper())
b = "a1b2c"
print(b.islower())

#Capitalize - make first letter capital
a = "meet"
print(a.capitalize())

#Startswith , Endswith - Tells whether string starts or ends with the specified character or word
z = "Today"
x = "Monday."
print(q.startswith(z))
print(q.endswith(x)) #False since "." is present
e = input("Enter name :- ")
if e == "Meet":
    print("Hello Master")
else:
    print("Hello Dude")


#Join -  Joining List to form a String
lis = ['Meet','Singh','Chouhan']
print(",".join(lis)) #these becomes string
print(" ".join(lis))
print(",".join(['Meet','Singh','Chouhan']))


#Split - Splits String to form a List
p1 = "My name is Meet Singh Chouhan"
li = p1.split() #it becomes a list
print(li)
#it is mostly used to detect multiline strings and get rid of empty spaces for ex-
q1 = '''Hello My name is Meet
I'm a student
Studying Python'''
t = q1.split("\n")
print(t)
p2 = "My\tname\n\tis\tmeet"
print(p2)
q2 = p2.split()
print(q2)


#Strip - removes unwanted Indentation
a = "	My Name is 	Meet		"
print(a.lstrip())   #remove left indentation
print(a.rstrip())   #remove right indentation
print(a.strip())    #remove both left and right indentation


#Find - Tells Location of specified character
a = "My name is Meet Singh"
a1 = a.find('e')    #prints position of specified character
print(a1)
print(a.find('M',a1))    #finds M present after a1(integer) which is the position of 1st e
#Thus it neglects M from 'My' and prints 11 which is the location of M from 'Meet'