import math
from abc import ABC, abstractmethod

# --- Абстрактна фігура (інтерфейс)
class Shape(ABC):
  @abstractmethod
  def get_area(self):
    pass

class Rectangle(Shape):
  def init(self, width, height):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height

class Circle(Shape):
  def init(self, radius):
    self.radius = radius

  def get_area(self):
    return math.pi * self.radius ** 2

# відповідає лише за обчислення
class AreaCalculator:
  def init(self, shapes):
    self.shapes = shapes

  def calculate_total_area(self):
    return sum(shape.get_area() for shape in self.shapes)

# --- Основна частина
if __name__ == "main":
  shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(2, 2)
  ]

  calculator = AreaCalculator(shapes)
  print("Total Area:", calculator.calculate_total_area())