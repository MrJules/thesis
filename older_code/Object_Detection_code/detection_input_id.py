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

organized_data = open('/home/juliosilva/Desktop/Testes_ID/organized_data.json' , 'w+') # ficheiro json


image_info = {
        'images': []
    }

image_id = []


image_name_array = []
#counter = 0
for all_images in all_images_paths:

        src = str(all_images)
        src = src.split("multiple_images/",1)[1] ## Defenir o diretorio onde estao a ir ser buscadas as imagens
        src = src[:10] # apenas a data da imagem fica como id
        src = src.replace("-", "_")
        
        final_src = "u1_" + src + "_" + "0"

       # counter = counter + 1 
        flag = True
        if (final_src not in image_id): 
            image_id.append(final_src)
            flag = False

        counter = 0

        if (flag is True):
            while (final_src in image_id): 
                
            # final =  int(final_src[-1])
                final_src_new = "u1_" + src + "_" + str(counter)  

                counter = counter + 1

                if (final_src_new not in image_id):
                    image_id.append(final_src_new)
                    final_src = "nothing"


for paths in all_images_paths:
    detections = detector.detectCustomObjectsFromImage(custom_objects = custom, input_image=paths, output_image_path= execution_path + "/multiple_images/results/detected_images/" + "yolo" + str(count) +  ".jpg", minimum_percentage_probability=int(percentage))
    #detections = detector.detectObjectsFromImage(input_image=paths, output_image_path="/home/juliosilva/Desktop/Tese/multiple_images/detected/" + "yolo" + str(count) +  ".jpg", minimum_percentage_probability=int(percentage))
    print("")
    print(" ------------------------------------------------------------------ Results yolo --------------------------------------------------------------------------------")
    



    

    print(paths)
    
    objects_detection = {
        image_id[count] : []
    }

    predictions = []
    
    for eachObject in detections:

        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

        predictions.append(eachObject["name"])  

        objects_detection[image_id[count]].append({
            
            str(eachObject["name"]): [
                
                str(eachObject["percentage_probability"]),
                str(eachObject["box_points"])
            ]         
        })

        image_info['images'].append(objects_detection)

        


    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    if user_input in predictions: 
        
        json.dump(objects_detection,organized_data, indent= 3)

    if user_input not in predictions:
            os.remove(execution_path + "/multiple_images/results/detected_images/" + "yolo" + str(count) +  ".jpg")
   
    count = count + 1

    


path = execution_path + "/multiple_images/results/detected_images/"

imgs = loadImages(path)

count = 0

for img in imgs:
    count = count + 1
    # you can show every image
    #img.show()
print('Number of detected images with keyword ' + str(user_input) + ' is : '+ str(count))