from detect2 import detect

LED = False
image_source = '../data/images/val/2022-05-03-11-25-835.jpg'
confidence_treshold = 0.9


LED = detect(source=image_source, conf_thres=confidence_treshold)

print("Led = ", LED)