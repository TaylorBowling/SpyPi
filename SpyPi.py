import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM) #Defines how we name the GPIO pins
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN) #Sets the output pin of the PIR Sensor
GPIO.setup(24,GPIO.OUT) #Sets the output pin of LED 1
GPIO.setup(23,GPIO.OUT) #Sets the output pin of LED 2

camera = PiCamera()

try:
    time.sleep(5) #Stabilizes sensor to prevent false detection
    while True:
        if GPIO.input(17):
            print("Motion Detected")
            GPIO.output(23,GPIO.HIGH) #Turn on LED 1
            GPIO.output(24,GPIO.HIGH) #Turn off LED 2
            camera.capture('/home/pi/Desktop/SpyPi_Photos/' + time.strftime('%y%m%d_%H-%M-%S') + '.jpg')
            	#Establishes a path and file name for captured photos
            time.sleep(5) #Prevents double detection of motion
            GPIO.output(23,GPIO.LOW) #Turn off LED 1
            GPIO.output(24,GPIO.LOW) #Turn off LED 2
        time.sleep(0.1) #loop delay

except:
	GPIO.cleanup() #"Cleans up" all of the GPIO ports we used
