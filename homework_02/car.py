"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle

class Car(Vehicle):
    engine = None

    def set_engine(self, engine):
        self.engine = engine
