n = int(input("Enter number of processes :- "))
AT = []
BT = []
CT = []
TAT = []
WT = []
temp = []
for i in range(0, n):
	m = int(input("Enter Arrival Time :- "))
	AT.append(m)
for i in range(0, n):
	m = int(input("Enter Burst Time :- "))
	BT.append(m)
	temp.append(m)
q = AT.index(min(AT))
CT.extend(range(n))
TAT.extend(range(n))
WT.extend(range(n))
CT[q] = BT[q]
w = CT[q]
temp[q] = 100
for i in range(0, n-1):
	p = temp.index(min(temp))
	CT[p] = min(temp) + w
	w = CT[p]
	temp[p] = 100
for i in range(0, n):
	TAT[i] = CT[i] - AT[i]
for i in range(0, n):
	WT[i] = TAT[i] - BT[i]
print("Arrival Time :- ",AT)
print("Burst Time :- ",BT)
print("Completion Time :- ",CT)
print("Turn Around Time :- ",TAT)
print("Waiting Time :- ",WT)