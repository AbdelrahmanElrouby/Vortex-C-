#define Motor1_1 5
#define Motor1_2 9
#define Motor2_1 10
#define Motor2_2 11
#define Forward_button 3
#define Backward_button 6
#define Right_button 7
#define Left_button 2


void setup() 
{
  pinMode(Motor1_1, OUTPUT);
  pinMode(Motor1_2, OUTPUT);
  pinMode(Motor2_1, OUTPUT);
  pinMode(Motor2_2, OUTPUT);
  pinMode(Forward_button, INPUT_PULLUP);
  pinMode(Backward_button, INPUT_PULLUP);
  pinMode(Right_button, INPUT_PULLUP);
  pinMode(Left_button, INPUT_PULLUP);
}

void loop() 
{
  while(digitalRead(Forward_button))
  {
     moveForward();
  }
  while(digitalRead(Backward_button))
  {
     moveBackward();
  }
  while(digitalRead(Right_button))
  {
     moveRight();
  }
  while(digitalRead(Left_button))
  {
     moveLeft();
  }
     digitalWrite(Motor1_1,LOW);
     digitalWrite(Motor1_2,LOW);
     digitalWrite(Motor2_1,LOW);
     digitalWrite(Motor2_2,LOW);
}

void moveForward()
{
     digitalWrite(Motor1_1,HIGH);
     digitalWrite(Motor1_2,LOW);
     digitalWrite(Motor2_1,HIGH);
     digitalWrite(Motor2_2,LOW);
}
void moveBackward()
{
     digitalWrite(Motor1_1,LOW);
     digitalWrite(Motor1_2,HIGH);
     digitalWrite(Motor2_1,LOW);
     digitalWrite(Motor2_2,HIGH);
}
void moveRight()
{
     digitalWrite(Motor1_1,HIGH);
     digitalWrite(Motor1_2,LOW);
     digitalWrite(Motor2_1,LOW);
     digitalWrite(Motor2_2,HIGH);
}
void moveLeft()
{
     digitalWrite(Motor1_1,LOW);
     digitalWrite(Motor1_2,HIGH);
     digitalWrite(Motor2_1,HIGH);
     digitalWrite(Motor2_2,LOW);
}






