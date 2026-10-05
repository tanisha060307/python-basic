numbers = [10,7,5,11,20,13,8,91]
print("prime numbers are:")
for n in numbers: 
    if n<2:
        continue
    prime = True
    for i in range(2,n):
        if n%i==0:
            prime = False
            break
    if prime:
        print(n)