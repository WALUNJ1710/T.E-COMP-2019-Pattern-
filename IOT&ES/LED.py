import RPi.GPIO as GPIO
import time

while True:
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(3, GPIO.OUT)
  GPIO.setup(5, GPIO.OUT)
  GPIO.output(3,1)
  GPIO.output(5,1)
  time.sleep(0.10)
  print("led on")
  GPIO.output(3,0)
  GPIO.output(5,0)
  print('led off')
  time.sleep(0.10)
