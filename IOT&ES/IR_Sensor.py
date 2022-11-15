# For 'GPIO.BOARD' MODE,we give the actual pin position
#For 'GPIO.BCM' MODE, we give the actual GPIO pin number

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

gpio_pin_in = 3
gpio_pin_out = 5

GPIO.setup(gpio_pin_in,GPIO.IN)
GPIO.setup(gpio_pin_out,GPIO.OUT)

while True:
  v=GPIO.input(3)
  if(v==0)
    GPIO.output(gpio_pin_out,False)
  else:
    GPIO.output(gpio_pin_out,True)
    
               
