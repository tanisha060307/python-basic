while True:
    try:
        x = int(input("what's x?"))
        
    except ValueError: #error handling
        print("x is not an integer")
    else: # for handling the name error

        break
print(f"x is {x}")