	#A5.py

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
  GPIO.output(out3,GPIO.HIGH)
  GPIO.output(out4,GPIO.LOW)
  print("left")
#Turn Right
def right():
  print("go right")
  GPIO.output(out1,GPIO.LOW)
  GPIO.output(out2,GPIO.HIGH)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.HIGH)
  print("right")


#UltraSonic Functions
def ReadFL():
  #print ("Reading Left")
  # set Trigger to HIGH
  GPIO.output(FL_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
  time.sleep(0.00001)
  GPIO.output(FL_TRIGGER, False)
 
  StartTime = time.time()
  StopTime = time.time()
 
    # save StartTime
  while GPIO.input(FL_ECHO) == 0:
    StartTime = time.time()
 
    # save time of arrival
  while GPIO.input(FL_ECHO) == 1:
    StopTime = time.time()
  #print ("Left Math Time!")
    # time difference between start and arrival
  TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
  FL_distance = (TimeElapsed * 34300) / 2
    
  return FL_distance
  

def ReadFR():
  # set Trigger to HIGH
  GPIO.output(FR_TRIGGER, True)
  #print("Reading Right")
    # set Trigger after 0.01ms to LOW
  time.sleep(0.00001)
  GPIO.output(FR_TRIGGER, False)
 
  StartTime = time.time()
  StopTime = time.time()
   
    # save StartTime
  while GPIO.input(FR_ECHO) == 0:
    StartTime = time.time()
    # save time of arrival
  while GPIO.input(FR_ECHO) == 1:
    StopTime = time.time()
  #print("Right Math Time!")
    # time difference between start and arrival
  TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
  FR_distance = (TimeElapsed * 34300) / 2
  
  return FR_distance 
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
FR_TRIGGER=18
FR_ECHO=23
FL_ECHO=24
FL_TRIGGER=25
R_TRIGGER=5
R_ECHO=6
L_ECHO=11
L_TRIGGER=9

#QTI GPIO's = 26 is green, 19 is yellow, 13 is orange.

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
GPIO.setup(FL_TRIGGER, GPIO.OUT)
GPIO.setup(FR_TRIGGER, GPIO.OUT)
GPIO.setup(L_TRIGGER, GPIO.OUT)
GPIO.setup(R_TRIGGER, GPIO.OUT)
GPIO.setup(L_ECHO, GPIO.IN)
GPIO.setup(R_ECHO, GPIO.IN)
GPIO.setup(FL_ECHO, GPIO.IN)
GPIO.setup(FR_ECHO, GPIO.IN)

#PWM Controllers
p=GPIO.PWM(enA,500) #original 500 for both A and B
q=GPIO.PWM(enB,500)



#start function
p.start(73)#right (Magic: 74 (p) and 79 (q))) QTI Magic: q= 55 and p = 60
q.start(79)#left 
print("hi\n")



#print("The default speed & direction of motor is LOW & Forward.....")
#print("g-go s-stop b-backward f-forward L_left R_right e-exit")
#print("\n")    


#HCSR04 Control Block   
print ("PROGRAM A5")
while (1):
  FR_dist = ReadFR()
  FL_dist = ReadFL()
  R_dist = ReadR()
  L_dist = ReadL()
  #dice = generator()
  print ("Distance Check! Left = {0:.1f} cm, Right = {1:.1f} cm,FLeft = {0:.1f} cm, FRight = {1:.1f} cm ".format(L_dist, R_dist, FL_dist, FR_dist))

  #Kevin's Driver Code 
  if (FL_dist <=15) or (FR_dist <=15) and (L_dist <= 10):#left and straight have walls 
    print ("left and straight have walls (starting condition, Block 1)")
    right()
    sleep(.5)
  elif (L_dist <=8):#left and straight have walls 
    print ("I'm in block 2")
    right()
    sleep(.25) #changed from .25 to .15 then .15 to .10
  elif(FL_dist <=20) or (FR_dist <=20) and (R_dist <= 15):#right and straight have walls
    print("I'm in block 3")
    left()
    sleep(.5)
  elif (R_dist <=8):#left and straight have walls 
    print("Block 4")
    left()
    sleep(.25)
  elif(L_dist <= 15) and (R_dist <= 15):#left and right have walls
	  print ("Block 5")
	  forward()
	  sleep(.5)
  elif(FL_dist <=15) or (FR_dist <=15):
    print ("Block 6")
    left()
    sleep(.5)
  else:#error case, go forward 
    print ("ERROR CASE")
    forward()
    sleep(.5)
  stop()
  sleep(.5)
