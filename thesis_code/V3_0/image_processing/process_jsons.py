####################################################### IMPORT ######################################################

import json
import os
from tqdm import tqdm

###################################################### FUNCTIONS #################################################
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

###################################################### MAIN ######################################################

if __name__ == '__main__' :

    print("")
    print("------------------------------------------JSON PROCESSING SCRIPT ----------------------------------------- \n")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    ground_path = dir_path + "/json/ground_data/data.json"
    ground_data = json.loads(open(ground_path).read())


    json_templates_path = dir_path + "/json/json_template/"
    json_templates_folder = os.listdir(json_templates_path)
    if ".gitkeep" in json_templates_folder : del json_templates_folder[json_templates_folder.index(".gitkeep")]

    json_detect_path = dir_path + "/json/json_detect/"
    json_detect_folder = os.listdir(json_detect_path)
    if ".gitkeep" in json_detect_folder : del json_detect_folder[json_detect_folder.index(".gitkeep")]

    json_places_path = dir_path + "/json/json_places/"
    json_places_folder = os.listdir(json_places_path)
    if ".gitkeep" in json_places_folder : del json_places_folder[json_places_folder.index(".gitkeep")]

    
    
    for each_json in json_templates_folder:
        print("")
        print("Copying GT location and activity to template -> json: " + str(json_templates_folder.index(each_json)+1) + "/" + str(len(json_templates_folder)))

        if each_json.endswith(".json"):
            json_path_result = dir_path + "/json/json_result/" + each_json
            each_json_path = json_templates_path + "/" + each_json
            images_dict = json.loads(open(each_json_path).read())

            for image_name in tqdm(images_dict.keys()):
                if image_name in ground_data.keys():
               # for ground_image in ground_data.keys():
                    ##if image_name == ground_image:
                     images_dict[image_name]["activity"] = ground_data[image_name]["activity"]
                     images_dict[image_name]["location"] = ground_data[image_name]["location"]

            sorted_data = {k: v for k, v in sorted(images_dict.items(), key=lambda item: item[0])}        
            with open(json_path_result, 'w') as jsonfile:
                json.dump(sorted_data, jsonfile, indent=4)
    
    for each_json in json_detect_folder:
        if each_json.endswith(".json"):
            print("")
            print("Copying detections json to template -> json: " + str(json_templates_folder.index(each_json)+1) + "/" + str(len(json_templates_folder)))
            
            json_path_result = dir_path + "/json/json_result/" + each_json 
            each_json_path = json_detect_path + "/" + each_json
            images_dict = json.loads(open(json_path_result).read())
            
            copy_dict = json.loads(open(each_json_path).read())

            for image_name in tqdm(images_dict.keys()):
                if image_name in copy_dict.keys():
                    images_dict[image_name]["concepts"] = copy_dict[image_name]["concepts"]

            sorted_data = {k: v for k, v in sorted(images_dict.items(), key=lambda item: item[0])}        
            with open(json_path_result, 'w') as jsonfile:
                json.dump(sorted_data, jsonfile, indent=4)


    for each_json in json_places_folder:
        if each_json.endswith(".json"):
            print("")
            print("Copying places json to template  -> json: " + str(json_templates_folder.index(each_json)+1) + "/" + str(len(json_templates_folder)))
            json_path_result = dir_path + "/json/json_result/" + each_json 
            each_json_path = json_places_path + each_json

            images_dict = json.loads(open(json_path_result).read())

            copy_dict = json.loads(open(each_json_path).read())

            for image_name in tqdm(images_dict.keys()):
                if image_name in copy_dict.keys():
                    images_dict[image_name]["io_score"] = copy_dict[image_name]["io_score"]
                    images_dict[image_name]["attributes"] = copy_dict[image_name]["attributes"]
                    images_dict[image_name]["categories"] = copy_dict[image_name]["categories"]

            sorted_data = {k: v for k, v in sorted(images_dict.items(), key=lambda item: item[0])}        
            with open(json_path_result, 'w') as jsonfile:
                json.dump(sorted_data, jsonfile, indent=4)   
        
    

















