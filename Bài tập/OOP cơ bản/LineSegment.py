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
    
    def distance(self, P = None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            return math.sqrt((self.__x - P.__x)**2 + (self.__y - P.__y)**2)
        
class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.d1 = Point(8,5)
            self.d2 = Point(1,0)

        elif len(args) == 2 and isinstance(args[0], Point): 
            self.d1 = args[0]
            self.d2 = args[1]

        elif len(args) == 4:
            self.d1 = Point (args[0], args[1])
            self.d2 = Point (args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            src = args[0]
            self.d1 = Point(src.getX().x, src.getY().y)
            self.d2 = Point(src.getX().x, src.getY().y)

        else:
            raise ValueError("Tham số không hợp lệ!")

    def read(self):
        x1, y1, x2, y2 = map(int, input().split())
        self.d1 = Point(x1, y1)
        self.d2 = Point(x2, y2)

    def print(self):
        return f"[({self.d1.getX()}, {self.d1.getY()}); ({self.d2.getX()}, {self.d2.getY()})]"
    
    def __str__(self):
        return self.print()
    
    def move(self, dx, dy):
        self.d1.move(dx, dy)
        self.d2.move(dx, dy)

    def length(self): 
        return self.d1.distance(self.d2)
    
    def angle(self): 
        dx = self.d2.getX() - self.d1.getX()
        dy = self.d2.getY() - self.d1.getY()

        goc = math.degrees(math.atan2(dy, dx))

        if goc<0:
            goc += 360

        return round(goc)