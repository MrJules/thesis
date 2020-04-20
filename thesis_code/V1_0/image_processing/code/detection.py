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
   
    images_folder = os.listdir(dir_path + "/../images")
    images_folder_path = dir_path + "/../images"
    images_paths = []
    images_names = []

    image_info = {}

    for each_image in images_folder:
        if(each_image.endswith(".jpg") or each_image.endswith(".png")):
            images_paths.append( images_folder_path + "/" + each_image) 
            images_names.append(each_image)
            image_info.update({each_image : {}})
            


    json_path = dir_path + "/../json_result/image_data.json"
    image_data = open(json_path , 'w+') 

    neural_path = dir_path + "/../neural_network/yolo.h5"
  

    
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(neural_path)
    detector.loadModel()
    
    output_path = dir_path + "/../results/" 
    print("")
    print("PROCESSING IMAGES")
    for path in tqdm(images_paths) :
        for name in images_names:
            if name in path:

                if name[0] == "b" : local_time = name[17:21] + "-" + name[21:23] + "-" + name[23:25] + "_" + name[26:28] + ":" + name[28:30]
                if str(name[0]) == "2" :  local_time = name[0:4] + "-" + name[4:6] + "-" + name[6:8] + "_" + name[9:11] + ":" + name[11:13]
                image_info[name]["local_time"] = local_time
                image_info[name]["concepts"] = {}
                image_info[name]["activity"] = "NULL"
                image_info[name]["location"] = "NULL"
                image_info[name]["categories"] = {}
                
                # use output_image = path to results, and delete in output_type in order to get the output images in the file results
                returned_image, detections =  detector.detectObjectsFromImage(input_image=path, output_type= "array" , minimum_percentage_probability=30)

                
                for eachObject in detections: 
                    image_info[name]["concepts"][str(eachObject["name"])] = {
                        "score" : float(eachObject["percentage_probability"]/100),
                        "box" : [float(eachObject["box_points"][0]),float(eachObject["box_points"][1]),float(eachObject["box_points"][2]),float(eachObject["box_points"][3])]
                    }
                
    json.dump(image_info, image_data, indent=5)

    
    



