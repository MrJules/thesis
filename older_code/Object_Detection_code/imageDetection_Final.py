from imageai.Prediction import ImagePrediction
import os

import numpy as np
import matplotlib.pyplot as plt


def find_common(list1,list2):
    for x in list1:
      for y in list2:
        if x == y :
          list2.remove(x)

execution_path = os.getcwd()

width = .15

### DenseNet

multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsDenseNet()
multiple_prediction.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/imageRecognition/DenseNet.h5")
multiple_prediction.loadModel()

all_images_array = []

all_files = os.listdir("/home/juliosilva/Desktop/Tese/u1") #diretorio igual ao all_images_array

#for file in all_files:
#   print (file)  
for each_file in all_files:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_array.append("/home/juliosilva/Desktop/Tese/u1/" + each_file)  ## Aqui temos de por o path das imagens tambem (estava a dar erro antes)
#print(all_images_array)

results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)

print("")
print("")
print("--------------------------- Results DenseNet ---------------------------")

for each_result in results_array:
    predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions[index] , " : " , percentage_probabilities[index])

    print("---------------------------------------------------------------")


#bars = plt.bar( predictions, height=percentage_probabilities, width=width)

# access the bar attributes to place the text in the appropriate location
#for bar in bars:
#    yval = round(bar.get_height(),2)
#    plt.text(bar.get_x() +0.03 , yval + 1, yval)
# Show graphic



## InceptionV3

multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsInceptionV3()
multiple_prediction.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/imageRecognition/inceptionV3.h5")
multiple_prediction.loadModel()

all_images_array = []

all_files = os.listdir("/home/juliosilva/Desktop/Tese/u1") #diretorio igual ao all_images_array

#for file in all_files:
#   print (file)  
for each_file in all_files:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_array.append("/home/juliosilva/Desktop/Tese/u1/" + each_file)  ## Aqui temos de por o path das imagens tambem (estava a dar erro antes)
#print(all_images_array)

results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)

print("")
print("")
print("--------------------------- Results Inception V3 ---------------------------")

for each_result in results_array:
    predictions2, percentage_probabilities2 = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions[index] , " : " , percentage_probabilities2[index])

    print("---------------------------------------------------------------")


#bars = plt.bar(predictions2, height=percentage_probabilities2, width=width,bottom=percentage_probabilities)

# access the bar attributes to place the text in the appropriate location
#for bar in bars:
#    yval = round(bar.get_height(),2)
#    plt.text(bar.get_x() +0.03 , yval + 1, yval)
# Show graphic




## ResNet50

multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsResNet()
multiple_prediction.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/imageRecognition/ResNet50.h5")
multiple_prediction.loadModel()

all_images_array = []

all_files = os.listdir("/home/juliosilva/Desktop/Tese/u1") #diretorio igual ao all_images_array

#for file in all_files:
#   print (file)  
for each_file in all_files:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_array.append("/home/juliosilva/Desktop/Tese/u1/" + each_file)  ## Aqui temos de por o path das imagens tambem (estava a dar erro antes)
#print(all_images_array)

results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)

    
print("");
print("");

print("--------------------------- Results ResNet50 ---------------------------")

for each_result in results_array:
    predictions3, percentage_probabilities3 = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions3[index] , " : " , percentage_probabilities3[index])

    print("---------------------------------------------------------------")

#bars = plt.bar(predictions3, height=percentage_probabilities3, width=width,bottom=percentage_probabilities2)

# access the bar attributes to place the text in the appropriate location
#for bar in bars:
 #   yval = round(bar.get_height(),2)
 #   plt.text(bar.get_x() +0.03 , yval + 1, yval)
# Show graphic



## SquezeeNet

multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsSqueezeNet()
multiple_prediction.setModelPath("/home/juliosilva/Desktop/Tese/Redes_Neurais/imageRecognition/SqueezeNet.h5")
multiple_prediction.loadModel()

all_images_array = []

all_files = os.listdir("/home/juliosilva/Desktop/Tese/u1") #diretorio igual ao all_images_array

#for file in all_files:
#   print (file)  
for each_file in all_files:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_array.append("/home/juliosilva/Desktop/Tese/u1/" + each_file)  ## Aqui temos de por o path das imagens tambem (estava a dar erro antes)
#print(all_images_array)

results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)


print("");
print("");


print("--------------------------- Results SqueezeNet ---------------------------")

for each_result in results_array:
    predictions4, percentage_probabilities4 = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions[index] , " : " , percentage_probabilities[index])

    print("---------------------------------------------------------------")

#bars = plt.bar(predictions4, height=percentage_probabilities4, width=width,bottom=percentage_probabilities3)

# access the bar attributes to place the text in the appropriate location
#for bar in bars:
 #   yval = round(bar.get_height(),2)
 #   plt.text(bar.get_x() +0.03 , yval + 1, yval)
temp=[]
all_values1 = []
all_values2 = []
all_values3 = []
all_values4 = []
temp.extend(predictions)

tempVar = predictions2.copy()
find_common(temp,tempVar)
temp.extend(tempVar)

tempVar = predictions3.copy()
find_common(temp,tempVar)
temp.extend(tempVar)


tempVar = predictions4.copy()
find_common(temp,tempVar)
temp.extend(tempVar)

for i in range(len(temp)):
    for j in range(len(predictions)):
        if predictions[j] == temp[i]:
            all_values1.append(percentage_probabilities[j])
            break
        else:
            if(j == len(predictions)-1):
                all_values1.append(0) 
    for j in range(len(predictions2)):
        if predictions2[j] == temp[i]:
            all_values2.append(percentage_probabilities2[j])
            break
        else:
            if(j == len(predictions)-1):
                all_values2.append(0) 
    for j in range(len(predictions3)):
        if predictions3[j] == temp[i]:
            all_values3.append( percentage_probabilities3[j])
            break
        else:
           if(j == len(predictions)-1):
                all_values3.append(0) 
    for j in range(len(predictions4)):
        if predictions4[j] == temp[i]:
            all_values4.append(percentage_probabilities4[j])
            break
        else:
            if(j == len(predictions)-1):
                all_values4.append(0)    
#percentage_probabilities.extend(percentage_probabilities2)
#percentage_probabilities.extend(percentage_probabilities3)
#percentage_probabilities.extend(percentage_probabilities4)
fig, ax = plt.subplots()
x = np.arange(len(temp))  # the label locations
bars = plt.bar(x-3/2*width, height=all_values1, width=width)#,bottom=percentage_probabilities3)
for bar in bars:
    yval = round(bar.get_height(),2)
    if yval != 0:
        plt.text(bar.get_x() +0.03 , yval + 1, yval)
bars = plt.bar(x-width/2, height=all_values2, width=width)#,bottom=all_values1)
for bar in bars:
    yval = round(bar.get_height(),2)
    if yval != 0:
        plt.text(bar.get_x() +0.03 , yval + 1, yval)
bars = plt.bar(x+width/2, height=all_values3, width=width)#,bottom=all_values2)
for bar in bars:
    yval = round(bar.get_height(),2)
    if yval != 0:
        plt.text(bar.get_x() +0.03 , yval + 1, yval)
bars = plt.bar(x+3/2*width, height=all_values4, width=width)#,bottom=all_values3)
for bar in bars:
    yval = round(bar.get_height(),2)
    if yval != 0:
        plt.text(bar.get_x() +0.03 , yval + 1, yval)
# Show graphic
bar_width = 0.3
ax.set_xticks(x)
ax.set_xticklabels(temp)

redes = ['DenseNet','InceptionV3','ResNet50','SqueezeNet']
plt.legend(redes, loc = 1)


plt.title('Image Detection')
plt.xlabel('Predictions',fontsize = 16)
plt.ylabel('Percentage of Probability', fontsize = 16)
plt.show()

