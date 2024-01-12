from cal_prj1 import add,sub,mul,div

while True:
    ch = int(input("Enter the choice: \n1 for Addition\n2 for substraction\n3 for Multiplication\n4 for Divison\n5 for Exit: "))
    if ch == 1:
        print("Addition")
        fn = int(input("Enter first number: "))
        sn = int(input("Enter second number: "))
        add(fn,sn)
    elif ch == 2:
        print("Substraction")
        fn = int(input("Enter first number: "))
        sn = int(input("Enter second number: "))
        sub(fn,sn)
    elif ch == 3:
        print("Multiplication")
        fn = int(input("Enter first number: "))
        sn = int(input("Enter second number: "))
        mul(fn,sn)
    elif ch == 4:
        print("Division")
        fn = int(input("Enter first number: "))
        sn = int(input("Enter second number: "))
        div(fn,sn)
    elif ch == 5:
        print("Calculaor closed..")
        break
    else:
        print("Invalid Choice")