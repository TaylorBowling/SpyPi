import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN) #PIR Sensor
GPIO.setup(24,GPIO.OUT) #LED 1
GPIO.setup(23,GPIO.OUT) #LED 2

camera = PiCamera()

try:
    time.sleep(5) #stabilizes sensor
    while True:
        if GPIO.input(17):
            print("Motion Detected")
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(24,GPIO.HIGH)
            camera.capture('/home/pi/Desktop/SpyPi_Photos/' + time.strftime('%y%m%d_%H-%M-%S') + '.jpg')
            time.sleep(5) #prevents double detection of motion
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
        time.sleep(0.1) #loop delay

except:
                  GPIO.cleanup()
