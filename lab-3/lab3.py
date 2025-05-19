import copy

class Shape:
  def __init__(self, color):
    self.color = color

  def clone(self):
    return copy.deepcopy(self)

  def display(self):
    print(f"Shape with color: {self.color}")

class Circle(Shape):
  def __init__(self, color, radius):
    super().__init__(color)
    self.radius = radius

  def display(self):
    print(f"Circle with radius: {self.radius} and color: {self.color}")

class Rectangle(Shape):
  def __init__(self, color, width, height):
    super().__init__(color)
    self.width = width
    self.height = height

  def display(self):
    print(f"Rectangle {self.width}x{self.height} with color: {self.color}")

def main():
  print("Оригінальні об'єкти:")
  circle1 = Circle("Red", 5)
  rect1 = Rectangle("Blue", 4, 6)

  circle1.display()
  rect1.display()

  print("\nКлоновані об'єкти:")
  circle2 = circle1.clone()
  rect2 = rect1.clone()

  # Змінюємо властивості клонів
  circle2.color = "Green"
  circle2.radius = 7
  rect2.height = 10

  circle2.display()
  rect2.display()

if __name__ == "__main__":
  main()

