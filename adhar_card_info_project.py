print("Adhar Card Data-->")
data = {}

def show_data():
    if len(data) == 0:
        print("NO data to Show..")
    else:
        print("SRNO\t NAME\t Adhar.No")
        count = 1
        for number,name in data.items():
            print(count,"\t",name,"\t",number)
            count += 1

def add_data(number):
    n = data.get(number)
    if n != None:
        print("DATA already exists!")
    else:
        name = input("Enter name to add: ")
        data[number]=name
        print("DATA ADDED")

def update_data(number):
    n = data.get(number)
    if n != None:
        name = input("Enter new name to update:")
        data[number]=name
        print("DATA UPDATED")
    else:
        print("NO Such data exists with mob.no",number)

def delete_data(number):
    is_present = data.get(number)
    if is_present != None:
        data.pop(number)
        print("Data Deleted!")
    else:
        print("No such data to delete")

def delete_all_data():
    data.clear()


def search(number):
    n = data.get(number)
    if n != None:
        print("Details found, Name: ",n)
    else:
        print("NO such data exists with mob.no: ", number)
    
        
while True:
    ch = int(input("\n\n1. Show data \t2. Add new adhar details \n3. Update adhar details\t4.Delete data\n5. Delete all data\t6. Search by Adhar.no\n7. Exit"))
    match ch:
        
        case 1:
            print("--> Show all data")
            show_data()
            
        case 2:
            print("-->Add new Details")
            number = input("Enter the Adhar.no to add: ")
            add_data(number)

            
        case 3:
            print("-->Update Adhar")
            number = input("Enter the Adhar.no to update: ")
            update_data(number)

            
        case 4:
            print("--> Delete")
            number = input("Enter the Adhar.no to delete: ")
            delete_data(number)
            
        case 5:
            print("--> Delete all Data")
            print("All contacts deleted!")
            
        case 6:
            print("--> Search by Adhar no")
            number = input("Enter Adhar.no to search")
            search(number)
            
        case 7:
            print("-->Exit")
            break
        case _:
            print("Invalid choice")
        
        
