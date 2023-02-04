# Map

n,m = map(int,input().split())
print(n)
print(m)

# it takes input , split it and convert it into integer
# here we already know we will have 2 inputs

#if we want to use map inside any function then we use *map
# since the value returned by map are to be treated as argumnets
# ex- 

import numpy as np
a = np.eye(*map(int,input().split()))
print(a)
#here eye is a function in array .thus we used *map

Q1.)Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda k : 'Fruit: '+k, lst_check)

# we decribed the function using lambda, in the parenthesis of map itself
