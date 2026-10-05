numbers = [10,20,3,40,50]
even = 0
odd = 0
for n in numbers:
    if n%2==0:
        even += 1
    else:
        odd += 1
print("even numbers is ", even)
print("odd numbers is ", odd)