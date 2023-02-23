#zip function

l1 = [1,2,3]
l2 = [4,5,6]
l3 = list(zip(l1, l2))
print(l3)

#this returns l3 = [(1,4), (2,5), (3,6)]
# it creates a tuple of elements present at the same position in the lists given in argument

l4 = []
for (x1, x2) in l3:
  l4.append(x1+x2)

print(l4)

# this outputs the list of sum of the tuples created by zip file
