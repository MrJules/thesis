from imageai.Detection import ObjectDetection
import numpy as np
import matplotlib.pyplot as plt


detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()

detector.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/ObjectRecognition/retinaNet.h5")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="/home/juliosilva/Desktop/Tese/u2/photo.jpg", output_image_path="/home/juliosilva/Desktop/Tese/u2/retinaNet.jpg", minimum_percentage_probability=30)


bar_width = 0.3

print("")
print(" ")
print(" ------------------------------ Results Retina --------------------------------")

a = plt.figure('RetinaNet Detection')
plt.title('RetinaNet', fontsize = 16)
plt.xlabel('Predictions',fontsize = 12)
plt.ylabel('Percentage of certainty', fontsize = 12)

names = []
probability = []


for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

    names.append(eachObject["name"])
    probability.append(eachObject["percentage_probability"])

    print("--------------------------------------------------------------------------------")

x= np.arange(len(names))

bars = plt.bar(x, height=probability, width=bar_width, color = 'gray')

for bar in bars:
        yval = round(bar.get_height(),2)
        plt.text(bar.get_x(), yval + 1, yval)

plt.xticks(x, names)

plt.show

plt.savefig('/home/juliosilva/Desktop/Tese/u2/retinaNet_graph.png')



detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()

detector.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/ObjectRecognition/yolo.h5")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="/home/juliosilva/Desktop/Tese/u2/photo.jpg", output_image_path="/home/juliosilva/Desktop/Tese/u2/yolo.jpg", minimum_percentage_probability=30)


print("")
print(" ")
print(" ------------------------ Results yolo ----------------------------")


b = plt.figure('YoloV3 detection')
plt.title('YoloV3', fontsize = 16)
plt.xlabel('Predictions',fontsize = 12)
plt.ylabel('Percentage of certainty', fontsize = 12)
names = []
probability = []



for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )

    names.append(eachObject["name"])
    probability.append(eachObject["percentage_probability"])

    print("--------------------------------------------------------------------------------")



x= np.arange(len(names))

bars = plt.bar(x, height=probability, width=bar_width, color = 'blue')

for bar in bars:
        yval = round(bar.get_height(),2)
        plt.text(bar.get_x(), yval + 1, yval)

plt.xticks(x, names)

plt.show
plt.savefig('/home/juliosilva/Desktop/Tese/u2/yolo_graph.png')



detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

detector.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/ObjectRecognition/yolo-tiny.h5")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="/home/juliosilva/Desktop/Tese/u2/photo.jpg", output_image_path="/home/juliosilva/Desktop/Tese/u2/yolo_tiny.jpg", minimum_percentage_probability=30)


print("")
print(" ")
print(" ------------------------ Results tiny yolo ----------------------------")


c = plt.figure('TinyYolo Detection')
plt.title('TinyYolo',fontsize = 16 )
plt.xlabel('Predictions',fontsize = 12)
plt.ylabel('Percentage of certainty', fontsize = 12)
names = []
probability = []



for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )


    names.append(eachObject["name"])
    probability.append(eachObject["percentage_probability"])


    print("--------------------------------------------------------------------------------")




x= np.arange(len(names))

bars = plt.bar(x, height=probability, width=bar_width, color = 'red')

for bar in bars:
        yval = round(bar.get_height(),2)
        plt.text(bar.get_x(), yval + 1, yval)

plt.xticks(x, names)

plt.show

plt.savefig('/home/juliosilva/Desktop/Tese/u2/yolo_tiny_graph.png')

plt.show()
