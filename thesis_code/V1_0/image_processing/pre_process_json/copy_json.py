###################################################### IMPORT ######################################################

import json
import os
from tqdm import tqdm

####################################################### MAIN  ######################################################

if __name__ == '__main__' :

    print("")
    print("------------------------------------------JSON ACTIVITY AND LOCATION COPY SCRIPT ----------------------------------------- \n")


    dir_path = os.path.dirname(os.path.realpath(__file__))

    ground_path = dir_path + "/ground_data/images.json"
    ground_data = json.loads(open(ground_path).read())

    image_path = dir_path + "/../json_result/image_data.json"
    image_data = json.loads(open(image_path).read())


    for image_name in tqdm(image_data.keys()):
        for ground_image in ground_data.keys():
            if image_name == ground_image:
                image_data[image_name]["activity"] = ground_data[ground_image]["activity"]
                image_data[image_name]["location"] = ground_data[ground_image]["location"]

    #iage_path = dir_path + "/../image_processing/json_result/image_data_2.json"

    json.dump(image_data, open(image_path,"w"),indent=5)
                































