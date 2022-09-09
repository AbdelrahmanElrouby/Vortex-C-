#include <stdio.h>
#include <stdlib.h>

double Average(double a ,double b , double c)
{
    return (a+b+c)/3.0 ;
} ;

double Sum(double a ,double b , double c)
{
    return a+b+c ;
};

int main()
{
    double x , y ,z ;
    printf("Please enter the three numbers :") ;
    scanf("%lf %lf %lf",&x,&y,&z) ;
    printf("Average of the three numbers = %lf \nSum of the three numbers = %lf\n",Average(x,y,z),Sum(x,y,z)) ;
    return 0;
}
