from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass

  def sleep(self):
    print(f"{self.__class__.__name__} is sleeping...")

class Dog(Animal):
  def make_sound(self):
    print("Woof! Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow! Meow!")

if __name__ == "__main__":
  dog = Dog()
  cat = Cat()

  dog.make_sound()
  cat.make_sound()
  
  dog.sleep()
  cat.sleep()
