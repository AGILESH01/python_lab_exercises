
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"name": book, "issued": False})
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\n--- LIBRARY BOOKS ---")
            for book in self.books:
                status = "Issued" if book["issued"] else "Available"
                print(book["name"], "-", status)

    def issue_book(self, name):
        for book in self.books:
            if book["name"].lower() == name.lower():
                if not book["issued"]:
                    book["issued"] = True
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return
        print("Book not found!")

    def return_book(self, name):
        for book in self.books:
            if book["name"].lower() == name.lower():
                if book["issued"]:
                    book["issued"] = False
                    print("Book returned successfully!")
                else:
                    print("This book was not issued!")
                return
        print("Book not found!")


library = Library()

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        name = input("Enter book name to issue: ")
        library.issue_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == "5":
        print("Thank you for using the library!")
        break

    else:
        print("Invalid choice! Try again.")
