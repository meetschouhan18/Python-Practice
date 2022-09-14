r = input("Enter any number :- ")
try:
    i = int(r)
except:
    i = -1
if i > 0 or i <= 0:
    print("Nice Work")
else:
   print("Its not a number.. you idiot ")

#we can also mention the error in execpt which occur in try
# ex - except ZeroDivisionError: #it occurs when number is divided by 0
#Thus we can execute different tasks for different errors in a single try by using various excepts with type of error mentioned in it

try:
    f = open('asasdasd')
    f.write('This is a test file')
except:
    print("Can't Open That File,It doesn't exist!!!")
else:
    print('Everything worked well!!')
#Since in this case file does not exist Thus except is excuted
#But if file do exist then after executing try, else will also be printed out
