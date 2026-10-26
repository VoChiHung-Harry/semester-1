# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """
    def __init__(self,x_coordinate,y_coordinate):
    # Add constructor here
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Add distance() method here
    def distance(self):
        return math.hypot(self.y_coordinate , self.x_coordinate)

    # Add distance_to() method here
    def distance_to(self,other):
        dist = math.hypot((self.x_coordinate - other.x_coordinate),(self.y_coordinate - other.y_coordinate))
        return dist
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p1 = Point(0, 0)
p2 = Point(1, 1)

distance = p1.distance_to(p2)
print(distance)