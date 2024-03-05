# abstraction assignment:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def area(self,radius):
        area_circle = 3.14 * (radius ** 2)
        return area_circle
    
class Rectangle(Shape):
    def area(self,length,width):
        area_rect = length * width
        return area_rect

cirobj = Circle()
rectobj = Rectangle()

area_of_circle = cirobj.area(2)
area_of_rect = rectobj.area(5,10)

print(area_of_circle)
print(area_of_rect)
