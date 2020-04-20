from imageai.Detection import ObjectDetection
import json
import os

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()

detector.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/ObjectRecognition/yolo.h5")
detector.loadModel()


all_images_paths = []
main_directory = os.listdir("/home/juliosilva/Desktop/Tese/wordcloud_image")
for each_file in main_directory:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_paths.append("/home/juliosilva/Desktop/Tese/wordcloud_image/" + each_file)  ## Aqui temos de por o path das imagens tambem (estava a dar erro antes)

detected_directory_data =os.listdir("/home/juliosilva/Desktop/Tese/wordcloud_image/data/")
for each_data_in_detected_before in detected_directory_data:
        os.remove("/home/juliosilva/Desktop/Tese/wordcloud_image/data/" + each_data_in_detected_before)

detected_directory_images =os.listdir("/home/juliosilva/Desktop/Tese/wordcloud_image/detections_image/")
for each_image_in_detected_before in detected_directory_images:
        os.remove("/home/juliosilva/Desktop/Tese/wordcloud_image/detections_image/" + each_image_in_detected_before)


yolo_data =open('/home/juliosilva/Desktop/Tese/wordcloud_image/data/yolo_data.json', 'w+')
names_yolo = []
count = 0


for paths in all_images_paths:
    detections = detector.detectObjectsFromImage(input_image=paths,output_image_path="/home/juliosilva/Desktop/Tese/wordcloud_image/detections_image/" + "yolo" + str(count) +  ".jpg", minimum_percentage_probability=30)
    
    print("")
    print(" ------------------------------------------------------------------ Results yolo --------------------------------------------------------------------------------")
    
    predictions= []
    probability =[]
    bounding_box =[]

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

        names_yolo.append(eachObject["name"])                              
    count = count + 1

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


json.dump(names_yolo,yolo_data)



tiny_yolo_data = open('/home/juliosilva/Desktop/Tese/wordcloud_image/data/tiny_yolo_data.json', 'w+')
names_tiny_yolo = []
count = 0

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

detector.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/ObjectRecognition/yolo-tiny.h5")
detector.loadModel()


for paths in all_images_paths:
    detections = detector.detectObjectsFromImage(input_image=paths,output_image_path="/home/juliosilva/Desktop/Tese/wordcloud_image/detections_image/" + "tiny_yolo" + str(count) +  ".jpg", minimum_percentage_probability=30)
    
    print("")
    print(" ------------------------------------------------------------------ Results Tiny YOLO --------------------------------------------------------------------------------")
    
    predictions= []
    probability =[]
    bounding_box =[]

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

        names_tiny_yolo.append(eachObject["name"])                              
    count = count + 1

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

json.dump(names_tiny_yolo,tiny_yolo_data)





detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()

detector.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/ObjectRecognition/retinaNet.h5")
detector.loadModel()


retina_data = open('/home/juliosilva/Desktop/Tese/wordcloud_image/data/retina_data.json', 'w+')
names_retina = []
count = 0

for paths in all_images_paths:
    detections = detector.detectObjectsFromImage(input_image=paths,output_image_path="/home/juliosilva/Desktop/Tese/wordcloud_image/detections_image/" + "retina" + str(count) +  ".jpg", minimum_percentage_probability=30)
    
    print("")
    print(" ------------------------------------------------------------------ Results Retina --------------------------------------------------------------------------------")
    
    predictions= []
    probability =[]
    bounding_box =[]

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

        names_retina.append(eachObject["name"])                              
    count = count + 1

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

json.dump(names_retina,retina_data)





