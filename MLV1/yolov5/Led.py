import Jetson.GPIO as GPIO

def Init_GPIO(led_pin):
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)    

def Turn_on(led_pin):
    GPIO.output(led_pin, GPIO.HIGH) 
    
def Turn_off(led_pin):
    GPIO.output(led_pin, GPIO.LOW) 