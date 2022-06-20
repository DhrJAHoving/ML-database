from detect2 import detect
# from Led import Init_GPIO
# from Led import Turn_on
# from Led import Turn_off

# led_pin = 7
# Init_GPIO(led_pin)

W = 'Database_V4/SER640x22x200xyolov5s.ptx1/weights/best.pt'           # weights_source    Best one is anders
I = '../datasets/custom_dataset_V3/val/images/2022-05-08-10-33-819.jpg'    # image_source      Dit zijn de fotos
D = 'data/custom_dataset_V3.yaml'                   # data_source
C = 0.85                                              # confidence_treshold

i = 0
# while True:
while i < 1:
    # Take image
    # Save image on path I

    LED = False
    LED = detect(weights=W, source=I, data=D, conf_thres=C)
    print("Led = ", LED)
    
    # if LED == True:
    #     Turn_on(led_pin)
    # else:
    #     Turn_off(led_pin)
    
    i = i + 1