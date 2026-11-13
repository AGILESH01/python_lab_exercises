def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
while True:
    while True:
        num=int(input("Enter a number: "))
        try:
            check = int(num)
        
            if num < 0:
                print("only positive numbers are allowed")
                continue
            else:
            
                print("The factorial of " , num , " is ",  factorial(num))
            break
        except:
            print("invalid input!" , check) 
        
            
    choice = input("Do you want to test another series? (y/n): ")
    if choice != 'y':
        print("Goodbye!")
        break
