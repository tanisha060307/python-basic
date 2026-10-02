def main():
    x = get_int("What's x?")
    print(f"x is {x}")



def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError: #error handling
            pass #ignore the error and continue the loop
        
main()
#try except pass and else (each have own use case)