from HandTrack import HandTrackModule as htm
from SerialModule import SerialCom
import time
import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 1500)
cap.set(4, 800)
detector = htm.handDetector(numHands=1, trackCon=0.75, detectionCon=0.75)    #apelez constructorul din HandTrackModule
                                                                             #setez prin trackCon cat de sensibila ar fi
                                                                             #urmarirea mainii, iar prin detectionCon
                                                                             #cat de sensibila ar fi detectia unui obiect
                                                                             #de a-l considera o mana

mySerial = SerialCom.serialCom("COM5", 9600, 1)                              #se incearca conectarea la modulul bluetooth

cTime = 0
pTime = 0
pictureH = 150
textH = 170
comandColor = (52, 212, 164)
runTime = False
autoDrive = False

folderPath = "D:\ETTI\Remote_Robot\SignComands"                         #pentru afisarea diferitelor semne pe ecran
                                                                        #in momentul controlului
handSigns = os.listdir(folderPath)
signList = []

for imgPath in handSigns:               #preiau imaginile din folder
    imgSigns = cv2.imread(f'{folderPath}\{imgPath}')
    signList.append(imgSigns)

while True:
    success, img = cap.read()
    img = detector.findHands(img)


    cTime = time.time()             #afisez fps-urile din timpul aplicatiei
    fps = 1 / (cTime - pTime)
    pTime = cTime
    hand = detector.findPosition(img)       #caut pozitia maini din imagine
    if len(hand) != 0:
        fingers = detector.fingersUp()
                                            #verific fiecare comanda
        if fingers == [0, 1, 1, 0, 1]:
            runTime = True
            h, w, c = signList[8].shape
            img[pictureH:h + pictureH, 0:w] = signList[8]
            cv2.putText(img, "Key accepted", (100, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                        (159, 245, 94), 2)
        if fingers == [1, 0, 0, 0, 1]:
            runTime = False
            h, w, c = signList[0].shape
            img[pictureH:h + pictureH, 0:w] = signList[0]
            cv2.putText(img, "Stop send data", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                        2, comandColor, 2)
            if autoDrive==False:
                mySerial.sendDatas([0, 0, 0, 0, 0])

        if runTime:
            try:
                if fingers == [0, 1, 0, 0, 0]:
                    h, w, c = signList[1].shape
                    img[pictureH:h + pictureH, 0:w] = signList[1]
                    cv2.putText(img, "Forward", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                                2, comandColor, 2)
                    autoDrive = False


                if fingers == [0, 1, 1, 0, 0]:
                    h, w, c = signList[2].shape
                    img[pictureH:h + pictureH, 0:w] = signList[2]
                    cv2.putText(img, "Back", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                                2, comandColor, 2)
                    autoDrive = False


                if fingers == [0, 1, 1, 1, 0]:
                    h, w, c = signList[3].shape
                    img[pictureH:h + pictureH, 0:w] = signList[3]
                    cv2.putText(img, "Left", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                                2, comandColor, 2)
                    autoDrive = False


                if fingers == [0, 1, 1, 1, 1]:
                    h, w, c = signList[4].shape
                    img[pictureH:h + pictureH, 0:w] = signList[4]
                    cv2.putText(img, "Right", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                                2, comandColor, 2)
                    autoDrive = False


                if fingers == [0, 1, 0, 0, 1]:
                    h, w, c = signList[6].shape
                    img[pictureH:h + pictureH, 0:w] = signList[6]
                    cv2.putText(img, "Self Control", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                                2, comandColor, 2)
                    autoDrive = True


                if fingers == [0, 0, 0, 0, 0]:
                    h, w, c = signList[7].shape
                    img[pictureH:h + pictureH, 0:w] = signList[7]
                    cv2.putText(img, "Stop", (0, h + textH), cv2.FONT_HERSHEY_PLAIN,
                                2, comandColor, 2)
                    autoDrive = False

                mySerial.sendDatas(fingers)         #trimit comanda in arduino prin modulul bluetooth
            except:
                mySerial.sendDatas([0, 0, 0, 0, 0])
    if runTime == False:
        cv2.putText(img, "Insert the key to continue", (100, 50), cv2.FONT_HERSHEY_PLAIN,
                    2, (159, 245, 94), 2)
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)