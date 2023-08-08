def add_contact(contact,name,phone):
    contact[name] = phone
    print(f"{name} is added to contact")
def search_contact(contact):
    for i,j in contact.items():
        print('Name:',i,'Number:',j)
def update_contact(contact):
    name = input('Enter the contact to be Edited')
    if name in contact:
        phone = input('Enter the new number')
        contact[name] = phone
        print('contact updated')
        search_contact(contact)
    else:
        print('The name is not found')
def delete_contact(contact, name):
    if name in contact:
        del contact[name]
        print(f"{name} has been deleted from contact")
    else:
        print(f"{name} not found in contact")
def list_contact(contact):
    if not contact:
        print("No contact found")
    else:
        print("Contact")
        for name, contact in contact.items():
            print('Name:', name, '\tNumber:', contact)
def save_contact(contact, filename):
    with open(filename, 'w') as file:
        for name, contact in contact.items():
            file.write(f"{name},{contact}\n")
def load_contact(filename):
    contact = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, phone = line.strip().split(',')
                contact[name] = phone
    except FileNotFoundError:
        pass
    return contact
def main():
    filename = "contact.txt"
    contacts = load_contact(filename)
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5):")
        if choice == '1':
            name = input("Enter the name of the contact:")
            phone = input("Enter the phone number:")
            add_contact(contacts, name, phone)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            Search_contact = input('enter the name')
            if Search_contact in contacts:
                print('Name :', Search_contact, '\nContact number:', contacts[Search_contact])
            else:
                print('The name is not found in contact book')
        elif choice == '4':
            name = input("Enter the name: ")
            delete_contact(contacts, name)
        elif choice == '5':
            save_contact(contacts, filename)
            print("Contact saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
        main()