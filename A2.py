#******************************************
#*Programmers: Kevin Mai and Geff Freire  *
#*Program 2: A2.py                        *
#*Lab 2                                   *
#*Class: EEE 187L (Group Johnny 5)        *
#*Date: September 18, 2019                *
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

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
p=GPIO.PWM(enA,500)
q=GPIO.PWM(enB,500)
#start function
p.start(73)#right (Magic: 74 (p) and 79 (q)))
q.start(79)#left 
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("g-go s-stop b-backward f-forward l-left r-right e-exit")
print("\n")    

while(1):
  
  """user Control
    x=raw_output()
    #Go motor forward
    if x=='g':
      forward()
    #Go motor backwards
    elif x == 'b':
      backward()
  #Stops go motor
    if x=='s':
      stop()
  #left
    if x =='l':
      left()
  #right
    if x = 'r':
      right()
  #End Program
    if x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
  """
  
  #Path for Lab 2
  #forward
  forward()
  sleep(5.1)
  stop()
  sleep(1)
  #rotate right at p1
  right()
  sleep(.7)
  stop()
  sleep(1)
  #forward
  forward()
  sleep(2.25)
  stop()
  sleep(1)
  #rotate right at p2
  right()
  sleep(.7)
  stop()
  sleep(1)
  #forward
  forward()
  sleep(3.5)
  stop()
  sleep(1)
  #rotate right at p3
  right()
  sleep(.3)
  stop()
  sleep(1)
  #forward
  forward()
  sleep(2.5)
  #stop
  stop()
  GPIO.cleanup()
  print("GPIO Clean up")
  break
