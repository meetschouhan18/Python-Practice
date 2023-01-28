import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
#timedelta is same as datetime but timedelta can also take weeks


print(dir(datetime.date))
#it provides various functions present inside datetime library

print(datetime.datetime.now())
#prints date and time at this instant

print(datetime.date.today())
#prints today's date

a = 2000
b = 12
c = 18
print(datetime.date(a,b,c))
#prints date - 2020-12-18 #my bday

print(datetime.date.fromtimestamp(1))
#it will print the date when 1sec has passed from 1-1-1970

#Inside datetime 'date' is present , and inside date 'fromtimespan' is present
#In fromtimespan function 1-1-1970 date is set and we provide seconds passed in the parenthesis(which is 1 in this case)
#This function can also be called by importing date class from datetime directory


print(date.fromtimestamp(34534523))
#it will print the date when 34534523sec has passed from 1-1-1970

tooday = date.today()
print("\t",tooday)

print("Current Year - " , tooday.year , "\nCurrent Month - " , tooday.month , "\nCurrent Date - " , tooday.day)
#It prints each value seperately


a = time()
#set time to 0:0:0
print(a)

b = time(11,34,36,33244)
#set time to 11:34:36:33244
print(b)
print("Hours :- " , b.hour , "\nMinutes :- " , b.minute , "\nSeconds :- " , b.second , "\nMicroseconds :- " , b.microsecond)


a = datetime(2000,12,18,2,30,15,324)   #prints date and time simultaneously
print(a)
print(a.year , "\t" , a.second ,"\t" , a.timestamp())  #timestamp() prints seconds from 1-1-1970 to 18-12-2000



t1 = datetime(year = 2000, month = 12, day = 18, hour = 2, minute = 30, second = 15)
t2 = datetime(year = 2020,month = 5, day = 20, hour = 19, minute = 14, second = 30)
t3 = t2 - t1
print("My Birthdate :- " , t1)
print("Today's Date :- " , t2)
print("Days and time elapsed since my bday :- " , t3)



t1 = timedelta(weeks = 5, days = 4, hours = 2, seconds = 23)
t2 = timedelta(days = 19, hours = 12, minutes = 23, seconds = 33)
print(t1 - t2)
print(t2 - t1)
print(t1 , "\tis equal to :- " , t1.total_seconds() , " seconds")
#total_seconds() convert everything into seconds



now = datetime.now()
print(now)

t = now.strftime('%d/%m/%Y, %H:%M:%S')
print(t)
#strftime() - string from time . It creates string
#%d - day, %m - month , %Y - year , %H - hour , %M - minute , %S - seconds


st = '18 December 2000'
d = datetime.strptime(st, '%d %B %Y')
print(d)
#strptime() - strip time . It creates time from string
#inside parenthesis we first provide our string and the our strings format
#%d - day, %B - converts words into month number, %Y - year
