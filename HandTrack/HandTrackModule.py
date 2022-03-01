import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, numHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode         #cream un obiect ce are aceasta variabila de la utilizator
        self.numHands = numHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        self.mpHands = mp.solutions.hands  # o initializare inainte de a folosi acest modul

        self.hands = self.mpHands.Hands(self.mode, self.numHands,           # apelez constructorul din mediapipe
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils            #folosit pentru a desena cele 21 de puncte

        self.tipFingers = [4, 8, 12, 16, 20]
        self.position = []


    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        #trb sa o convertim intr-o imagine RGB pentru "hands"
                                                             #acesta lucreaza doar in RGB

        self.results = self.hands.process(imgRGB)

    #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:                   #daca detectez mana
            for self.eachHand in self.results.multi_hand_landmarks:     #pentru fiecare mana

                if draw:                                    #desenez cele 21 de puncte + linii dintre ele
                    self.mpDraw.draw_landmarks(img, self.eachHand, self.mpHands.HAND_CONNECTIONS)


        return img


    def findPosition(self, img, handNo = 0, draw = True):

        self.position = []
        if self.results.multi_hand_landmarks:                   #daca detectez mana
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):           #pentru fiecare punct preiau
                                                                #pozitiile sale si le adaug in lista
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.position.append([id, cx, cy])
                if draw and id == 0:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return self.position

    def fingersUp(self):

        if self.results.multi_hand_landmarks:
            myHand = self.handType()        #in functie de mana
            fingers = []

            #Degetul mare
            if myHand == "Right":
                if self.position[self.tipFingers[0]][1] > self.position[self.tipFingers[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if self.position[self.tipFingers[0]][1] < self.position[self.tipFingers[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            #celelalte 4 degete
            for finger in range(1, 5):
                if self.position[self.tipFingers[finger]][2] < self.position[self.tipFingers[finger] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            return fingers


    def handType(self):                                     #verificam ce mana se arata in fata ecranului

        if self.results.multi_hand_landmarks:
            if self.position[17][1] < self.position[5][1]:
                return "Right"
            else:
                return "Left"
def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        position = detector.findPosition(img)
        #if len(position) != 0:
         #   print(position[4])                      # desenez punctul din baza mainii
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 255, 0), 2)
        print(detector.fingersUp())
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__=="__main__":
    main()

