    ###################################################### IMPORT ######################################################

import os
import json
from tqdm import tqdm
from imageai.Detection import ObjectDetection
#################################################################################### MAIN  #################################################################################

def getIndexPositions(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
 
    return indexPosList

if __name__ == '__main__' :
    
    print ("")
    print("-----------------------------------------------IMAGE PROCESSING SCRIPT----------------------------------------- \n")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    #### detector
    neural_path = dir_path + "/neural_network/yolo.h5"
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(neural_path)
    detector.loadModel()
    #output_path = dir_path + "/results/" 
    ######

    
    image_folder = os.listdir(dir_path + "/images")
    folders_paths = []


    for each_folder in image_folder : 
        if each_folder != ".gitkeep" :
            folders_paths.append(dir_path + "/images/" + each_folder)

    

    print("")
    print("PROCESSING IMAGES...")
    print("")


    for each_folder_path in folders_paths:
        images_paths = []
        images_names = []
        images_dict = {}

        index_bar = getIndexPositions(each_folder_path, '/')
        folder_name = each_folder_path[index_bar[len(index_bar)-1] + 1 : len(each_folder_path)]

        json_path = dir_path + "/json/json_detect/" + folder_name + ".json"

        folder = os.listdir(each_folder_path)

        for each_image in folder :
            if each_image.startswith("2") or each_image.startswith("b") or each_image.startswith("B"):
                if(each_image.endswith(".jpg") or each_image.endswith(".png") or each_image.endswith(".JPG") or each_image.endswith(".PNG")):
                    images_paths.append(each_folder_path + "/" + each_image) 
                    images_names.append(each_image)

        print("Processing folder : " + str(folders_paths.index(each_folder_path) + 1) + "/" + str(len(folders_paths)))     
             
        for path in tqdm(images_paths) :
            for name in images_names:
                if name in path:
                    except_flag = False

                    # use output_image = path to results, and delete in output_type in order to get the output images in the file results
                    try : returned_image, detections =  detector.detectObjectsFromImage(input_image=path, output_type= "array" , minimum_percentage_probability=30)
                    except: except_flag = True

                    if except_flag == False:
                        images_dict.update({name : {}})
                        images_dict[name]["concepts"] = {}

                        for eachObject in detections: 
                            images_dict[name]["concepts"][str(eachObject["name"])] = {
                                "score" : float(eachObject["percentage_probability"]/100),
                                "box" : [float(eachObject["box_points"][0]),float(eachObject["box_points"][1]),float(eachObject["box_points"][2]),float(eachObject["box_points"][3])]
                            }
                    if except_flag == True:
                        print("Exception ocurred, skipping image :" , name)

        sorted_data = {k: v for k, v in sorted(images_dict.items(), key=lambda item: item[0])}                
        #json.dump(images_dict, image_data, indent=5)
        with open(json_path, 'w') as jsonfile:
                json.dump(sorted_data, jsonfile, indent=4)
    
    



