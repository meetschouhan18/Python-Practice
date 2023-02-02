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
s = (m + n) / 2

for i in range (0, 5):
	p = a*s*s*s + b*s*s + c*s + d
	q = 3*a*s*s + 2*b*s + c
	o = s - (p / q)
	f = a*o*o*o + b*o*o + c*o + d
	print("Value of f(x) at x = ",o," is   ",f ,"\n")
	s = o

print("Thus Root of the equation(upto 6 decimal places) is :- ",round(o, 6),"     (Using Newton Raphson Method)")
