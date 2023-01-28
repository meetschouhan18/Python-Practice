dict = {"Meet":"A+" , "Billa":"A" , "Abhinay":"B+" , "Swapnil":"B"}
name = input("Enter person's name whose grade is required :- ")

if name in dict:
    print("Grades obtained by " + name + " is " + dict[name])
else:
    print("Wrong Input")


#To print keys
print("Printing Keys")
for i in dict.keys():
    print(i)


#To print values
print("Printing Values")
for i in dict.values():
    print(i)


#To print them together
print("Printing each items in dictionary")
for i in dict.items():
    print(i)


#Alternative method
print("Printing each items in dictionary (alternative method)")
for i,j in dict.items():
    print(i + "  : " + j)


#Alternative method to print values in dictionary using keys
a = input("Enter Name :- ")
print("Grades of " + a + " is " + str(dict.get(a,"Not present")) + " ..")
#In .get function inside brackets 1st value is key (inputted) and second value print statement present there in case if inpuuted key is not present in the dictionary


#changing keys and values of previously defined dictionary
dict1 = {'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5}

vdict = {p:q*2 for (p,q) in dict1.items()}
print("Doubling Values")
print(vdict)

kdict = {p*2:q for (p,q) in dict1.items()}
print("Doubling Keys")
print(kdict)


#Creating A dictionary with conditions
#Ex - key should be divisible by 2 and value should be square of key
number = range(0,10)
dicti = {}
for m in number:
    if m%2 == 0:
        dicti[m] = m**2
print(dicti)


#OR Simple approach
dicti1 = {m:m**2 for m in number if m%2 == 0}
print(dicti1)


#Final Example Questions On Dictionary
#We will use dict1
d1 = {k:v for (k,v) in dict1.items() if v>3 and v%2 == 0}
print(d1)
