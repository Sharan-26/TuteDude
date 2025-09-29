# abstract - Its a blue print for class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod  #decorator
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self,name):
        #super().start_engine()
        self.name = name
        print(f"{self.name} car engine started")
        
car = Car()
car.start_engine("BMW")