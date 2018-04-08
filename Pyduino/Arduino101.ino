char var, opt;
int b, g, r;
int flag=0;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  /*while (1){
        Serial.print(20, DEC);
        delay(100);
  }*/

  if (flag==0){
    Serial.print(20, DEC);
    flag=1;
}
Serial.print(40, DEC);
  if (Serial.available() > 0)
  {
     if (flag==0){
        Serial.write("20");
        flag=1;
    }
Serial.write("40");
    
  }
    /*while (1)
        Serial.write('a');
    var = Serial.read();
    if (var == 'r')                                                   // Was not working when directly using Serial.read() == 'b'
    {
      //Serial.print(10, DEC);
      //Serial.print(10, DEC);
      delay(15);
      while (1)
          Serial.write('a');
      //b = Serial.read(); 
      //g = Serial.read(); 
      //r = Serial.read(); 
      
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
*/
 
  /*
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);  
  */
}
