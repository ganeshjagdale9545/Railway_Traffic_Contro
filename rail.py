import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(2,GPIO.IN)
GPIO.setup(3,GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
global flag
flag=0
GPIO.output(17, True)
GPIO.output(4, False)
GPIO.output(23, False)
GPIO.output(22, False)
GPIO.output(27, False)
def start():
 try:
  global flag
  while 1:
   if(GPIO.input(2)==False):
    if(flag==0):
	 GPIO.output(4, True)
	 GPIO.output(17, False)
	 GPIO.output(23, True)
	 GPIO.output(27, True)
	 flag=1
	 time.sleep(5)
    else:
     GPIO.output(17, True)
     GPIO.output(4, False)
     flag=0
     GPIO.output(23, False)
     GPIO.output(22, False)
     GPIO.output(27, False)
     time.sleep(5)
   if(GPIO.input(3)==False):
    if(flag==0):
	 GPIO.output(4, True)
	 GPIO.output(17, False)
	 GPIO.output(22, True)
	 GPIO.output(27, True)
	 flag=1
	 time.sleep(5)
    else:
     GPIO.output(17, True)
     GPIO.output(4, False)
     flag=0	
     GPIO.output(23, False)
     GPIO.output(22, False)
     GPIO.output(27, False)
     time.sleep(5)
 except:
  start()
start()
