



#define numOfValsRec 5      //numarul de valori din vector
#define digitsPerValRec 1

unsigned char Lpwm_val = 100;
unsigned char Rpwm_val = 100;
int valsRec[numOfValsRec];    //valorile receptionate
int stringLength = numOfValsRec * digitsPerValRec + 1; // numere de tipul $00000
int counter = 0;
bool counterStart = false;
String receivedString;
bool autoDrive = false;

void setup() {
  Serial.begin(9600);
  M_Control_IO_config();
  Set_Speed(Lpwm_val, Rpwm_val);
  setupServo();
  IR_Control(0);
}

void receivedData() {
  while (Serial.available())
  {
    char c = Serial.read();     //preiau primul caracter

    if (c == '$')             //daca este numar
    {
      counterStart = true;
    }
    if (counterStart) {
      if (counter < stringLength) {
        receivedString = String (receivedString + c);     //cream stringul cu fiecare caracter receptat
        counter++;        //adaugam si verificam numarul de elemente din string
      }
      else {
        for (int i = 0; i < numOfValsRec; i++)    //apoi adaugam in vector numerele
        {
          int num = (i * digitsPerValRec) + 1;    //omitem caracterul $
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();  //o metoda de a lua fiecare caracter din string si le convertim in int
          //incepem de la 1 pentru ca pe pozitia 0 este $
        }
        receivedString = "";
        counter = 0;
        counterStart = false;
      }
    }
  }
}



void loop() {

  receivedData();   //asteptam comanda
  long dist = ultraSonic();
  if (dist > 20) {
    if (valsRec[0] == 0){
      if (valsRec[1] == 1 && valsRec[2] == 1 && valsRec[3] == 1 && valsRec[4] == 1) {
        IR_Control(4);
        autoDrive = false;
      }
  
      else if (valsRec[1] == 1 && valsRec[2] == 1 && valsRec[3] == 1 && valsRec[4] == 0) {
        IR_Control(3);
        autoDrive = false;
      }
      else if (valsRec[1] == 1 && valsRec[2] == 1 && valsRec[3] == 0 && valsRec[4] == 0) {
        IR_Control(2);
        autoDrive = false;
      }
      else if (valsRec[1] == 1 && valsRec[4] == 1 && valsRec[2] == 0 && valsRec[3] == 0){
        IR_Control(1);
        autoDrive = true;
      }
      else if (valsRec[1] == 1 && valsRec[2] == 0 && valsRec[3] == 0 && valsRec[4] == 0) {
        IR_Control(1);
        autoDrive = false;
      }
  
      else {
        IR_Control(0);
      }
    }
  }
  else {
    autoControl();
    if (autoDrive == false){
    for (int i = 0; i < 5; i++)
    {
      valsRec[i] = 0;
    }
  }
    leftS(-180,90);
    IR_Control(0);
  }
}
