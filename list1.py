numbers = [10,20,3,40,50]
even = 0
odd = 0
for n in numbers:
    if n%2==0:
        even += n
    else:
        odd += n
print("sum of even numbers is ", even)
print("sum of odd numbers is ", odd)