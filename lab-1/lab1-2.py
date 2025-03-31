from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass

  def sleep(self):
    print(f"{self.__class__.__name__} is sleeping...")

class Dog(Animal):
  def __init__(self, name, age):
    self.__name = name 
    self.__age = age   

  def make_sound(self):
    print("Woof! Woof!")

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_age(self):
    return self.__age

  def set_age(self, age):
    self.__age = age


# Тестування
dog = Dog("Rex", 5)

print(dog.get_name())  
dog.set_name("Buddy")
print(dog.get_name())  

dog.make_sound() 

dog.sleep() 

