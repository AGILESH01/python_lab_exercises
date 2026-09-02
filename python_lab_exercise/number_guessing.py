import random



while True:
    randomnumber = random.randint(0,10)
    i=1
    print("Guess the number between 0 to 10")
    while i < 8:
        
        try:
            guess = int(input("Enter the guessed number: "))
        
            if guess < randomnumber:
                print("the guess is too low")
            elif guess > randomnumber:
                print("the guess is too high")
            else:
                break
            
            i += 1  
            
        except:
            print("Invalid characters identified. Please recheck the number.")
             
    if randomnumber == guess:
        print("Congratulations!! you have guessed the number!! , \n You guessed the number in "  +  str(i) +  ' guesses! ')
    else:
        print('Nope. The number was ' + str(randomnumber))
            
    while True:
        choice = input("Do you want to continue the game? (yes/no): ")

        if choice == 'yes' or choice == 'y':
            print("Starting a new game...")
            break 
        else:
            print("Thanks for playing!")
            exit()
