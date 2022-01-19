from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight = 900
    started = False
    fuel = 100
    fuel_consumption = 1
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel != 0:
                self.started = True
            else:
                raise LowFuelError
    def move(self, km):
        if self.fuel >= km:
            self.fuel = self.fuel - km
        else:
            raise NotEnoughFuel
