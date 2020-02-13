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
#Turn Left  
def left():
  print("go left")
  GPIO.output(out1,GPIO.HIGH)
  GPIO.output(out2,GPIO.LOW)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.LOW)
  print("left")
#Turn Right
def right():
  print("go right")
  GPIO.output(out1,GPIO.LOW)
  GPIO.output(out2,GPIO.LOW)
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
	
#Randomly stop:
def generator():
	return randint(1,10)

#import
import RPi.GPIO as GPIO          
from time import sleep
import time
from random import randint
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
p.start(70)#right (Magic: 74 (p) and 79 (q))) QTI Magic: q= 55 and p = 60
q.start(73)#left 
print("hi\n")



#print("The default speed & direction of motor is LOW & Forward.....")
#print("g-go s-stop b-backward f-forward L_left R_right e-exit")
#print("\n")    

#straight()
t0= time.time()
stopflag = 0
#HCSR04 Control Block		
print ("PROGRAM A4-L")
while (1):
	R_dist = ReadR()
	L_dist = ReadL()
	#dice = generator()
	print ("Distance Check! Left = {0:.1f} cm, Right = {1:.1f} cm".format(L_dist, R_dist))
	#print ("Measured Distance on Left Sensor= %.1f cm" % L_dist)
    
	#print ("Measured Distance on Right Sensor= %.1f cm" % R_dist)
	
	#~ if ((t0>(t0+500)) and (stopflag ==0)):
		#~ if stopflag ==1: stop()
	
	#~ elif (L_dist > 8) and (R_dist >8):	
	   #~ if (GPIO.input(left_sensor) == 0 & GPIO.input(center_sensor) == 0 & GPIO.input(right_sensor) ==0):
		   #~ print ("ERROR")
		   #~ forward()
		   #~ sleep(.1)
	   #~ if (GPIO.input(left_sensor) == 1 & GPIO.input(center_sensor) == 0 & GPIO.input(right_sensor) == 1): # Sequence 101, Straight
		   #~ print ("Sensor Sequence: L =%b, Center =%b, R =%b", GPIO.input(left_sensor), GPIO.input(center_sensor), GPIO.input(right_sensor))
		   #~ forward()
		   #~ sleep(.5)
	   #~ elif (GPIO.input(left_sensor)==0 & GPIO.input(center_sensor)==1 & GPIO.input(right_sensor) ==1):#Sequence 011, Left 
		   #~ print ("Sensor Sequence: L =%b, Center =%b, R =%b", GPIO.input(left_sensor), GPIO.input(center_sensor), GPIO.input(right_sensor))
		   #~ right()
		   #~ sleep(.1)
	   #~ elif (GPIO.input(left_sensor) == 1 & GPIO.input(center_sensor) ==1 & GPIO.input(right_sensor)==0): #Sequence 110, Right
		   #~ left()
		   #~ sleep(.1)
		   #~ print ("Sensor Sequence: L =%b, Center =%b, R =%b", GPIO.input(left_sensor), GPIO.input(center_sensor), GPIO.input(right_sensor))
	#~ else:
		#~ stopflag ==1 
		#~ print (str(stopflag))
	
	
	#Kevin's Leader Code 
	
	if(L_dist <=8) and (R_dist <=8):
		stop()
		sleep(.5)
	else:
		if (GPIO.input(left_sensor) ==0 & GPIO.input(center_sensor) == 0 & GPIO.input(right_sensor)==0):
			right()
			sleep(.05)
			print("error")
		if GPIO.input(center_sensor):
			forward()
			sleep(.1)
		if GPIO.input(left_sensor):
			left()
			sleep(.05)
		if (GPIO.input(left_sensor) ==0 & GPIO.input(center_sensor) == 0 &  GPIO.input(right_sensor)==1):
			right()
			sleep(.05)
		print ("Sensors: Left = %b, Center = %b, Right = %b", GPIO.input(left_sensor), GPIO.input(center_sensor), GPIO.input(right_sensor))
		stop()
		sleep(.01)
            #~ if GPIO.input(center_sensor):
                    #~ forward()
                    #~ sleep(.1)
            #~ if GPIO.input(left_sensor):
                    #~ left()
                    #~ sleep(.15)
            #~ if (GPIO.input(left_sensor) ==0 & GPIO.input(center_sensor) == 0 &  GPIO.input(right_sensor)==1):
                    #~ right()
                    #~ sleep(.15)
            #~ if (GPIO.input(left_sensor) ==0 & GPIO.input(center_sensor) == 0 & GPIO.input(right_sensor)==0):
                    #~ right()
                    #~ sleep(.05)
                    #~ print("error")
            #~ if (GPIO.input(left_sensor) ==1 & GPIO.input(center_sensor) == 1 & GPIO.input(right_sensor)==1):
				#~ forward()
				#~ sleep(.2)
							
	print ("Sensors: Left = %b, Center = %b, Right = %b", GPIO.input(left_sensor), GPIO.input(center_sensor), GPIO.input(right_sensor))
#	if (dice != 1):
#		print ("you're good: " + str(dice))
#	else:
#		print ("STOP! " + str(dice))
#		stopflag ==1
		
		
