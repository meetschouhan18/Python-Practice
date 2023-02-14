from statistics import mean
li = [90,44,75,66,54,26,56,88,56,47,66,45,35,69,75,68,98]
li.sort()
x = int(0.1*len(li))
li = li[x:len(li)-x]
print(li)
print(mean(li))

#list is sorted and using slicing list's 1st and last element is discarded and mean is calculated from the remaining list
#Example of slicing list
#list = [1,2,3,4,5,6,7,8]
#y = list[0:4]
#z = list[:2]
#p = list[5:]
# Answer - y = [1,2,3,4] , z = [1,2] , p = [6,7,8]