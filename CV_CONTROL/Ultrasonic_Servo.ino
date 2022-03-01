#include<Servo.h>
#define TRIG_PIN A1
#define ECHO_PIN A0
#include "SR04.h"
int pos = 0;
Servo myServo;

long ultraSonic()
{
  SR04 senz = SR04(ECHO_PIN, TRIG_PIN);
  return senz.Distance();
}

void head()
{
  myServo.write(90);
}

void setupServo()
{
  myServo.attach(A2);
  head();
}
void leftS(int index,int degree)          //move head right
{
  for (pos = index; pos < degree; pos += 1)
  {
    myServo.write(pos);
    delay(15);
  }
}
void rightS(int degree)         //move head left
{
  for (pos = degree; pos > -degree; pos--)
  {
    myServo.write(pos);
    delay(15);
  }
}
