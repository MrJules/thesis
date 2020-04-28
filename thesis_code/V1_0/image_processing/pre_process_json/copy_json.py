###################################################### IMPORT ######################################################

import json
import os
from tqdm import tqdm

####################################################### FUNCTIONS #################################################
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

####################################################### MAIN  ######################################################

if __name__ == '__main__' :

    print("")
    print("------------------------------------------JSON ACTIVITY AND LOCATION COPY SCRIPT ----------------------------------------- \n")


    dir_path = os.path.dirname(os.path.realpath(__file__))

    ground_path = dir_path + "/ground_data/data.json"
    ground_data = json.loads(open(ground_path).read())

    json_folder_path = dir_path + "/../json_result"
    json_folder = os.listdir(json_folder_path)
    if ".gitkeep" in json_folder : del json_folder[json_folder.index(".gitkeep")]


    for each_json in json_folder:
        image_data = []
        print("")
        print("Processing json: " + str(json_folder.index(each_json)+1) + "/" + str(len(json_folder)))
        if each_json.endswith(".json"):
            json_path = json_folder_path + "/" + each_json
            image_data = json.loads(open(json_path).read())

            for image_name in tqdm(image_data.keys()):
                for ground_image in ground_data.keys():
                    if image_name == ground_image:
                        image_data[image_name]["activity"] = ground_data[ground_image]["activity"]
                        image_data[image_name]["location"] = ground_data[ground_image]["location"]

            json.dump(image_data, open(json_path,"w"),indent=5)
































