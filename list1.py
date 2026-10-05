numbers = [10,-7,5,-1,0,13,8,91]
positive = []
negative = []
zero = []
for n in numbers:
    if n>0:
        positive.append(n)
    elif n<0:
        negative.append(n)
    else:
        zero.append(n)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zero numbers:", zero)
