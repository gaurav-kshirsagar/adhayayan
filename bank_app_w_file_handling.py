import datetime

balance = 0

def check_balance():
    print("Total balance of your account is:", balance)

def deposite(amt):
    global balance
    balance = balance + amt
    print(amt,"Rs. Deposited!")

def withdraw(amt):
    global balance
    if balance > amt:
        balance = balance - amt
        print(amt,"Rs.Withdrawn!")
    else:
        print("Insufficient Balance")

with open("bankapp_logs.txt","at")as logfile:
    logfile.write(f"\n\n[{datetime.datetime.now()}] BankApp Started")      
    while True:
        ch = int(input("Enter the choice\n1 for Balance Check\t\t2 for Deposite\n3 for Withdraw\t\t4 for Exit:"))
        logfile.write(f"\n[{datetime.datetime.now()}] User have chossen {ch}")

        if ch == 1:
            print("Balance check")
            logfile.write(f"\n[{datetime.datetime.now()}] User performed balance check operation")
            check_balance()
        elif ch == 2:
            print("code of Deposite")
            d_amt = int(input("Enter amount of deposite"))
            logfile.write(f"\n[{datetime.datetime.now()}] User Deposited amount {d_amt}")
            deposite(d_amt)
            check_balance()
        elif ch == 3:
            print("Code of withdrawn")
            w_amt = int(input("Enter withdraw amount"))
            logfile.write(f"\n[{datetime.datetime.now()}] User Withfrawn amount {w_amt}")
            withdraw(w_amt)
            check_balance()
        elif ch == 4:
            print("Application closed..")
            logfile.write(f"\n[{datetime.datetime.now()}] User closed the Application")
            break
        else:
            print("Invalid choice")
            logfile.write(f"\n[{datetime.datetime.now()}] User chossen invalid choice {ch}")
