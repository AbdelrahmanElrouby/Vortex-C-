#include <stdio.h>
#include <stdlib.h>




int main()
{
    double x , y ; 
    char op ; 
    printf("Please enter the first number :") ; 
    scanf("%lf",&x) ;
    printf("Please enter the operation you want to use :") ; 
    scanf(" %c",&op) ;
    printf("Please enter the second number :") ; 
    scanf("%lf",&y) ;
    switch(op)
    {
        case '+' :
            printf("The sum of the two numbers = %lf",x+y) ;
            break ;
        case '-' :
            printf("The difference between the two numbers = %lf",x-y) ;
            break ;
        case '*' :
            printf("The product of the two numbers = %lf",x*y) ;
           break ;
        case '/' :
            printf("The first number divided by the second number = %lf",x/y) ;
            break ;
        default :
            printf("Invalid operation") ;
        break ;
    }
    return 0;
}
