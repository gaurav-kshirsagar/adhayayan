x = input("Enter user name: ")
y = input("Enter your password: ")

data = {'user1':'abc@12','user2':'asd123'}

def show_data():
    print(data)

def add_user(a,b):
    data[a]= b
    print(a,"Added Succssfully!")

def delete_user(a):
    data.pop(a)
    print(a,'Deleted!')

def delete_all_user():
    data.clear()
    print('ALL users deleted..',data)

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
        show_data()
    elif ch == 2:
        print("--> Add new user")
        a = input("Enter user name:")
        b = input("Enter password")
        add_user(a,b)
        
        
    elif ch == 3:
        print("-->Delete user")
        a = input("Enter user name which you want to delete:")
        delete_user(a)

    elif ch == 4:
        print("Deleting all users")
        delete_all_user()

    elif ch == 5:
        print("Change password")
        a = input("Enter user name :")
        change_password(a)
        
    elif ch == 6:
        print("exit..")
        break
    else:
        print("Invalid Choice")