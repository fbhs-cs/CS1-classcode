import math

class Point:
    def __init__(self, x, y):
        self.coordinates = (x, y)
    
    def __str__(self):
        return str(self.coordinates)
    
    def distance(self, other_point):
        x1 = self.coordinates[0]
        y1 = self.coordinates[1]
        x2 = other_point.coordinates[0]
        y2 = other_point.coordinates[1]
        return math.sqrt( (x2-x1)**2 + (y2-y1)**2 ) 
        
class Segment:
    def __init__(self, point1, point2):
        self.end_points = (point1, point2)
    
    def __str__(self):
        return str(self.end_points[0]) + ", " \
               + str(self.end_points[1])
    
    def length(self):
        ep1 = self.end_points[0]
        ep2 = self.end_points[1]
        return ep1.distance(ep2)
    
class Triangle:
    def __init__(self, segment1, segment2, segment3):
        self.sides = (segment1, segment2, segment3)

    def __str__(self):
        return "\nside 1: %s\nside 2: %s\nside 3: %s" \
               % ( str(self.sides[0]), str(self.sides[1]), \
                   str(self.sides[2]) )

    def perimeter(self):
        side1 = self.sides[0].length()
        side2 = self.sides[1].length()
        side3 = self.sides[2].length()
        return side1 + side2 + side3
    
    def area(self):
        s = self.perimeter() / 2
        a = self.sides[0].length()
        b = self.sides[1].length()
        c = self.sides[2].length()
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    