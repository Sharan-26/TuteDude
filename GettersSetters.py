# Getters and Setters
#Getters and setters are methods that allow controlled access to an object's attributes.
#They help in validating data, protecting data from accidental modification, and providing controlled access.
class Student():
    def __init__(self, name,age):
        self.__name = name
        self.__age = age
        
    def get_name(self):  #getter
        return self.__name
    
    def set_name(self, name): #setter
        self.__name = name
        
    def get_age(self):
        return self.__age
        
    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("Age should be integer. ERROR , Try Again")
    
s = Student("Chandan", 22)
print(s.get_name())

s.set_name("Sharan")
print(s.get_name())

s.set_age(100)
print(s.get_age())