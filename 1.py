name = input("Enter your name: ")

match name:
    case "tanisha"|"pappu"|"arman":
        print("DAITM")
    case "dipti":
        print("BESC")
    case _:
        print("Unknown name")