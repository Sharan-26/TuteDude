# reason for self and _init__ in class
# if we create a fn inside class it'll be method else function
#The __init__() method in Python is a special method that initializes an object when it’s created.
# It’s called automatically when you create a new instance of a class.

# optional parameters in constructors
# class Book:
#     def __init__(self, title, author="Unknown"):
#         #print(title)
#         self.title = title
#         self.author = author

#     def show_book(self):
#         print(f"Title: {self.title}, Author: {self.author}")

# book1 = Book("Python Programming")
# book2 = Book("Machine Learning", "Andrew Ng")

# book1.show_book()
# book2.show_book()
#Create a Class with a Constructor:
class Movie():
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating
        
    def movieReview(self):
        print(f"{self.title} rating is {self.rating}")
        
movie1 = Movie("Conjuring", 8.7)
movie1.movieReview()
print(" ")
movie2 = Movie("Lokah", 9.1 )
movie2.movieReview()
print(" ")

#Adding Default Parameters:

class Employee():
    def __init__(self, name, designation,salary =30000):
        self.name = name
        self.designation = designation
        self.salary = salary
        
    def empDetails(self):
        print(f"Employee name is {self.name}, his designation is {self.designation} and his is salary is {self.salary}")

Employee1 = Employee("Virat", "Team Lead")
Employee1.empDetails()
Employee2 = Employee("Rohit","Team Lead", 45000)
Employee2.empDetails()
Employee3 = Employee("Rishabh","Vice President",80000)
Employee3.empDetails()


def findDuplicates(arr):
    n = len(arr)
    duplicates = []

    for i in range(n):
        index = abs(arr[i])
        if arr[index] >= 0:
            arr[index] = -arr[index]   # Mark visited
        else:
            duplicates.append(index)   # Already visited → duplicate

    if not duplicates:
        return -1
    return duplicates


# Test Cases
print(findDuplicates([0,3,1,2]))    # Output: -1
print(findDuplicates([2,3,1,2,3]))  # Output: [2,3]
