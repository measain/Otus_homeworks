"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 5
    max_cargo = 150

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, ves):
        if self.cargo + ves <= self.max_cargo:
            self.cargo += ves
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

samolet1 = Plane(100)
samolet1.load_cargo(91)

print(samolet1.cargo)
old_cargo1 = samolet1.remove_all_cargo()
print(samolet1.cargo)
print(old_cargo1)
