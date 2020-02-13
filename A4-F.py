#******************************************
#*Programmers: Geff Freire and Kevin Mai *
#*Program 4: A4.py                        *
#*Lab 3                                   *
#*Class: EEE 187L (Group Johnny 5)        *
#*Date: October 22, 2019                  *
#******************************************
#forward function
def forward():
  print('go FWD')
  GPIO.output(out1,GPIO.HIGH)
  GPIO.output(out2,GPIO.LOW)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.HIGH)
  print("forward")

#backward function
def backward():
  print("go REV")
  GPIO.output(out1,GPIO.LOW)
  GPIO.output(out2,GPIO.HIGH)
  GPIO.output(out3,GPIO.HIGH)
  GPIO.output(out4,GPIO.LOW)
  print("backwards")

#stop function
def stop():
  print("stop")
  GPIO.output(out1,GPIO.LOW)
  GPIO.output(out2,GPIO.LOW)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.LOW)
# Turn Left
def left():
  print("go left")
  GPIO.output(out1,GPIO.HIGH)
  GPIO.output(out2,GPIO.LOW)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.LOW)
  print("left")
# Turn Right
def right():
  print("go right")
  GPIO.output(out1,GPIO.LOW)
  GPIO.output(out2,GPIO.HIGH)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.HIGH)
  print("right")

def straight():
  p.start(73)#right (Magic: 74 (p) and 79 (q)))
  q.start(79)

def forwardLeft():
  print("forward left")
  p.start(73)#right (Magic: 74 (p) and 79 (q)))
  q.start(82)

def forwardRight():
  print("forward right")
  p.start(76)
  q.start(79)

#UltraSonic Functions
def ReadL():
	#print ("Reading Left")
	# set Trigger to HIGH
	GPIO.output(L_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(L_TRIGGER, False)
 
	StartTime = time.time()
	StopTime = time.time()
 
    # save StartTime
	while GPIO.input(L_ECHO) == 0:
		StartTime = time.time()
 
    # save time of arrival
	while GPIO.input(L_ECHO) == 1:
		StopTime = time.time()
	#print ("Left Math Time!")
    # time difference between start and arrival
	TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
	L_distance = (TimeElapsed * 34300) / 2
    
	return L_distance
	

def ReadR():
	# set Trigger to HIGH
	GPIO.output(R_TRIGGER, True)
	#print("Reading Right")
    # set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(R_TRIGGER, False)
 
	StartTime = time.time()
	StopTime = time.time()
	 
    # save StartTime
	while GPIO.input(R_ECHO) == 0:
		StartTime = time.time()
    # save time of arrival
	while GPIO.input(R_ECHO) == 1:
		StopTime = time.time()
	#print("Right Math Time!")
    # time difference between start and arrival
	TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
	R_distance = (TimeElapsed * 34300) / 2
	
	return R_distance 

#import
import RPi.GPIO as GPIO          
from time import sleep
import time

#Pin Modes for I2C (for later)
#I2CLK = 2
#I2DAT = 3

#L298 Bridge pin definitions
#Outs are the Ins of the Bridge. 
out1 =20 #right wheel +
out2 = 16 #right wheel -
out3 = 12 #left wheel -
out4 = 7 #left wheel +
enA = 21 #enable 1 & 2
enB = 8  #enable 3 & 4

#QTI Pin Sensor Definitions 
left_sensor = 13 #left QTI
center_sensor = 19 #Center QTI
right_sensor = 26 #right QTI

#UltraSonics Definitions (4)
R_TRIGGER=18
R_ECHO=23
L_ECHO=24
L_TRIGGER=25

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#LN298D Bridge Control Pins
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

#Motor Output Pins 
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)

#Light Sensor Pins 
GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(center_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

#UltraSonic Pin Setups
GPIO.setup(L_TRIGGER, GPIO.OUT)
GPIO.setup(R_TRIGGER, GPIO.OUT)
GPIO.setup(L_ECHO, GPIO.IN)
GPIO.setup(R_ECHO, GPIO.IN)

#PWM Controllers
p=GPIO.PWM(enA,500) #original 500 for both A and B
q=GPIO.PWM(enB,500)



#start function
p.start(64)#right (Magic: 74 (p) and 79 (q)))
q.start(79)#left 
print("hi\n")
#print("The default speed & direction of motor is LOW & Forward.....")
#print("g-go s-stop b-backward f-forward L_left R_right e-exit")
#print("\n")    

straight()
		
#HCSR04 Control Block		

while (1):
	R_dist = ReadR()
	L_dist = ReadL()
	print ("Distance Check! Left = {0:.1f} cm, Right = {1:.1f} cm".format(L_dist, R_dist))
	#print ("Measured Distance on Left Sensor= %.1f cm" % L_dist)
	
	#print ("Measured Distance on Right Sensor= %.1f cm" % R_dist)	

	if (L_dist < R_dist):
		print ("Going Right Around")
		right()
		sleep(.2)
		straight()
		sleep(.2)

	elif (R_dist < L_dist):
		print ("Going Left Around")
		left()
		sleep(.2)
		straight()
		sleep(.2)
	elif (L_dist <=8) and (R_dist <=8):
		stop()
	else:
		straight()

