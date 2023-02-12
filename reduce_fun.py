# reduce function was built-in in Python2
# in python3 it is needed to import from functools


data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x, y: x*y
a = reduce(multiplier, data)
print(a)

# output - 6469693230
# reduce function works as follows
# since multiplier takes 2 values
# 2,3 are passed in multiplier
# thus, output = 6
# then 6, 5 is passed in multiplier
# output = 30
# then 30, 7 is passed in multiplier
# as it goes on
# when it reaches last element it returns the final output

# reduce function is not used much