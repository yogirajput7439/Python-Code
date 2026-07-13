# ABSTRACTION IN PYTHON

from abc import ABC, abstractmethod

class Vehicle(ABC):

  @abstractmethod
  def start(self):
    pass

class Car(Vehicle):

  def Start(self):

    print("Car Started")

c1 = Car()
c1.start()
  
# example

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print("Animal is eating")

# Derived class
class Dog(Animal):

    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
d.eat()
