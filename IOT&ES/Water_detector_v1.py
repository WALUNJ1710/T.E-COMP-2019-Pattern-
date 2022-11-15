import RPi.GPIO AS gpio
import time

GPIO.setmode(GPIO.BCM)

try:
  while True:
    if(GPIO.input(3)==True):
      print("Water Detected")
      GPIO.output(2,True)
      
    else:
      print('Water not detected')
      GPIO.output(2,False)
      
except:
  GPIO.cleanup()
