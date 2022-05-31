from detect2 import detect
from Led import Init_GPIO
from Led import Turn_on
from Led import Turn_off


LED = False
led_pin = 7
Init_GPIO(led_pin)
image_source = '../data/images/val/2022-05-03-11-25-835.jpg'
confidence_treshold = 0.9


# LED = detect(source=image_source, conf_thres=confidence_treshold)

# print("Led = ", LED)