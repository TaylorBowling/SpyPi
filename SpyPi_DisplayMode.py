import RPi.GPIO as GPIO
import time
from picamera import PiCamera

camera = PiCamera()
GPIO.setmode(GPIO.BCM) #Defines how we name the GPIO pins
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.OUT) #Sets the output pin of LED 1
GPIO.setup(24,GPIO.OUT) #Sets the output pin of LED 1

camera.start_preview() #Start showing Pi camera feed
GPIO.output(23,GPIO.HIGH) #Turn on LED 1
GPIO.output(24,GPIO.HIGH) #Turn on LED 2

time.sleep(60) #Sleeps to show the camera feed for 60 seconds

GPIO.output(23,GPIO.LOW) #Turn off LED 1
GPIO.output(24,GPIO.LOW) #Turn off LED 2
camera.stop_preview() #Stop showing Pi camera feed

except:
        GPIO.cleanup() #"Cleans up" all of the GPIO ports we used