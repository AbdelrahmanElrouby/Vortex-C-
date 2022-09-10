#include <stdio.h>
#include <stdlib.h>

int main()
{
    int height; 
    printf("Please enter the height of the pyramid :") ;
    scanf("%d",&height) ;
    if(height <2 || height > 5) 
    {
        printf("Invalid height") ;
    }
    else 
    {
        for(int i =0 ; i<height ; i++)
        {
            for(int j = 0 ; j<i+1 ;j++ )
            {
                printf("*") ;
            }
            printf("\n") ;
        }
    }
    return 0;
}
