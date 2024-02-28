import datetime

def add(a ,b):
    ans = a + b
    print("Addition is: ",ans)

def sub(a ,b):
    ans = a - b
    print("substraction of a and b is: ",ans)

def mul(a ,b):
    ans = a * b
    print("Multiplication of a and b is: ",ans)

def div(a ,b):
    ans = a / b
    print("Division of a and b is: ",ans)

with open("calcproject_logs.txt","at") as logfile:
    logfile.write(f"\n\n[{datetime.datetime.now()}]: Calculator Started.")
    
    while True:
        ch = int(input("Enter the choice: \n1 for Addition\n2 for substraction\n3 for Multiplication\n4 for Divison\n5 for Exit: "))
        logfile.write(f"\n\n[{datetime.datetime.now()}]: User have  chosen no. {ch} ")

        if ch == 1:
            print("Addition")
            fn = int(input("Enter first number: "))
            sn = int(input("Enter second number: "))
            logfile.write(f"\n[{datetime.datetime.now()}]: User have performed the addition of {fn} {sn} ")
            add(fn,sn)
        elif ch == 2:
            print("Substraction")
            fn = int(input("Enter first number: "))
            sn = int(input("Enter second number: "))
            logfile.write(f"\n[{datetime.datetime.now()}]: User have performed the substraction of {fn} {sn} ")
            sub(fn,sn)
        elif ch == 3:
            print("Multiplication")
            fn = int(input("Enter first number: "))
            sn = int(input("Enter second number: "))
            logfile.write(f"\n[{datetime.datetime.now()}]: User have performed the multipllication of {fn} {sn} ")
            mul(fn,sn)
        elif ch == 4:
            print("Division")
            fn = int(input("Enter first number: "))
            sn = int(input("Enter second number: "))
            logfile.write(f"\n[{datetime.datetime.now()}]: User have performed the division of {fn} {sn} ")
            div(fn,sn)
        elif ch == 5:
            print("Calculaor closed..")
            logfile.write(f"\n[{datetime.datetime.now()}]: User have closed the calculator ")
            break
        else:
            print("Invalid Choice")
            logfile.write(f"\n[{datetime.datetime.now()}]: User have chosen choice: {ch} ")
