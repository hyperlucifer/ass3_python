# write a python program to class circle and compute the area and circumferences 
# of circle (use parameterize constructor)
import math
class circle:
    def __init__(self,r) -> None:
        self.r=r
    
    def area(self):
        return math.pi * self.r * self.r
    
    def circumferences(self):
        return 2*math.pi*self.r

c=circle(3)
print(c.area())
print(c.circumferences())