void setup() 
{
  Serial.begin(9600);

}

void loop() 
{
  Serial.write("Y");
  delay(1000);
  while(Serial.available()>0)
    {
      if(Serial.available())
      {
        char c=Serial.read();
        if(c=='F')
        {
          //MOTOR MOVES IN ONE DIRECTION
        }
        else if(c=='B')
        {
          //MOTOR MOVES IN OPPOSITE DIRECTION
        }
        else if(c=='S')
        {
          //MOTOR IS STILL
        }
      }
    }
    
}
