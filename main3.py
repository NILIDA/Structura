from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def type_of_vehicle(self):
        pass

class Car(Vehicle):
    def speed(self):
        return '100 км/ч'

    def type_of_vehicle(self):
        return 'Автомобиль'

class Bike(Vehicle):
    def speed(self):
        return '20 км/ч'

    def type_of_vehicle(self):
        return 'Велосипед'

car = Car()
print(car.type_of_vehicle())
print(car.speed())

bike = Bike()
print(bike.type_of_vehicle())
print(bike.speed())
