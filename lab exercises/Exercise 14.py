
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Current Balance: Rs.", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            account.deposit(amount)
        else:
            print("Enter a valid amount!")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0:
            account.withdraw(amount)
        else:
            print("Enter a valid amount!")

    elif choice == "3":
        account.display()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")
