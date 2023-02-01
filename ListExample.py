list = [[1,2,3,4,5],['Meet','Singh','Chouhan']]
test1 = list[0][0]
test2 = list[1][0]
test3 = list[-1][2]
print(test1)
print(test2)
print(test3)
if 2 in list[0]:
    print("2 is present")
else:
    print("2 is not present")
list1 = ['My','Name','Is','Meet']
if 'Meet' in list1:
    print("Hello",list[1][0])

#Joining list to form a string
lis = ['Meet','Singh','Chouhan']
print(",".join(lis)) #these becomes string
print(" ".join(lis))
print(",".join(['Meet','Singh','Chouhan']))

#Spliting string to form a list
p = "My name is Meet Singh Chouhan"
li = p.split() #it becomes a list
print(li)
#It get rid of empty spaces for ex-
p2 = "My\tname\n\tis\tmeet"
print(p2)
q2 = p2.split()
print(q2)