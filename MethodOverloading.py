class calculator():
    def add(self, a, b, c=0):
        print(a+b+c)
        
c = calculator()
c.add(1,2)
c.add(1,2,3)

#Method Overriding
# class Animal():
#     def make_sound(self):
#         print("animal making sound")
        
# class Dog(Animal):
#     def make_sound(self):#method overrided
#         super().make_sound() # calls parents behaviour also
#         print("Bark")
        
# d = Dog()
# d.make_sound()

#Super() function

class Animals:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print(f"{self.name} makes a sound")
        
class Dog(Animals):
    def __init__(self, name,breed = None):
        super().__init__(name) #calls parent name also
        if breed == None:
            print("Breed not specified")
        else:
            self.breed = breed
        
    def sound(self):
        super().sound() # calls parent class sound also
        print(f"{self.name} barks")
        
dog = Dog("Nymeria")
dog.sound()