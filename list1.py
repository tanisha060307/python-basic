num = list(map(int,input("enter numbers: ").split()))
element = int(input("enter element to search: "))
if element in num:
    print("element exists") 
else:
    print("element does not exist")      