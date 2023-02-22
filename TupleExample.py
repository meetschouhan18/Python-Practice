tup = ('My','name','Is','O',0,7)

print(tup[0])
print(tup[0:5])
print(len(tup))

try:
   tup[3] = 'Meet'
except:
    print("Elements of tuple cannot be changed")

#To make changes in tuple we have to convert tuple in list and then again convert it back to tuple

lst = list(tup)
print(lst)
lst[3] = 'Meet'
tup = tuple(lst)
print(tup)
