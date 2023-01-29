import os
print(os.getcwd())

p = open('a.txt','w')     #Opening an exisiting file to write only
q = 'Meet'
p.write(q)                     #Previously exisitng data is deleted and string q is written in its place
#print(p.write(q))           #It prints no. of bytes we added after removing previous data(18 bytes in this case)
p.close()

p = open('a.txt','r')     #Opening an existing file to read only
print(p.read())
p.close()

p = open('a.txt','a')      #Opening an exisiting file to append data
q = ' Singh Chouhan'
p.write(q)                      #No data is deleted, New data is added
#print(p.write(q))            #Prints no. of bytes added
p.close()

p = open('b.txt','r')
for line in p.readlines():     #readlines is used to read multiple lines
    print(line)
p.close()

p = open('b.txt','r')
print("Getting rid of new lines")
for line in p.readlines():
    line = line.strip('\n')    #we stripped every \n
    print(line)
p.close()
