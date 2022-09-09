#include <stdio.h>
#include <stdlib.h>
int main()
{
    int True_Number = 7 ;
    int Guessed_Number ;
    int i ; 
    for(i = 0 ; i< 3 ; i++)
    {
        printf("Please enter a number :") ;
        scanf("%d",&Guessed_Number) ;
        if(Guessed_Number == True_Number)
        {
            printf("Correct Guess! \nYou Won!") ;
            break ;
        }
    }
    if(i==3)
    {
        printf("You ran out of guesses :(\nHard luck next time ") ;
    }

    return 0;
}
