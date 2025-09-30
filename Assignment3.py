# Task 1: Calculate Factorial Using a Function 
num = int(input("Enter a number: "))

def factorial(num):
    if num >=0 and num<2:
        return 1
    else:
        return num * (factorial(num-1))
    
fact = factorial(num)
print(f'Factorial of {num} is: {fact}')

# Task 2: Using the Math Module for Calculations
import math 

num = float(input('Enter a number:'))

Square_root = math.sqrt(num)
Logarithm = math.log(num)
Sine = math.sin(num)

print(f'Square_root: {Square_root}')
print(f'Logarithm: {Logarithm}')
print(f'Sine: {Sine}')

