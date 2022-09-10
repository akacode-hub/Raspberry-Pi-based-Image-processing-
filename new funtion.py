from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
LED = 23
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.LOW)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
camera = PiCamera()


camera.start_preview()
GPIO.output(LED,GPIO.HIGH)
sleep(10)
camera.capture('/home/pi/Desktop/akanksha.jpg')
GPIO.output(LED,GPIO.LOW)
camera.stop_preview()
