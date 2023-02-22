import statistics
import matplotlib.pyplot as plt

est = [23,43,54,65,76,87,98,45,13,66,76,85,67,90,56,73,23,56,77,51]
plt.plot(est)

y = []
for i in range(len(est)):
	y.append(5)

plt.plot(est,y,'r--')
est.sort()

t = int(0.1*len(est))
est = est[t:len(est)-t]

a = []
for i in range(len(est)):
	a.append(5)


plt.plot(est,a,'r--')

plt.plot([statistics.mean(est)],[5],'g^')

plt.plot([statistics.median(est)],[5],'bs')
