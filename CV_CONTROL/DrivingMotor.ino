#define Lpwm_pin  5     //pinurile cu viteza
#define Rpwm_pin  6    
int pinLB = 2;         // pin2 stanga in spate
int pinLF = 4;         // pin4 stanga in fata
int pinRB = 7;         // pin7 dreapta in spate
int pinRF = 8;         // pin8 dreapta in fata
int back = 0;
int left = 0;
int right = 0;
void M_Control_IO_config(void)
{
  pinMode(pinLB, OUTPUT); // pin2
  pinMode(pinLF, OUTPUT); // pin4
  pinMode(pinRB, OUTPUT); // pin7
  pinMode(pinRF, OUTPUT); // pin8
  pinMode(Lpwm_pin, OUTPUT); // pin5 (PWM)
  pinMode(Rpwm_pin, OUTPUT); // pin6 (PWM)
}
void Set_Speed(unsigned char Left, unsigned char Right)
{
  analogWrite(Lpwm_pin, Left);
  analogWrite(Rpwm_pin, Right);
}
void advance()     // inainte
{
  digitalWrite(pinRB, HIGH); //Motorul din dreapta inainte
  digitalWrite(pinRF, LOW);
  digitalWrite(pinLB, HIGH); //Motorul din stanga inainte
  digitalWrite(pinLF, LOW);
}
void turnR()        //dreapta
{
  digitalWrite(pinRB, LOW); //Motorul din dreapta merge inainte
  digitalWrite(pinRF, HIGH);
  digitalWrite(pinLB, HIGH);
  digitalWrite(pinLF, LOW); //Motorul din stanga inapoi
  right++;
}
void turnL()        //stanga
{
  digitalWrite(pinRB, HIGH);
  digitalWrite(pinRF, LOW );  //Motorul din dreapta merge inapoi
  digitalWrite(pinLB, LOW);  //Motorul din stanga inainte
  digitalWrite(pinLF, HIGH);
  left++;
}
void stopp()         //stop
{
  digitalWrite(pinRB, HIGH);
  digitalWrite(pinRF, HIGH);
  digitalWrite(pinLB, HIGH);
  digitalWrite(pinLF, HIGH);
}
void Tback()          //inapoi
{

  digitalWrite(pinRB, LOW); // Motorul din dreapta merge inapoi
  digitalWrite(pinRF, HIGH);
  digitalWrite(pinLB, LOW); //Motorul din stanga merge inapoi
  digitalWrite(pinLF, HIGH);
  back++;
}
void IR_Control(int a)      //Panoul de Comanda
{
  if (a == 1)
  {
    advance();
    Serial.println("Inainte");
  }
  if (a == 2)
  {
    Tback();
    Serial.println("Inapoi");
  }
  if (a == 3)
  {
    turnL();
    Serial.println("Stanga");
  }
  if (a == 4)
  {
    turnR();
    Serial.println("Face dreapta");
  }
  if (a == 0)
  {
    stopp();
    //Serial.println("Stop");

  }
}
