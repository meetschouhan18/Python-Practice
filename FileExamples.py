import os
dir = input("Enter path of directory(Use \\\ to seperate directories) :- ")   #We get location
os.chdir(dir)                                                                                                   #We go to that location
name = input("Enter file name which you want to create(extension required) :- ")                         #We get file's name
content = '''Hello Meet
Good Moring
What's going on
'''                                                                                          #We get file's content
p = open(name , 'w')                                                              #We create a file with name = name and its location = dir
p.write(content)
p.close()
p = open(name , 'r')
print(p.read())
p.close()
p = open(name , 'r')
for i in p.readlines():
    i = str(i.strip('\n'))
    print(i)
    i = i[::-1]
    print(i)
    p = open(name , 'a')
    p.write(str(i + '\n'))
    p.close()
    p = open(name , 'r')
