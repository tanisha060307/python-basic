def main():
    x = get_int()
    print(f"x is {x}")



def get_int():
    while True:
        try:
            x = int(input("what's x?"))
            
        except ValueError: #error handling
            print("x is not an integer")
        else: # for handling the name error

            break
    return x
main()