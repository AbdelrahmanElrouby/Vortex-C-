#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//By: squad-asl

void Draw_Circle(int); // By Abdelrahman Mohamed
void Draw_Square(int) ; // By Danial Adel
void Draw_Triangle(int) ; // By Mohammed Maher
void Draw_Pyramid(int) ; 

int main()
{
    // By Abdelrahman Mohamed
    char shape;
    int h ;
    printf("\t\t\t\tENTER THE SHAPE YOU WANT TO DRAW :\n\t\t\t\t------------------------------------------\n\t\t\t\t");
    printf("Where:\n\t\t\t\t\n\t\t\t\tc --> Circle \t\t s --> Square \n\n\t\t\t\tt --> Right triangle \t p --> Pyramid \n\n") ;
    scanf(" %c",&shape) ;
    if(shape != 'c' && shape != 's' && shape != 't' && shape != 'p' )
    {
        printf("\t\t\t\tERROR!!!\n\t\t\t\tWRONG INPUT\n\n") ;
        return 0 ;
    }
    printf("\t\t\t\tEnter the Maximum height of the shape :") ;
    scanf("%d",&h) ;
    switch(shape)
    {
        case 'c' :
        {
            //Where diameter is the maximum height in a circle , so the radius is half of the maximum height
            Draw_Circle(h/2) ;
            break ;
        }
        case 's' :
        {
            Draw_Square(h) ;
            break ;
        }
        case 't' :
        {
            Draw_Triangle(h) ;
            break ;
        }
        case 'p' :
        {
            Draw_Pyramid(h) ;
            break;
        }
    }
    return 0;
}
void Draw_Circle(int r)
{
    int i,j ;
    int rsq = r*r;
    //I used nested loops with i and j to act as x and y co-ordinates
    printf("\n") ;
    for(i=-r;i<=r;i++)
    {
        int isq = i*i;
        printf("\t\t\t\t\t\t");
        for(j=-r;j<=r;j++)
        {
            int jsq = j*j;
            int dsq = isq + jsq;
            /*since the equation of the circle is x^2 + y^2 = r^2 , I could
            have drawn the circle according to this equation but more points can be drawn
            if we drew the points within a range centered around the r^2 */
            if( dsq > rsq - r && dsq < rsq + r || dsq < rsq )
            {
                printf("**");
            }
            else
            {
                printf("  ");
            }
        }
        printf("\n");
    }
}
void Draw_Square(int l)
{
    int i, j;
    for(i=0 ; i<l ; i++)
    {
        for(j=0 ; j<l ; j++)
        {
            printf("* ") ;
        }
        printf("\n");
    }
}
void Draw_Triangle(int h)
{
    for(int i =0 ; i<h ; i++)
        {
            for(int j = 0 ; j<i+1 ;j++ )
            {
                printf("* ") ;
            }
            printf("\n") ;
        }
}
void Draw_Pyramid(int h)
{
        int i , j ;
        printf("\n") ;
        for(int i =0 ; i<h ; i++)
        {
            printf("\t\t\t\t\t\t"); //To make it centered
            for(int j=h-i-1; j>0 ; j--)
            {
                printf(" ");
            }
            for(int k=((i+1)*2)-1 ; k>0 ; k--)
            {
                printf("*");
            }
            printf("\n");
        }

}

