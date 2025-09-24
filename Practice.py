a = [1,2,2,3,4,4]
# b = []
# b = list(a)
unique = []
for x in a:
    if x not in unique:
        unique.append(x)
print(unique)



