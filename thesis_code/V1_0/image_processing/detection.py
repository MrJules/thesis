    ###################################################### IMPORT ######################################################

import os
import json
from tqdm import tqdm
from imageai.Detection import ObjectDetection
#################################################################################### MAIN  #################################################################################


if __name__ == '__main__' :
    
    print ("")
    print("-----------------------------------------------IMAGE PROCESSING SCRIPT----------------------------------------- \n")
    dir_path = os.path.dirname(os.path.realpath(__file__))
   
    image_folder = os.listdir(dir_path + "/images")
    folders_paths = []


    for each_folder in image_folder : 
        if each_folder != ".gitkeep" :
            folders_paths.append(dir_path + "/images/" + each_folder)

    images_paths = []
    images_names = []
    image_info = {}


    for each_folder_path in folders_paths:
        folder = os.listdir(each_folder_path)
        for each_image in folder :
            if each_image.startswith("2") or each_image.startswith("b") or each_image.startswith("B"):
                if(each_image.endswith(".jpg") or each_image.endswith(".png") or each_image.endswith(".JPG") or each_image.endswith(".PNG")):
                    images_paths.append(each_folder_path + "/" + each_image) 
                    images_names.append(each_image)
                    



    json_path = dir_path + "/json_result/image_data.json"
    image_data = open(json_path , 'w+') 

    neural_path = dir_path + "/neural_network/yolo.h5"
  

    
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(neural_path)
    detector.loadModel()
    
    output_path = dir_path + "/results/" 
    print("")
    print("PROCESSING IMAGES...")
    print("")
    for path in tqdm(images_paths) :
        for name in images_names:
            if name in path:
                except_flag = False

                # use output_image = path to results, and delete in output_type in order to get the output images in the file results
                try : returned_image, detections =  detector.detectObjectsFromImage(input_image=path, output_type= "array" , minimum_percentage_probability=30)
                except: except_flag = True

                if except_flag == False:
                    image_info.update({name : {}})

                    if name[0] == "b" : local_time = name[17:21] + "-" + name[21:23] + "-" + name[23:25] + "_" + name[26:28] + ":" + name[28:30]
                    if name[0] == "B" : local_time = name[17:21] + "-" + name[21:23] + "-" + name[23:25] + "_" + name[26:28] + ":" + name[28:30]
                    if str(name[0]) == "2" :  local_time = name[0:4] + "-" + name[4:6] + "-" + name[6:8] + "_" + name[9:11] + ":" + name[11:13]
                    image_info[name]["local_time"] = local_time
                    image_info[name]["concepts"] = {}
                    image_info[name]["activity"] = "NULL"
                    image_info[name]["location"] = "NULL"
                    image_info[name]["categories"] = {}
                    image_info[name]["attributes"] = []
                    image_info[name]["io_score"] = "NULL"
                    
                    for eachObject in detections: 
                        image_info[name]["concepts"][str(eachObject["name"])] = {
                            "score" : float(eachObject["percentage_probability"]/100),
                            "box" : [float(eachObject["box_points"][0]),float(eachObject["box_points"][1]),float(eachObject["box_points"][2]),float(eachObject["box_points"][3])]
                        }
                if except_flag == True:
                    print("Exception ocurred, skipping image :" , name)
                       
    json.dump(image_info, image_data, indent=5)

    
    



