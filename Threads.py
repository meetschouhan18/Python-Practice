import _thread
import time
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)      #number of seconds specified in sleep func is the time program will not do anything
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time , ("Thread - 1" , 2 , ))
    _thread.start_new_thread(print_time , ("Thread - 2" , 4 , ))
except:
    print("error")

while True:    #this loop do nothing but runs infinitaly 
    pass           #this loop simply passes and calls function idk how?

#while loop is an infinity loop . thus to come out of it in cmd type ctrl+c

#in this program
#2 threads are working simultaneously i.e. Thread - 1 and Thread - 2
#thread1 prints its name and time after every 2 sec(delay time) total 5 times(count) while running the rest program
#thread2 prints its name and time after every 4 sec(delay time) total 5 times(count) while running the rest program
#_thread.start_new_thread is function used to create a thread and inside its parenthesis we declare a function(ex - print_time in our case)
#thread perform that specified function 
