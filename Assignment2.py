# Task 1: Check if a Number is Even or Odd
num = int(input("Enter a number: "))
for i in range(1,num+1):    
    if num % 2 == 0:
        print(f"{num} is an even number.")
        break
    else:
        print(f"{num} is an odd number.")
        break

    
# # Task 2: Sum of the First 50 Numbers
sum = 0    
for i in range(1,51):
    sum += i
print(f"The sum of the first 50 numbers is: {sum}")