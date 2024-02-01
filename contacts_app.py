#Conttact application

contacts = {9921:'abc',9922:'bcd',9923:'efg'}


'''
print(contacts[9921])
print(contacts.get(9925))

#print(contacts)
1

#Add contact:
#contacts[9924]='jkl'
print('Contactt Added!')
print(contacts)

#Delete contact:
contacts.pop(9923)
print('Contact Deleted!')
print(contacts)

#Delete all contacts:
contacts.clear()
print('contacts:',contacts)
'''

while True:
    ch = int(input("\n1. Show Contacts\n2. Add Contact\n3. Delete Contact\n4. Delete all contacts\n5. Update Contact\n6. Exit"))

    if ch == 1:
        if len(contacts) == 0:
            print('NO CONTACTS To SHOW')
        else:
            print(contacts)
    elif ch == 2:
        while True:
            mob = input("Enter the mobile number 10-digit")
            name = input("Enter the name")
            if len(mob) != 10 or  (mob) in contacts:
                print("Invalid mobile number. Please enter a 10-digit number. Or Mob.No already exist")
                break        
            else:
                contacts[mob]= name
                print('Contact Added!')
                print(contacts)
                break
    elif ch == 3:
        mob = int(input("Enter the mobile number which you want to delete"))
        is_present = contacts.get(mob)
        #print("is_present=",is_present)
        if is_present != None:
            contacts.pop(mob)
            print('Contact Deleted!')
            print(contacts)
        else:
            print("No Such contact to delete")
    elif ch == 4:
        contacts.clear()
        print('contacts:',contacts)
    elif ch == 5:
        mob = int(input("Enter the mobile number of the contact to update: "))
        if mob in contacts:
            new_name = input("Enter the new name: ")
            contacts[mob] = new_name
            print('Contact Updated!')
            print(contacts)
        else:
            print("No such contact to update")
    elif ch == 6:
        print("Exit")
        break
    else:
        print("Invalid choice")
    
    
    
