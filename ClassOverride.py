class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector (%d , %d)' %(self.a , self.b)     
        #%d will print integer value which is defined after string in brackets 
    
    def __add__(self,other):
        return Vector(self.a + other.a , self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)

#here we overrided '+' i.e __add__ operator
