def menu():
    print("1. Add New Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter name: ")
    for contact in contact_book:
        if contact["name"] == name:
            print("Error: A contact named", name, "already exists.")
            return
            
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contact_book.append(new_contact)
    print("Success: Contact", name, "has been added successfully!!.")

def display_all(contact_book):
    print("Contact List")
    if not contact_book:
        print("Your contact book is empty.")
        return
        
    for index, contact in enumerate(contact_book, start=1):
        print(str(index) + ". Name: " + contact['name'] + " | Phone: " + contact['phone'] + " | Email: " + contact['email'])

def search_contact(contact_book):
    print("Search Contact")
    search_name = input("Enter the name to search for: ")
    
    for contact in contact_book:
        if contact["name"] == search_name:
            print("Contact Found:")
            print("Name: ", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            return
            
    print("No contact found matching", search_name)

def update_contact(contact_book):
    print("Update Contact")
    search_name = input("Enter the name of the contact to update: ")
    
    for contact in contact_book:
        if contact["name"] == search_name:
            print("Modifying values for", contact['name'], "(Leave blank to keep current value):")
            
            new_name = input("New Name: ")
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            
            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
                
            print("Success: Contact updated successfully!")
            return
            
    print("No contact found matching", search_name)

def delete_contact(contact_book):
    print("Delete Contact")
    search_name = input("Enter the name of the contact to delete: ")
    
    for contact in contact_book:
        if contact["name"] == search_name:
            contact_book.remove(contact)
            print("Success: Contact", contact["name"], "has been deleted.")
            return
            
    print("No contact found matching", search_name)

def main():
    contact_book = []
    
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            display_all(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            update_contact(contact_book)
        elif choice == '5':
            delete_contact(contact_book)
        elif choice == '6':
            print("Thank you for using Contact Book. Bye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()



