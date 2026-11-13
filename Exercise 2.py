#building a simple calculator
def add(x,y):
    return x + y
def subtract(x,y):
    return x- y
def multiply(x,y):
    return x * y
def power(x,y):
    return x ** y
def divide(x,y):
    return x/y
print("please select an operation to perform")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. power")
print("5. divide")

while True :
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice not in ('1', '2', '3', '4', '5'):
        print("choose the correct option")
    else:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "**",y, "=", power(x,y))

        elif choice == '5':
            print(x, "/", y, "=", divide(x,y))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
 
add(x,y)
subtract(x,y)
multiply(x,y)
power(x,y)
divide(x,y)
