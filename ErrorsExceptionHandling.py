# Errors & Exception Handling
# try,except,else,finally,raise.
import time
 #Error Handling
# try:
#     #x = 10  # Define x before using it
#     print(x)
# except NameError:
#     print("Variable x is not defined.")
#     # Task: Mathematical Operations with Exception Handling
# except Exception as e:
#     print(f"An error occurred: {e}")# Task 1: Mathematical Operations with Exception Handling
while True:
    def Errors(): 
        try:
            a = int(input("Enter a number: ")) # Input from user
            b = int(input("Enter another number: ")) # Input from user
            result = a / b
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e: # Catch any other exceptions
            print(f"An error occurred: {e}") # Task 2: File Handling with Exception Handling
        else:
            print("Division performed successfully.")
        finally: # This block will always execute
            print("Execution completed.")               
    Errors()
    
    

# def Connect():
#     print("Connecting to internet...")
#     time.sleep(3) # Simulate a delay for connection
#     print("Connected")
    
# if __name__ == "__main__":
#     Connect()

# def is_bob(name:str)-> bool: # Check if the name is "Bob" (case insensitive)
#     return name.lower() == "bob"

# def is_an_adult(age: int, has_id: bool) -> bool: # Check if age is 18 or older and has ID
#     return age >= 18 and has_id

# def enter_club(name:str, age:int, has_id:bool)->None: # Main function to determine if a person can enter the club
#     if is_bob(name):
#         print("Welcome Bob! You are allowed to enter the club." )
#         return
    
#     if is_an_adult(age, has_id): # Check if the person is an adult with ID
#         print(f"Welcome {name}! You are allowed to enter the club.")
#     else:
#         print(f"Sorry {name}, you are not allowed to enter the club.")

# def main() ->None: # Test cases
#     enter_club("Alice", 20, True)  # Expected: Allowed
#     enter_club("John", 17, False)   # Expected: Allowed (Bob exception)
#     enter_club("Bob", 16, False)    # Expected: Not Allowed
    
    
# if __name__ == "__main__":
#     main()
    
    
# num = [1,2,3,1]

# def has_duplicates(num):
#     for i in range(len(num)):
#         if num[i] in num[:i]: # Check if the number has appeared before in the list
#             print(f"Duplicate found: {num[i]}") # Print the duplicate number
#             return True  # Return True if a duplicate is found
#     print("No duplicates found.")
    
# has_duplicates(num)
