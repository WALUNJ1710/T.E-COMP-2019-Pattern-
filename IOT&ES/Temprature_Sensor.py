import Adafruit_DHT
import time 
# Adafruit_DHT.read_retry(Sensor Type, Sensor attached to GPIO number)
# In this program the Sensor that was used was of type DHT-11 which was connected to GPIO4

while True:
  humidity,temprature=Adafruit_DHT.read_retry(11,4)
  print("Temprature: {},Humidity: {}.".format(temprature, humidity))
  
  time.sleep(2)
