def HangMan(Word) :
    print("\n\tWelcome to Hangman game !!\n\tYou have 8 chances !!")
    Guessed_Word = ""
    for i in range( len(Word) ) : #to show the user how many letters is the word to be guessed
        Guessed_Word += "_"
    print(Guessed_Word + "\n")
    Correct_letters= ""
    i = 8 #Number of chances
    while i > 0 :
        Guessed_letter = input("Guess a letter : ")
        Guessed_Word = ""
        if len(Guessed_letter) !=1 : #To avoid user entering more than one letter at once
            print("\nYou can only one letter at once !!\n")
            continue
        if Guessed_letter in Correct_letters: #To avoid user guessing the same letter twice
            print("\nYou already guessed this letter , Try again !\n")
            continue
        elif Guessed_letter in Word :
            Correct_letters += Guessed_letter #adds all the current guessed correct letters to a string 
            for j in range(len(Word)) : #if the letter guessed is in the word , the game shows the user his progress by printing the word without the unguessed letters
                if Word[j] in Correct_letters :
                    Guessed_Word += Word[j]
                else :
                    Guessed_Word += "_"
            
            if(Guessed_Word == Word) :
                print(Word)
                print("You guessed the correct word !!\nGreat job :)")
                break
            print("Great guess !!!\n")
            print(Guessed_Word + "\n")
        else :
            if i== 0 :
                print("You are out of chances :( \nHard luck next time")
            i -=1 #This means that your chances is decremented
            if i==1 :
                print("\nWrong guess !!\nYou have only 1 chance left !\n") #Just to avoid the grammer mistake :)
            print("\nWrong guess !!\nYou have "+ str(i) + " chances left !\n")       
Word = ("absurd") #Any random word
HangMan(Word)