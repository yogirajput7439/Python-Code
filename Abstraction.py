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
  
