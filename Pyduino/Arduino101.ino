char var;
int flag = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    var = Serial.read();
    if (var == 'b')                                                   // Was not working when directly using Serial.read() == 'b'
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
    }

    if (var == 's')
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(10000);
    }

    if (var == 'p')
    {
      flag = 1;
    }
  }

  else
  {
     digitalWrite(LED_BUILTIN, LOW);
      if (flag == 1)
      {
         Serial.print(var);
         flag = 0;
      }

  }

 
  /*
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);  
  */
}
