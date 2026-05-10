import math

class Point:
    def __init__(self, x = 0, y = 1):
        self.__x = x
        self.__y = y

    def read(self):
        x,y = map(int,input().split())
        self.__x = x
        self.__y = y
        
    def print(self):
        print(f"({self.__x}, {self.__y})")
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
    
    def distance(self, P = None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            return math.sqrt((self.__x - P.__x)**2 + (self.__y - P.__y)**2)        

class PointTest:
    def testCase(cls):
        A = Point()
        A.print()

        B = Point()
        B.read()  
        B.print() 

        B.move(1,1)
        B.print()
        
        print(B.distance())



    