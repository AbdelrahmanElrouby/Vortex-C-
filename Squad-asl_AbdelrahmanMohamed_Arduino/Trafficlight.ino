const int colours[] = {4,5,7} ;
int i = 2 ;
bool j = false ; 
void setup()
{
  pinMode(2,INPUT);
  pinMode(4, OUTPUT) ;
  pinMode(5, OUTPUT) ;
  pinMode(7, OUTPUT) ;
  
}

void loop()
{
    if(digitalRead(2) && !j)
    {
      j = true ; 
    }
  if(j)
    { 
         i++ ;
         delay(50);
         digitalWrite( 4,LOW) ;
       digitalWrite( 5,LOW) ;
       digitalWrite( 7,LOW) ;
         delay(50);
         j = false ; 
    }
    delay(50);
    digitalWrite( colours[i%3] ,HIGH ) ;
    digitalWrite( colours[(i+1)%3] , LOW) ;
    digitalWrite( colours[(i-1)%3],LOW) ;
    delay(50);
      
    
}