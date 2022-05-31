from detect2 import detect
from Led import Init_GPIO
from Led import Turn_on
from Led import Turn_off

led_pin = 7
Init_GPIO(led_pin)

image_source = '../data/images/val/2022-05-03-11-25-835.jpg'
# model???????? = ..........
confidence_treshold = 0.9

while True:
    LED = False
    LED = detect(source=image_source, conf_thres=confidence_treshold)
    print("Led = ", LED)
    
    if LED = True:
        Turn_on(led_pin)
    else:
        Turn_off(led_pin)
        
#einde