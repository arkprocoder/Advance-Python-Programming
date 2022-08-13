# from abc import ABCMeta, abstractmethod Abstract Base Class & @abstractmethod 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod   
    def mandatory(self):
        return 0

class Circle(Shape):
    type = "Circle"
    Sides = 0
    def __init__(self):
        self.radius = 5
        self.pie = 3.14

    def printarea(self):
        return self.radius *self.radius* self.pie

    def mandatory(self):
        print("DONE bro" )

c = Circle()

print(c.printarea())
print(c.type)
c.mandatory()

