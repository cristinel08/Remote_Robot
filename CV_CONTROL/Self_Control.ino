void autoControl()    //
{
  long dreapta;
  long stanga;
  IR_Control(0);
  delay(100);
  while (back < 70) {
    IR_Control(2);
  }
  back = 0;
  IR_Control(0);
  leftS(90, 180);
  stanga = ultraSonic();
  Serial.print("Stanga: ");
  Serial.println(stanga);
  rightS(180);
  dreapta = ultraSonic();
  Serial.print("Dreapta ");
  Serial.println(dreapta);
  delay(1000);
  if (dreapta > stanga)
  {
    while (right < 35)
    {
      IR_Control(4);
    }
    right = 0;
    Serial.println("Dreapta");
  }
  else {
    while (left < 65)
    {
      IR_Control(3);
    }
    left = 0;
    Serial.println("Stanga");
  }
  IR_Control(0);
}
