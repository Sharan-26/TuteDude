# Solid Principles
# 1. Single Responsibility Principle (SRP)
# 2. Open/Closed Principle
# 3. Liskov Substitution Principle (LSP)
# 4. Interface Segregation Principle (ISP)
# 5. Dependency Inversion Principle (DIP)
# 6. Don't Repeat Yourself (DRY) Principle
# 7. Keep It Simple, Stupid (KISS) Principle
# 8. You Aren't Gonna Need It (YAGNI) Principle
class Student:
    def __init__(self,name): # Single Responsibility Principle
        self.name = name # Open/Closed Principle
        
    def database(Student):
        super().__init__()
        print(f"Database connected for {Student.name}")
        
Student = Student("John")
Student.database()
# print(Student.name)

class Discount:  #OCP
    def get_discount(self,price,discount):
        return price - (price * discount / 100) # Don't Repeat Yourself (DRY) Principle
    
class RegularCustomer(Discount):
    def get_discount(self, price, discount):
        return super().get_discount(price, discount)
    
class PremiumCustomer(Discount):
    def get_discount(self, price, discount):
        return super().get_discount(price, discount)
    
regular_customer = RegularCustomer()
premium_customer = PremiumCustomer()
print(regular_customer.get_discount(1000, 10)) # 900.0
print(premium_customer.get_discount(1000, 20)) # 800.0

# Liskov Substitution Principle
# class Bird:  # BAD example
#     def fly(self):
#         pass

# class Sparrow(Bird):
#     def fly(self):
#         return "Sparrow can fly"
    
# class Ostrich(Bird):
#     def fly(self):
#         raise NotImplementedError("Ostrich can't fly")
    
# sparrow = Sparrow()
# print(sparrow.fly())

# ostrich = Ostrich()
# print(ostrich.fly())

#good example

class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        return "Sparrow can fly"
    
class Ostrich(Bird):
    def move(self):
        return "Ostrich can swim"
    
sparrow = Sparrow()
print(sparrow.move())

ostrich = Ostrich()
print(ostrich.move())

# Interface Segregation Principle(ISP)

class Workable:
    def work(self):
        pass
    
class Eatable:
    def eat(self):
        pass
    
class Human(Workable, Eatable):
    def work(self):
        return "Human is working"
    
    def eat(self):
        return "Human is eating"
    
class Robot(Workable):
    def work(self):
        return "Robot is working"
    
    def eat(self):
        raise NotImplementedError("Robot can't eat")

human = Human()
print(human.work(),human.eat())

robot = Robot()
print(robot.work())
#print(robot.eat())

# Dependency Inversion Principle (DIP)
class BackendDeveloper:
    def develop(self):
        return "Backend Developer is developing"
    
class FrontendDeveloper:
    def develop(self):
        return "Frontend Developer is developing"
    
class Project:
    def __init__(self, developer):
        self.developer = developer
        
    def develop(self):
        return self.developer.develop()
    
backend_dev = BackendDeveloper()
frontend_dev = FrontendDeveloper()
project1 = Project(backend_dev) 
project2 = Project(frontend_dev)
print(project1.develop())
print(project2.develop())
