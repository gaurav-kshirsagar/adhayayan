print("PROGRAM STARTS")
ch = int(input("Enter any no. from 1 to 7:"))
match ch:
    case 1:
        print("Its a Monday")
    case 2:
        print("Its a Tuesday")
    case 3:
        print("Its a Wednesday")
    case 4:
        print("Its a Thursday")
    case 5:
        print("Its a Friday")
    case 6:
        print("Its a Saturday")
    case 7:
        print("Its a Sunday")
    case _:
        print("Invalid Choice!")