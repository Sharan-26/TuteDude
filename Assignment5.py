# Task 1: Create a Dictionary of Student Marks

my_dict = {'Alice': 85, 'Judy':90, 'Bob':70}

Students = input(f"Enter the students name: ")

if Students in my_dict:
    print(f"{Students}'s marks: {my_dict[Students]}")
else:
    print('Student not found')
    
    
#Task 2: Demonstrate List Slicing 

Original_list = list(range(1,11))

first_five = Original_list[0:5]

reversed_elements = first_five[::-1]

print(Original_list)
print(first_five)
print(reversed_elements)
