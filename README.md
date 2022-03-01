# Remote_Robot
With the help of a bluetooth module I created a code to control robot using hand signs with the help of Python and OpenCV

RobotSendData is the main folder. With the help of the other modules (HandTrack and Serial), I can find my hand, check if there is a hand sign and transfer that data to an Arduino 
with the help of an HC06 bluetooth module.

The SignComands is a folder with all the hand signs that can transfer data to the Arduino


The CV_CONTROL folder has the codes for the robot. Depending on the data that python transfers it executes a command. It also has an SR04 ultrasonic sensor that allow him to avoid the environment around him.
