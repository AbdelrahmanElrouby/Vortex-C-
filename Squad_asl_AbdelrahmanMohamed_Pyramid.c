#include <stdio.h>
#include <stdlib.h>

int main()
{
    int height;
    printf("Please enter the height of the pyramid :") ;
    scanf("%d",&height) ;

    int stars[5] = {1,3,5,7,9} ;
    if(height <2 || height > 5)
    {
        printf("Invalid height") ;
    }
    else
    {
        for(int i =0 ; i<height ; i++)
        {
            for(int j=height-i-1; j>0 ; j--)
            {
                printf(" ");
            }
            for(int k=stars[i] ; k>0 ; k--)
            {
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}
