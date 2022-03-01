import serial
import time
import logging


class serialCom:

    # Preiau acces pentru a trasnmite date catre Serial Device

    def __init__(self, portNo="COM3", baudRate=9600, digits=1):

        self.portNo = portNo
        self.baudRate = baudRate
        self.digits = digits
        try:  # In cazul in care reuseste sa se conecteze
            self.ser = serial.Serial(self.portNo, self.baudRate)
            print("S-a conectat")
        except:  # Sa mi afiseze acest mesaj
            logging.warning("Nu s-a conectat")

    def sendDatas(self, data):
        # Trimitem valori catre Serial Device

        myString = '$'  # deoarece valorile mereu incep cu '$'
        for d in data:
            myString += str(int(d)).zfill(self.digits)
        try:
            self.ser.write(myString.encode())
            return True
        except:
            return False


def main():
    mySerial = serialCom("COM3", 9600, 1)
    while True:
        mySerial.sendDatas([1, 1, 1, 1, 1])
        time.sleep(2)
        mySerial.sendDatas([0, 0, 0, 0, 0])
        time.sleep(2)


if __name__ == '__main__':
    main()
