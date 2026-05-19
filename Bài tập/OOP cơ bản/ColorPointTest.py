import math

class Point:
    def __init__(self, x = 0, y = 1):
        self.__x = x
        self.__y = y

    def read(self): 
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y

    def print(self):
        return f"({self.__x}, {self.__y})"
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, P = None):
        if P is None:
            return math.sqrt ((self.__x)**2 + (self.__y)**2)
        else:
            return math.sqrt ((self.__x - P.__x)**2 + (self.__y - P.__y)**2)
        
class ColorPoint(Point):
    def __init__(self, x = 0, y = 1, color = "xanh" ):
        if isinstance(x, ColorPoint):
            super().__init__(x.getX(), x.getY())
            self.__color = x.__color
        else:
            super().__init__(x, y)
            self.__color = color
            
    def __str__(self):
        return f"({self.getX()}, {self.getY()}): {self.__color}"

    def read(self):
        data = input().split()
        x = int(data[0])
        y = int(data[1])
        color = " ".join (data[2:])

        self.setXY(x, y)
        self.__color = color

    def print(self):
        return f"({self.getX()}, {self.getY()}): {self.__color}"

    def setColor(self, color):
        self.__color = color

class ColorPointTest:
    @staticmethod
    def testCase():
        c1 = ColorPoint()
        print(c1)
        c2 = ColorPoint()
        c2.read()
        print(c2)
        c3 = ColorPoint(c2)
        c2.move(5, 5)
        print(c2)
        print(c3)