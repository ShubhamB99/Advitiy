char var, opt;
int b, g, r;

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
    if (var == 'r')                                                   // Was not working when directly using Serial.read() == 'b'
    {
      opt = Serial.read();
      if (opt == 'x')
        Serial.write(10);
      delay(500);
      opt = Serial.read();
      if (var == 'y')
        Serial.write(10);
      delay(500);

      b = Serial.read(); 
      g = Serial.read(); 
      r = Serial.read(); 
      
    }

    if (var == 's')
    {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
    }

  }

  else
  {
     digitalWrite(LED_BUILTIN, LOW);
     Serial.print(" b is ");
     Serial.print(b);
     Serial.print(" g is ");
     Serial.print(g);
     Serial.print(" r is ");
     Serial.print(r);
      

  }

 
  /*
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);  
  */
}
