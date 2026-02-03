from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass

class Bike(Vehicle):
    def speed(self):
        print("Bike speed is 60 km/h")

b = Bike()
b.speed()
