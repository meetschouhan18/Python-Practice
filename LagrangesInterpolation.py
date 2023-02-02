x = []
y = []

n = int(input("Enter number of elements in x column :- "))
print("Enter elements of x column :- ")

for i in range(0, n):
	a = int(input())
	x.append(a)
print("Enter elements of y or f(x) column :- ")

for i in range(0, n):
	b = int(input())
	y.append(b)
r = 0
m = int(input("Enter the value of x at which y is to be calculated :- "))

for i in range(0, n):
	t = i
	p = 1
	q = 1

	for j in range(0, n):
		if j != t:
			p = (m - x[j])*p
			q = (x[t] - x[j])*q
	z = (p*y[t])/q
	r = r + z

print("Y at x =",m,"  is = ",r,"     (Using Lagranges Interpolation Formula )")
