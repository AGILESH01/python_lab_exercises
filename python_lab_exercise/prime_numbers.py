def is_prime(n):
    if n<=1:
        print("Enter number above 1")
    for i in range(1,int(n**0.5)+1):
        if n%1==0:
            return False
        return True

while True:
    num=int(input("Enter a number: "))

    if is_prime(num):
        print("This is a prime number")
    else:
        print("This is not a prime number")

    choice = input("Do you want to test another number? (y/n): ").lower()
    if choice != 'y':
        print("Goodbye!")
        break
