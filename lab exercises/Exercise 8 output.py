Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: a
No contact found matching a
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Enter name: abd
Enter phone number: 4321
Enter email address: abd@yahoo
Success: Contact abd has been added successfully!!.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 2
Contact List
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 114, in <module>
    main()
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 100, in main
    display_all(contact_book)
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 36, in display_all
    print(index + ". Name: " + contact['name'] + " | Phone: " + contact['phone'] + " | Email: " + contact['email'])
TypeError: unsupported operand type(s) for +: 'int' and 'str'

============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: a
No contact found matching a
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: abd
No contact found matching abd
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 5
Delete Contact
Enter the name of the contact to delete: abd
No contact found matching abd
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 
============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 4
Invalid choice! Please enter a number between 1 and 6.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Invalid choice! Please enter a number between 1 and 6.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 2
Invalid choice! Please enter a number between 1 and 6.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 
============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Enter name: abd
Enter phone number: 1234
Enter email address: 123@asd
Success: Contact abd has been added successfully!!.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 2
Contact List
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 115, in <module>
    main()
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 101, in main
    display_all(contact_book)
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 36, in display_all
    print(index + ". Name: " + contact['name'] + " | Phone: " + contact['phone'] + " | Email: " + contact['email'])
TypeError: unsupported operand type(s) for +: 'int' and 'str'

============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Enter name: abc
Enter phone number: 123
Enter email address: abc@gmail.com
Success: Contact abc has been added successfully!!.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 2
Contact List
1. Name: abc | Phone: 123 | Email: abc@gmail.com
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: abc
Contact Found:
Name:  abc
Phone: 123
Email: abc@gmail.com
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 4
Update Contact
Enter the name of the contact to update: abc
Modifying values for abc (Leave blank to keep current value):
New Name: abcd
New Phone: 12345
New Email: abcd@yahoo.com
Success: Contact updated successfully!
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 5
Delete Contact
Enter the name of the contact to delete: abc
No contact found matching abc
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): abds
Invalid choice! Please enter a number between 1 and 6.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): abcd
Invalid choice! Please enter a number between 1 and 6.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 6
Thank you for using Contact Book. Bye!

============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 5
Delete Contact
Enter the name of the contact to delete: abcd
No contact found matching abcd
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 
============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Enter name: john
Enter phone number: 5
Enter email address: 5
Success: Contact john has been added successfully!!.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 5
Delete Contact
Enter the name of the contact to delete: john
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 116, in <module>
    main()
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 108, in main
    delete_contact(contact_book)
  File "/Users/agil/Desktop/python_lab_exercise/contacts.py", line 87, in delete_contact
    print("Success: Contact", contact_book[0]["name"], "has been deleted.")
IndexError: list index out of range

============================================= RESTART: /Users/agil/Desktop/python_lab_exercise/contacts.py =============================================
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Enter name: abcd
Enter phone number: 1234
Enter email address: 123@abc
Success: Contact abcd has been added successfully!!.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 2
Contact List
1. Name: abcd | Phone: 1234 | Email: 123@abc
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: abc
No contact found matching abc
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: abcd
Contact Found:
Name:  abcd
Phone: 1234
Email: 123@abc
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 4
Update Contact
Enter the name of the contact to update: abc
No contact found matching abc
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 3
Search Contact
Enter the name to search for: abcd
Contact Found:
Name:  abcd
Phone: 1234
Email: 123@abc
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 4
Update Contact
Enter the name of the contact to update: abcd
Modifying values for abcd (Leave blank to keep current value):
New Name: abc
New Phone: 123
New Email: 123@abc
Success: Contact updated successfully!
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 5
Delete Contact
Enter the name of the contact to delete: abc
Success: Contact abc has been deleted.
1. Add New Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 6
Thank you for using Contact Book. Bye!
