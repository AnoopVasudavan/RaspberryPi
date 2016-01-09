import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
pwm_obj = GPIO.PWM(18,1)
pwm_obj.start(100)

try :
	while(1) :
		invalue = GPOI.input(13)
		if(invalue == True) :
			pwm_obj.ChangeDutyCycle(50)
		else :
			pwm_obj.ChangeDutyCycle(100)
except KeyboardInterrupt :
	print ("Ctrl C received. Terminating Program")

finally :
	GPIO.cleanup()
	
