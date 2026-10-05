numbers = [10,10,30,50,60,80]
unique=[]
for n in numbers:
    if n not in unique:
        unique.append(n)
print("oroginal list:",numbers)
print("list after removing duplicates:",unique)

