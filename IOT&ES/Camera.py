import picamera
from time import sleep

camera = picamera.PiCamera()

camera.capture('img7.jpg')

sleep(1)
camera.capture('img8.jpg')

camera.start_preview()
camera.brightness=75
sleep(3)

camera.stop_preview()
