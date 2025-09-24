def Menu():
    print("Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
while True:
    Menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice in ['1','2','3','4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Enter numeric values.")
            continue
        
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed !")
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def display_menu():
#     print("Simple Calculator")
#     print("1.Add")
#     print("2.Sub")
#     print("3.Multiply")
#     print("4.Exit")
    
# while(True):
#     display_menu()
#     choice = int(input("Enter the choice: "))

#     if choice in {1,2,3}:    
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))

#     for i in range(1,5):
#         if choice == 1:
#             print(add(a,b))
#             break
#         elif choice == 2:
#             print(sub(a,b))
#             break
#         elif choice ==3:
#             print(mul(a,b))
#             break
#         elif choice ==4:
#             print("Exit")
#             break
#         else:
#             print("Try Again")
#             break
    

    