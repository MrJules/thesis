from imageai.Detection import ObjectDetection
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from os import listdir
from PIL import Image as PImage
import json

def loadImages(path= '/home/juliosilva/Desktop/Tese/multiple_images/results/detected_images/ '):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = PImage.open(path + image)
        loadedImages.append(img)

    return loadedImages



os.chdir("/home/juliosilva/Desktop/Tese") ## Define working directory

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()

detector.setModelPath(execution_path + "/Redes_Neurais/ObjectRecognition/yolo.h5")
detector.loadModel()

all_images_paths = []
main_directory = os.listdir(execution_path + "/multiple_images")

for each_file in main_directory:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_paths.append(execution_path + "/multiple_images/" + each_file)  ## Aqui temos de por o path das imagens tambem (estava a dar erro antes)

detected_directory_images =os.listdir(execution_path + "/multiple_images/results/detected_images/")

for each_image_in_detected_before in detected_directory_images:
        os.remove(execution_path + "/multiple_images/results/detected_images/" + each_image_in_detected_before)

detected_directory_data =os.listdir(execution_path + "/multiple_images/results/data/")
for each_data_in_detected_before in detected_directory_data:
        os.remove(execution_path + "/multiple_images/results/data/" + each_data_in_detected_before)




print("")
print("-----------------------------------------------------------------------------------------MENU---------------------------------------------------------------------------------------------------------")
print("")
print("All images in the directory :")
print("")
print(os.listdir( execution_path + '/multiple_images/'))
print("")
print('Words available for detection:')
print("")
print(detector.CustomObjects().keys())
print("")
user_input = str(input('Choose a word for detection : '))

while user_input not in detector.CustomObjects().keys():
    user_input = str(input('Please add a word that is available for detection:'))
print ('Your chosen word is : ' + user_input)
percentage = str(input('Choose a minimum percentage for the detection :'))

while int(percentage) > 100 or int(percentage) < 0:
    percentage = str(input('Please add a percentage between 0 and 100:'))

print ('Your chosen percentage is : ' + percentage + '%')
print("")
print("------------------------------------------------------------------------ END OF MENU ----------------------------------------------------------------------------------------------------------")
#globals()[user_input] = True

count = 0

custom = detector.CustomObjects()
if any(user_input in s for s in custom.keys()):
    custom[user_input] = 'valid'
predictions_data=open(execution_path + '/multiple_images/results/data/predictions.json', 'w+')
probability_data=open(execution_path + '/multiple_images/results/data/probability.json', 'w+')
bounding_box_data =open(execution_path + '/multiple_images/results/data/bounding_box.json', 'w+')
total_data =open(execution_path + '/multiple_images/results/data/total_data.json', 'w+')

predictions_total=[]
probability_total=[]
bounding_box_total=[]
total = []

for paths in all_images_paths:
    detections = detector.detectCustomObjectsFromImage(custom_objects = custom, input_image=paths, output_image_path= execution_path + "/multiple_images/results/detected_images/" + "yolo" + str(count) +  ".jpg", minimum_percentage_probability=int(percentage))
    #detections = detector.detectObjectsFromImage(input_image=paths, output_image_path="/home/juliosilva/Desktop/Tese/multiple_images/detected/" + "yolo" + str(count) +  ".jpg", minimum_percentage_probability=int(percentage))
    print("")
    print(" ------------------------------------------------------------------ Results yolo --------------------------------------------------------------------------------")
    
    predictions= []
    probability =[]
    bounding_box =[]

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

        predictions.append(eachObject["name"])                          # cleaned after each image
        probability.append(eachObject["percentage_probability"])        # cleaned after each image
        bounding_box.append(eachObject["box_points"])                   # cleaned after each image

        predictions_total.append(eachObject["name"])                    # this array doesnt get cleaned 
        probability_total.append(eachObject["percentage_probability"])  # this array doesnt get cleaned 
        bounding_box_total.append(str(eachObject["box_points"]))        # this array doesnt get cleaned
        
        total.append(eachObject["name"])                              
        total.append(eachObject["percentage_probability"])  
        total.append(str(eachObject["box_points"]))             

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    if user_input not in predictions:
            os.remove(execution_path + "/multiple_images/results/detected_images/" + "yolo" + str(count) +  ".jpg")
    count = count + 1



json.dump(predictions_total,predictions_data)
json.dump(probability_total,probability_data)
json.dump(bounding_box_total,bounding_box_data)
json.dump(total,total_data)



path = execution_path + "/multiple_images/results/detected_images/"
imgs = loadImages(path)

count = 0
for img in imgs:
    count = count + 1
    # you can show every image
    img.show()
print('Number of detected images with keyword ' + str(user_input) + ' is : '+ str(count))