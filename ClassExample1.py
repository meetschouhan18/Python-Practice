class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        name = self.__class__.__name__
        print(name , " Destroyed")
point1 = Point()
del point1
#here both init and del are built in class attribute
#but we defined them to do extra work
#i.e del is used to delete attribute but we defined it to print a statement after doing its basic task i.e deleting
