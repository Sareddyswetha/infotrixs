def add_contact(contacts):
    name = input("Enter new contact name: ")
    phone_no = input(f"Enter name's phone no: ")
    contacts[name] = phone_no
    print("New contact added!")


def search_contact(contacts):
    name = input("Enter the name to search for: ")
    if name in contacts:
        for i, j in contacts.items():
            print("Name:", i, "Number:", j)
    else:
        print("Contact not found.")


def edit_contact(contacts):
    name = input("Enter the contact name to edit: ")
    if name in contacts:
        phone_no = input(f"Enter new phone no for name: ")
        contacts[name] = phone_no
        print("Contact information updated!")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found.")


def main():
    contacts = {}
    print("WELCOME\n")
    while True:
        print("Menu\n1. Add new contact\n2. Search contact\n3. Edit contact\n4. Delete contact\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()


   
       

        
