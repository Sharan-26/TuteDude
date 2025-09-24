#Inheritance

# class Family():
#     def __init__(self, surname):
#         self.surname = surname
        
# class Child(Family):
#     def __init__(self, surname,name):
#         super().__init__(surname)
#         self.name = name
        
# child = Child("Gowda","Chandan")
# print(f"{child.name} {child.surname}")

#Real world example
class User():
    def __init__(self,username, password):
        self.username = username
        self.__password = password #pwd protected
        
    def login(self):
        print(f"{self.username} logged in")
        
    # provide a way to access password (optional, 
    # not recommended usually)   
    def get_password(self):
        return self.__password
    
class Admin(User):
    def __init__(self, username, password,name):
        super().__init__(username, password)
        self.name = name
        
admin = Admin("Nymeria", "Alpha","Sharan")
print(f"{admin.username} {admin.get_password} {admin.name}")

# class Notification:
#     def send(self):
#         print(f"Notification sent")

# class EmailNotification(Notification):
#     def send(self):
#         print("Sending Email")

# class SMSNotification(Notification):
#     def send(self):
#         print("Sending SMS")

# notifications = [EmailNotification(), SMSNotification()]
# for notification in notifications:
#     notification.send()

#Polymorphism allows objects of different classes to be treated as objects of a common superclass,
#but they can behave differently depending on the object type.

class Animal():
    
    def make_sound(self):
        print(f"Animal is making sound")
    
class Dog(Animal):
    def make_sound(self):
        print("Bark")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow")
        
animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
    
    