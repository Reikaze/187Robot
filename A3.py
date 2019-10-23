#******************************************
#*Programmers: Kevin Mai and Geff Freire  *
#*Program 3: A3.py                        *
#*Lab 3                                   *
#*Class: EEE 187L (Group Johnny 5)        *
#*Date: October 2, 2019	                  *
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

def left():
  print("go left")
  GPIO.output(out1,GPIO.HIGH)
  GPIO.output(out2,GPIO.LOW)
  GPIO.output(out3,GPIO.LOW)
  GPIO.output(out4,GPIO.LOW)
  print("left")

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
#import
import RPi.GPIO as GPIO          
from time import sleep

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

left_sensor = 13 #left QTI
center_sensor = 19
right_sensor = 26 #right QTI

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(center_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
p=GPIO.PWM(enA,500)
q=GPIO.PWM(enB,500)
#start function
p.start(74)#right (Magic: 74 (p) and 79 (q)))
q.start(79)#left 
print("hi\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("g-go s-stop b-backward f-forward l-left r-right e-exit")
print("\n")    


while(1):
	if (GPIO.input(left_sensor) ==0 & GPIO.input(center_sensor) == 0 & GPIO.input(right_sensor)==0):
		right()
		sleep(.05)
		print("error")
	if GPIO.input(center_sensor):
		forward()
		sleep(.1)
	if GPIO.input(left_sensor):
		left()
		sleep(.15)
	if (GPIO.input(left_sensor) ==0 & GPIO.input(center_sensor) == 0 &  GPIO.input(right_sensor)==1):
		right()
		sleep(.15)
	print ("Sensors: Left = %b, Center = %b, Right = %b", GPIO.input(left_sensor), GPIO.input(center_sensor), GPIO.input(right_sensor))
	stop()
	sleep(.01)