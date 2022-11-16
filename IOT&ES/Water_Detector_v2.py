import RPi.GPIO as GPIO

GPIO_pin_in=5
GPIO_pin_out=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_pin_in,IN)
GPIO.setup(gpio_pin_out,OUT)

while True:
  v=GPIO.input(5)
  
  if(v==0):
    GPIO.output(gpio_pin_out,True)
  else:
    GPIO.output(gpio_pin_out,False)
    
