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
    
while True:
    ch = int(input("Enter the choice\n1 for Balance Check\t\t2 for Deposite\n3 for Withdraw\t\t4 for Exit:"))

    if ch == 1:
        print("Balance check")
        check_balance()
    elif ch == 2:
        print("code of Deposite")
        d_amt = int(input("Enter amount of deposite"))
        deposite(d_amt)
        check_balance()
    elif ch == 3:
        print("Code of withdrawn")
        w_amt = int(input("Enter withdraw amount"))
        withdraw(w_amt)
        check_balance()
    elif ch == 4:
        print("Application closed..")
        break
    else:
        print("Invalid choice")



