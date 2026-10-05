num = list(map(int, input("enter numbers:").split()))
unique=list(set(num))#removing duplicates
unique.sort()
print("second smallest number is:", unique[1])
