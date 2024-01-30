contacts = {}
while True:
    ch = int(input("\n\n1. Show all contacts \t2. Add new contacts \n3. Update Contacts\t4.Delete Contact\n5. Delete all contacts\t6. Search Contact by mob.no\n7. Exit"))
    if ch == 1:
        print("--> Show all contacts")
        print(contacts)
        if len(contacts) == 0:
            print("NO Contacts to Show..")
        else:
            print("SRNO\t NAME\t Mob.No")
            count = 1
            for mono,name in contacts.items():
                print(count,"\t",name,"\t",mono)
                count += 1
    elif ch == 2:
        print("-->Add new contact")
        mono = input("Enter the mob.no to add: ")
        n = contacts.get(mono)
        if n != None:
            print("Contact already exists!")
        else:
            name = input("Enter name to add: ")
            contacts[mono]=name
            print("CONTACT ADDED")
    elif ch == 3:
        print("-->Update Contact")
        mono = input("Enter the mob.no to update: ")
        n = contacts.get(mono)
        if n != None:
            name = input("Enter new name to update:")
            contacts[mono]=name
            print("CONTACT UPDATED")
        else:
            print("NO Such contact exists with mob.no",mono)
    elif ch == 4:
        print("--> Delete contact")
        mono = input("Enter the mob.no to delete: ")
        is_present = contacts.get(mono)
        if is_present != None:
            contacts.pop(mono)
            print("Contact Deleted!")
        else:
            print("No such contact to delete")
    elif ch == 5:
        print("--> Delete all contact")
        contacts.clear()
        print("All contacts deleted!")
    elif ch == 6:
        print("--> Search by mono")
        mono = input("Enter Mob.no to search")
        n = contacts.get(mono)
        if n != None:
            print("Conttacts details found, Name: ",n)
        else:
            print("NO such contact exists with mob.no: ", mono)
    elif ch == 7:
        print("-->Exit")
        break
    else:
        print("Invalid choice")
        
        