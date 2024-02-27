class ContactsManager:
    def __init__(self):
        self.contacts = {}

    def show_all_contacts(self):
        print("--> Show all contacts")
        if len(self.contacts) == 0:
            print("NO Contacts to Show..")
        else:
            print("SRNO\t NAME\t Mob.No")
            count = 1
            for mono, name in self.contacts.items():
                print(count, "\t", name, "\t", mono)
                count += 1

    def add_new_contact(self):
        print("--> Add new contact")
        mono = input("Enter the mob.no to add: ")
        n = self.contacts.get(mono)
        if n is not None:
            print("Contact already exists!")
        else:
            name = input("Enter name to add: ")
            self.contacts[mono] = name
            print("CONTACT ADDED")

    def update_contact(self):
        print("--> Update Contact")
        mono = input("Enter the mob.no to update: ")
        n = self.contacts.get(mono)
        if n is not None:
            name = input("Enter new name to update:")
            self.contacts[mono] = name
            print("CONTACT UPDATED")
        else:
            print("NO Such contact exists with mob.no", mono)

    def delete_contact(self):
        print("--> Delete contact")
        mono = input("Enter the mob.no to delete: ")
        is_present = self.contacts.get(mono)
        if is_present is not None:
            self.contacts.pop(mono)
            print("Contact Deleted!")
        else:
            print("No such contact to delete")

    def delete_all_contacts(self):
        print("--> Delete all contacts")
        self.contacts.clear()
        print("All contacts deleted!")

    def search_contact_by_number(self):
        print("--> Search by mono")
        mono = input("Enter Mob.no to search")
        n = self.contacts.get(mono)
        if n is not None:
            print("Contacts details found, Name: ", n)
        else:
            print("NO such contact exists with mob.no: ", mono)


class Menu(ContactsManager):
    def __init__(self):
        super().__init__()

    def menu_options(self):
        while True:
            ch = int(input("\n\n1. Show all contacts \t2. Add new contacts \n3. Update Contacts\t4. Delete Contact\n5. Delete all contacts\t6. Search Contact by mob.no\n7. Exit"))
            if ch == 1:
                self.show_all_contacts()
            elif ch == 2:
                self.add_new_contact()
            elif ch == 3:
                self.update_contact()
            elif ch == 4:
                self.delete_contact()
            elif ch == 5:
                self.delete_all_contacts()
            elif ch == 6:
                self.search_contact_by_number()
            elif ch == 7:
                print("-->Exit")
                break
            else:
                print("Invalid choice")


menu = Menu()
menu.menu_options()
