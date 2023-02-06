import numpy as np

# ex1
lst = [1,2,3]
x = np.array(lst)
print(x)

# ex2
x = np.array([4,5,6])
print(x)

# ex3 - 2*3 matrix
x = np.array([[7,8,9] , [1,2,3]])
print(x)

# ex4 - shape function tells rows and column of array
print(x.shape)

# ex5 - arange function returns evenly spaced values within a given interval
x = np.arange(0,30,2)
print(x)
#from 0 to 30 with spacing of 2

# ex6 - reshape function changes the shape into given no. of rows and column
# reshape returns while resize  changes dimensions in place
x = x.reshape(3,5)
print(x)
x. resize(5,3)
print(x)

#ex7 - linspace function is same as arange but in it we tell how many number we want returned and the function will split the intervals accordingly
x = np.linspace(0,4,9)
print(x)
#from 0 to 4 we need 9 numbers

#ex8 - ones - matrix of 1's , zeros - matrix of 0's , eye - identity matrix , diag - prints number diagonally
print(np.ones((3,3))) # 3 rows , 3 column
print(np.zeros((3,3)))
print(np.ones((2,1,3))) # 2 times , 1 row , 3 column
print(np.ones((3,2,1,4))) # 3 times , pair of 2 , 1 row , 4	 column
print(np.eye(3))
y = [1,3,5]
print(np.diag(y))

#ex9 - * and repeat function
# * prints whole list n times
# repeat function prints each element n times
print(np.array([1,2,3]*3))
print(np.repeat([1,2,3],3))

# ex10 - vstack - stack array vertically , hstack - stack array horizontally
p = np.ones([2,3],int) #int is to convert float into int
print(p)
print(np.vstack([p,2*p]))
#it prints p then vertically prints 2*p
print(np.hstack([p,2*p]))
#it prints p then horizontally prints 2*p

# ex11 - operations
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x*y)
print(x**2)
z = np.array([y , y**2]) #created an array from another array
print(z)
print(np.transpose(z)) #transpose array z
print(z.T) #T means transpose means convert rows into columns
print(z.flatten()) #convert array in single line

# ex12 - type of data
print(z.dtype) #prints type of data present i.e integer in this case
z = z.astype('f') #convert data from one type to another
print(z.dtype)

# ex13 - searching element
print(x.sum())
print(x.argmax()) #prints index of last element
print(x.argmin()) #prints index of 1st element

# ex14 - indexing/slicing
p = np.array([1,2,3,4,5,6,7,8,9])
print(p[0] , p[3] , p[8])
print(p[3:6])
print(p[-5::-2])
r = np.arange(36)
r.resize(6,6)
print(r)
print(r[2,2])
print(r[3 , 3:6])
print(r[r>30])
r[r>30] = 30
print(r)

# ex15 - copying data using slicing/indexing
r1 = r[:3 , :3]
print(r1)
r1[:] = 0
print(r1)
print(r)
# Thus we can see that changes done in slice is also reflected back on the original variable as well
# i.e changes made in r1 were also made in r indirectly
# in order to avoid this , we use copy function
r_copy = r.copy()
print(r_copy)
r_copy[:] = 10
print(r_copy)
print(r)
# changes made in copy is not reflected back on the original variable

# ex16 - Iterating over array
test = np.random.randint(0,10,(4,3))
# this means random integer from 0 to 10 in 4*3 dimension
print(test)

# ex16.1 - printing using row
for row in test:
    print(row)

# ex16.2 - printing using index
for i in range(len(test)):
    print(test[i])

# ex16.3 - printing using both row and index by using enumeration function
for i,row in enumerate(test):
    print("row " , i , " has elements :- " , row)

# ex16.4 - zip function is used when loop is to be used on multiple arrays
test1 = test**2
print("test = ")
print(test)
print("test1 = ")
print(test1)

for i,j in zip(test,test1):
    print(i , " + " , j , " = " , i+j)
r = np.arange(36)
r.resize(6,6)
print(r[2:4,2:4])

# ex17 - concatenate function joins arrays in the specified axis
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[2,3,4],[5,6,7]])
print(np.concatenate((x,y))) # axis not specified ,thus joined vertically(axis = 0)
print(np.concatenate((x,y), axis = 1)) # axis is specified (axis = 1 means horizontally)

# ex18 - floor - gives int value of floating no. , ceil - gives next int value of floating no. , rint - round off no.
x = np.array([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
print(np.floor(x))
print(np.ceil(x))
print(np.rint(x))

# ex19 - set_printoptions - using it we can print anything before printing elements of array
np.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None, formatter=None, sign=None, floatmode=None, *, legacy=None)
#these all are the parameters which can be used
#if we want to add any character or space before every element ,then-
np.set_printoptions(sign=" ")
#this will add " " before every element

# ex20 - np.sum(array_name , axis) - gives sum of elements , similarly np.prod(array_name , axis) - gives product
x = np.array([[1,2],[3,4]])
print(np.sum(x , axis = 0)) # sum is [4,6] elements are added along y-axis
print(np.sum(x , axis = 1)) # sum is [3,7] elements are added along x-axis
print(np.sum(x)) # sum is 10 since no axis is specified
print(np.prod(x , axis = 0)) # product is [3,8] elements are multiplied along y-axis
print(np.prod(x , axis = 1)) # product is [2,12] elements are multiplied along x-axis
print(np.prod(x)) # product is 24 since no axis is specified

# ex - 21 - max(array_name , axis) - gives max. element i that axis and min(array_name,axis) - gives min.
x = np.array([[1,2],[3,4]])
print(np.max(x , axis = 0)) #output - [3,4] as 3 and 4 are largest in y-axis
print(np.max(x , axis = 1)) #output - [2,4] as 2 and 4 are largest in x-axis
print(np.max(x)) # output is 4
print(np.min(x , axis = 0)) # op - [1,2]
print(np.min(x , axis = 1)) # op - [1,3]
print(np.min(x)) # op- 1

# ex - 22 - mean(array_name , axis) - gives mean along specified axis , var(array_name , axis) - gives variance , std(array_name , axis) - gives standard deviation
x = np.array([[1,2],[3,4]])
print(np.mean(x , axis = 0)) # output - [2.0,3.0] along y-axis
print(np.mean(x , axis = 1)) # output - [1.5 , 3.5] along x-axis
print(np.mean(x)) # op - 5
#similarly with variance and standard deviation

# ex - 23 - dot(array1, array2) - gives dot product(matrix multiplication) , cross(array1,array2) - gives cross product
x = np.array([[1,2],[3,4]])
y = np.array([[1,2],[3,4]])
print(np.dot(x,y)) #gives matrix multiplication as output
print(np.cross(x,y)) #gives cross product of 2 arrays

# ex - 24 - inner(array1,array2), outer(array1,array2)
x = np.array([[1,2],[3,4]])
y = np.array([[1,2],[3,4]])
print(np.inner(x,y))
#inner gives inner multiplication i.e.
#x = [1 2]   y = [1 2]   op = [1*1+2*2  1*3+2*4]
#      [3 4]        [3 4]          [3*1+4*2  3*3+4*4]
print(np.outer(x,y))
#gives outer multiplication i.e
#x = [1 2]   y = [1 2]   op = [1*1  1*2  1*3  1*4]
#      [3 4]        [3 4]          [2*1  2*2  2*3  2*4]
#                                        [3*1  3*2  3*3  3*4]
#                                        [4*1  4*2  4*3  4*4]

# ex - 25 - polynomials
#1. poly - The poly tool returns the coefficients of a polynomial with the given sequence of roots.
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]
#2. roots - The roots tool returns the roots of a polynomial with the given coefficients.
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]
#3. polyint - The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]
#4. polyder - The polyder tool returns the derivative of the specified order of a polynomial.
print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]
#5. polyval - The polyval tool evaluates the polynomial at specific value.
print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34
#6. polyfit - The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)    #Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

# ex - 26 - linear algebra
#1. linalg.det - The linalg.det tool computes the determinant of an array.
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
#2. linalg.eig - The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                     #Output : [[ 0.70710678 -0.70710678]
#                                                  #          [ 0.70710678  0.70710678]]
#3. linalg.inv - The linalg.inv tool computes the (multiplicative) inverse of a matrix.
print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
#                                                              #          [ 0.66666667 -0.33333333]]
