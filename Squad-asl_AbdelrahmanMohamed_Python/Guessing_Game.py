Secret_Word = "elephant"
print("\nWelcome to the guessing game !\n")
for i in range(3):
    Guess = input("Please guess a word : ")
    if Guess == Secret_Word :
        print("Correct guess!!\nYou Won !!!!\n")
    else :
        print("\nSorry , but you guessed wrong :(")
        if i==2 :
            print("\nYou are out of guesses !\nBetter Luck next time :)\n")
        else :
            print("You have " + str( 2-int(i) ) + " guess(es) left\n")