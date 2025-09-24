class Mathematical_Operations:
    def __init__(self):
        try:
            self.a = float(input("Enter the first number: "))
            self.b = float(input("Enter the second number: "))
            print(f"You entered: num1 = {self.a}, num2 = {self.b}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            self.a = 0.0
            self.b = 0.0

    def Addition(self):
        addition = self.a + self.b
        print("Addition is:")
        return addition

    def Subtraction(self):
        subtraction = self.a - self.b
        print("Subtraction is:")
        return subtraction

    def Multiplication(self):
        multiplication = self.a * self.b
        print("Multiplication is:")
        return multiplication

    def Division(self):
        if self.b == 0:
            print("Cannot divide by zero.")
            return None
        division = self.a / self.b
        print("Division is:")
        return division
    
# Example usage
math_ops = Mathematical_Operations()
print(math_ops.Addition())
print(math_ops.Subtraction())
print(math_ops.Multiplication())
print(math_ops.Division())

# Second

# Task 2: Personalized Greeting

# Step 1: Take first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Concatenate into a full name
full_name = first_name + " " + last_name

# Step 3: Print personalized greeting
print(f"\nHello, {full_name}! Welcome to the Python program.")





