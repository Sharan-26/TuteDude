# class Car:
#     # Attributes
#     def __init__(self, brand, model):
#         self.brand = brand #instance  variable
#         self.model = model #instance  variable
        
#     #method
#     def display_info(self):
#         print(f"Car brand: {self.brand}, Mdodel: {self.model}")
        
# class ElectricCar(Car):
#     pass
     
# # object creation for class car
# my_car = Car("Toyota", "Corolla")
# my_car.display_info()
# print(" ")

# my_car = ElectricCar("Tesla","CyberTruck")
# my_car.display_info()
# print(" ")


# class human():
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
        
#     #creating function
#     def greet(self):
#         print(f"Hello, my name is {self.name} and my age is {self.age}")
    
#     #object creation for class Human
    
# human1 = human("Sharan", 27)
# human1.greet()
# print(" ")    

# class Mobile():
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
        
#     def display(self):
#         print(f"The brand is {self.brand} and price is {self.price}")
        
# # object creation

# mobile1 = Mobile("Apple",1000)
# mobile2 = Mobile("Samsung", 1100)  

# mobile1.display()
# mobile2.display() 
# print(" ")

#Student

class Student():
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    def display_info(self):
        print(f"Student name is {self.name} and students marks are {self.marks}")
        
student1 = Student("Anusha", 97)
student1.display_info()

student2 = Student("Pavan", 35)
student2.display_info()