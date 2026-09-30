try:

    x = int(input("what's x?"))
    print(f"x is {x}")
except ValueError: #error handling
    print("x is not an integer")