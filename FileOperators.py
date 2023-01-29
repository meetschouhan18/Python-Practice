import os
print(os.getcwd())                                                            #cwd - current working directory
os.chdir("C:\\Users\\Rohan Singh Chouhan\\Desktop")#chdir - change directory
print(os.getcwd())
#os.makedirs("File Created By Python.txt")                     #makedirs make directory in the directory it is present
                                                                                         #Since we changed directory above thus or present directory 
                                                                                   #is Desktop Thus directory(file .Since no extensions were given)
                                                                                         #will be created on desktop
#os.makedirs("C:\\Users\\Rohan Singh Chouhan\\Desktop\\meet python\\Folder ")
                                                                                         #we just created a directory in a location we were not present
                                                                                         #Without Changing our location 
print(os.path.isabs("C:\\Users\\Rohan Singh Chouhan\\Desktop"))
                                                                              #It tells wheter path entered is true or not by outputting boolean value
print(os.path.isabs("Desktop\\Users"))
file_path = "C:\\Users\\Rohan Singh Chouhan\\Desktop\\meet python\\a.txt"
print(os.path.split(file_path))                               #It splits file name and its path as 2 strings
dir,name = os.path.split(file_path)
print("Path of file :- " + name + " is :- " + dir)
print(os.path.getsize(file_path))                           #It gives size of file
#print(os.system('dir'))
print(os.path.exists('a.txt'))                                  #Tells in boolean whether file exists in same directory as our location
print(os.path.exists('meet python'))
print(os.path.isdir("C:\\Users\\Rohan Singh Chouhan\\Desktop\\meet python"))#True since meet python is a directory
print(os.path.isfile("C:\\Users\\Rohan Singh Chouhan\\Desktop\\meet python\\a.txt"))   #True since a.txt is a file
                                                                              #These tells in boolean the path is of a directory or a file
