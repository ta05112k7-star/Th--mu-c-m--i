import math

class Point:
    def __init__ (self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

def distance(p1: Point, p2: Point)->float:
    return math.sqrt((p1.x - p2.x)**2 + (p1.y -p2.y)**2)
        
def point_in_circle(circle: Circle, point: Point)->bool:
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle: Circle, rect: Rectangle)->bool:
    
    c = rect.corner 
    corners = [
        Point(c.x, c.y),
        Point(c.x + rect.width, c.y),
        Point(c.x, c.y + rect.height),
        Point(c.x + rect.width, c.y + rect.height),
    ]
    return all(point_in_circle(circle, p)for p in corners)

def rect_circle_overlap(circle: Circle, rect: Rectangle)-> bool:
    c= rect.corner
    corners = [
        Point(c.x, c.y),
        Point(c.x + rect.width, c.y),
        Point(c.x, c.y + rect.height),
        Point(c.x + rect.width, c.y + rect.height),
    ]
    return any(point_in_circle(circle, p)for p in corners)

circle = Circle(Point(150,100), 75)
p1 = Point(150, 100)
p2 = Point(300, 300)
print (f"p1 trong vòng tròn: {point_in_circle(circle, p1)}")
print (f"p2 trong vòng tròn: {point_in_circle(circle, p2)}")

rect_small = Rectangle(Point(140, 90),10,10)
rect_large = Rectangle(Point(100,50),300,200)
print (f"rect_small trong circle: {rect_in_circle(circle, rect_small)}")
print (f"rect_large overlap circle: {rect_in_circle(circle, rect_large)}")