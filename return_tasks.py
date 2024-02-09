'''
a=int(input("Entyer 1st number : "))
b=int(input("Enter 2nd number :"))
def add():
    c = a+b
    return c

print(add())

def sub():
    c = a-b
    return c
print(sub())


def mul():
    c = a*b
    return c
print(mul())


def div():
    c = a/b
    return c
print(div())


#Bank application 
balance = 0

def check_balance():
    return balance

def deposite(amt):
    global balance
    balance = balance + amt
    return amt

def withdraw(amt):
    global balance
    if balance > amt:
        balance = balance - amt
        return amt
    else:
        print("Insufficient Balance")
    
while True:
    ch = int(input("\n\nEnter the choice\n1 for Balance Check\t\t2 for Deposite\n3 for Withdraw\t\t4 for Exit:"))

    if ch == 1:
        print("Balance check")
        print("Total balance of your account is:",check_balance())
    elif ch == 2:
        print("code of Deposite")
        d_amt = int(input("Enter amount of deposite"))
        print(deposite(d_amt),"Rs.Deposited!")
        print("Updated Balance: ",check_balance())
    elif ch == 3:
        print("Code of withdrawn")
        w_amt = int(input("Enter withdraw amount"))
        print(withdraw(w_amt),"Rs.Withdrawn!")
        print("Updated Balance: ",check_balance())
    elif ch == 4:
        print("Application closed..")
        break
    else:
        print("Invalid choice")
'''
        
# User password login program:
x = input("Enter user name: ")
y = input("Enter your password: ")

data = {'user1':'abc@12','user2':'asd123'}

def show_data():
    return data

def add_user(a,b):
    data[a]= b
    return a

def delete_user(a):
    data.pop(a)
    return a

def delete_all_user():
    data.clear()
    return data

def change_password(a):
    is_present = data.get(a)
    if is_present != None:
        b = input("Enter New Password")
        data[a]= b
        print("Password changed Succssfully!")
    else:
        print("Incorrect Username or User not Exists!")


if x in data:
    print("Login Successfully!")
else:
    print("Incorrect password please try again!")
while True:
    
    ch = int(input("\n1. Show usres data\n2. Add User\n3. Delete User\n4. Delete all Users\n5. Change Password\n6. Exit"))
    
    if ch ==1:
        print(show_data())
    elif ch == 2:
        print("--> Add new user")
        a = input("Enter user name:")
        b = input("Enter password")
        print(add_user(a,b),"Added Succssfully!")
        
        
    elif ch == 3:
        print("-->Delete user")
        a = input("Enter user name which you want to delete:")
        print(delete_user(a),'Deleted!')

    elif ch == 4:
        print("Deleting all users")
        print('ALL users deleted..',delete_all_user())

    elif ch == 5:
        print("Change password")
        a = input("Enter user name :")
        change_password(a)
        
    elif ch == 6:
        print("exit..")
        break
    else:
        print("Invalid Choice")
