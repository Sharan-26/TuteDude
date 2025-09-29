import math

#Abstraction

# class Vehicle():
#     def __init__(self,start, brake,stop):
#         self.start = start
#         self.brake = brake
#         self.stop = stop
    
#     def vehicleStart(self):
#         print(f"vehicle {self.start}")
        
#     def vehicleBrake(self):
#         print(f"Vehicle {self.brake}")
        
#     def vehicleStop(self):
#             print(f"Vehicle {self.stop}")
    
#     # Create a Vehicle instance and call its methods
# vehicle = Vehicle("Engine started", "Brake applied", "Engine stopped")
# vehicle.vehicleStart()
# vehicle.vehicleBrake()
# vehicle.vehicleStop()

# Encapsulation

class ATM():
    def __init__(self, balance):
        self.__balance = balance #Private Attribute
        
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited {amount}, New balance is {self.__balance}")
        
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn amount is {amount}, new balance is {self.__balance}")
        else:
            print("Insufficient Balance")
 
atm = ATM(1000)  
atm.deposit(300)
atm.withdraw(1200) 
print(" ")

#Abstraction + Encapsulation

class Phone():
    def __init__(self, call_contact, take_picture):
        self.call_contact = call_contact
        self.take_picture = take_picture
        
    def callContact(self):
        print(f"{self.call_contact}")
        
    def takePicture(self):
        print(f"{self.take_picture}")
        
phone = Phone("able to contact", "able to take picture")
phone.callContact()
phone.takePicture()
print(" ")

#Inheritance

class Vehicle():
    def start(self):
        print(f"Bike started")
        
#subclass     
class Bike(Vehicle):
    def ride(self):
        print("Bike is being riden")
        
my_bike = Bike()
my_bike.start()
my_bike.ride()
print(" ")

#Polymorphism

class Shape():
    def calculate_area(self):
        print("Shapes area calculation")
        #raise NotImplementedError("Subclass must implement this method")  
     
#subclass Circle
class circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * (self.radius**2)
    
#subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
shapes = [circle(5), Rectangle(3,4)]
for shape in shapes:
    print(f"Area of shapes are: {shape.calculate_area()}")
    
    

        
            
