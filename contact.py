contacts = []

def View_Contacts():
    """
    View all contacts in the contact list.
    """
    if len(contacts) == 0:
        print("No contacts in the contact list")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone_number']}")
            
def add_contact(name, phone_number):
    """
    Add contact to the contact list.
    """
    
    contact = {
        "name": name,
        "phone_number": phone_number
    }
    contacts.append(contact)
    print(f"Contact '{contact['name']}, {contact['phone_number']}' added to the contact list'\n")
            
def delete_contact():
    """
    Delete a contact from the contact list.
    """
    View_Contacts()
    name = input("Enter the name of the contact you want to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted from the contact list'\n")
            break
    else:
        print("Contact not found in the contact list")

while True:
    print("Contact List Menu:")
    print("1. View Contact")
    print("2. Add Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    
    choice = input("Enter your choice (1,2,3,4): ")
    
    if choice == '1':
       View_Contacts()
    elif choice == '2':
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")
        add_contact(name, phone_number)
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        print("Exiting the program.")
        break