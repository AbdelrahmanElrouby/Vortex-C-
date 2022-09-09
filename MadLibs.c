#include <stdio.h>
#include <stdlib.h>
int main()
{
    char Color[20] ;
    char PluralNoun[20] ;
    char Celebrity[20] ;
    printf("Please enter a color :") ;
    scanf("%s",Color) ;
    printf("Please enter a Plural Noun :") ;
    scanf("%s",PluralNoun) ;
    printf("Please enter a Celebrity's name :") ;
    scanf("%s",Celebrity) ;
    printf("Rose are %s\n%s are blue\nI love %s\n",Color,PluralNoun,Celebrity) ;
    return 0;
}
