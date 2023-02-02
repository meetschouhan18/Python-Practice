t = 0

print("Equation is of the form a*x^3 + b*x^2 + c*x + d ");
a = int(input("Enter the value of a :- "))
b = int(input("Enter the value of b :- "))
c = int(input("Enter the value of c :- "))
d = int(input("Enter the value of d :- "))

while t == 0:

	x = int(input("Enter the value of x at which f(x) is to be calculated :- "))
	e = a*x*x*x + b*x*x + c*x + d
	print("Value of f(x) at x = ", x ," is   ",e)
	t = int(input("Enter 0 to continue calculating f(x) :- "))
	
print("After calculating different values of f(x) you must have got a negative and a positive value of f(x) at x being two consecutive integers...")
m = int(input("Enter value of x at which f(x) is positive :- "));
n = int(input("Enter value of x at which f(x) is negative :- "));

for i in range (0, 5):
	o = (m+n)/2
	f = a*o*o*o + b*o*o + c*o + d
	print("Value of f(x) at x = ",o," is   ",f ,"\n")

	if f > 0:
		m = o
	if f < 0:
		n = o

print("Thus Root of the equation (upto 5 decimal places) is :- ",o,"    (Using Bisection Method)")
