contacts = []


while True:
    print("Contact List Menu:")
    print("1. View Contact")
    print("2. Add Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    
    choice = input("Enter your choice (1,2,3,4): ")
    
    if choice == "1":
        # Display all contacts
        if not contacts:
            print("No contacts available")
        else:
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")
    
    elif choice == "2":
        # Add a new contact
        
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contact = {"name": name, "phone": phone}
        contacts.append(contact)
        print(f"Contact '{name}, {phone}' added to the contact list'\n")
        
    elif choice == "3":
    # Delete a contact
        if not contacts:
         print("No contacts available")
        else:
            print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        
        choice = int(input("Enter the number of the contact you want to delete: "))  
        if 1 <= choice <= len(contacts): 
            deleted_contact = contacts[choice - 1]  
            del contacts[choice - 1]  
            print(f"Contact '{deleted_contact['name']}, {deleted_contact['phone']}' deleted from the contact list\n")
        else:
            print("Invalid choice. Please enter a valid number.")
            
    elif choice == "4":
        # Exit the program
        print("Exiting the program. Goodbye")
        break
    