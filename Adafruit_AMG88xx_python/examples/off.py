
import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27 , GPIO.OUT)
while(1):
#	print("abc")
#	GPIO.output(27,1)
#	sleep(1)
	GPIO.output(27,0)
	sleep(1)
