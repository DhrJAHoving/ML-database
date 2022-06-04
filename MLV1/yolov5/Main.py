from detect2 import detect
from Led import Init_GPIO
from Led import Turn_on
from Led import Turn_off

led_pin = 7
Init_GPIO(led_pin)

W = 'Database_V3/Best_one/weights/best.pt'           # weights_source    Best one is anders
I = '../data/images/val/2022-05-03-11-25-835.jpg'    # image_source      Dit zijn de fotos
D = '/data/custom_dataset_V3.yaml'                   # data_source
C = 0.9                                              # confidence_treshold

while True:
    # Take image
    # Save image on path I

    LED = False
    LED = detect(weights=W, source=I, data=D, conf_thres=C)
    print("Led = ", LED)
    
    if LED = True:
        Turn_on(led_pin)
    else:
        Turn_off(led_pin)