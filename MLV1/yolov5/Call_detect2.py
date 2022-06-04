from detect2 import detect
# import Jetson.GPIO as GPIO
# import cv2 ?

weights_path = 'runs/train/CPU_epochs=30_batch-size=24_image-size=640_database-size=600/weights/best.pt'
confidence_treshold = 0.9

while True:
    LED = False
    
    # Maak foto
    # Sla foto op
    image_source = '../datasets/custom_dataset_V3/val/images/2022-05-08-10-33-1644.jpg' #Nieuwste afbeelding
    LED = detect(weights=weights_path, source=image_source, conf_thres=confidence_treshold)
   
    # Zet led aan of uit
    print("Led = ", LED)