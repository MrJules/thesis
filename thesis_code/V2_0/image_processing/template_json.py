import os
from tqdm import tqdm
import json


if __name__ == '__main__' :
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_folder_path = dir_path + "/images/"
    json_folder_path = dir_path + "/json/json_template/"

    for date_folder in os.listdir(image_folder_path):
        if not date_folder.startswith(".") :
            json_path = json_folder_path + date_folder + ".json"
            date_folder_path = image_folder_path + "/" + date_folder 
            images_dict = {}

            for name in tqdm(os.listdir(date_folder_path)):
                if not name.startswith(".") :

                    images_dict.update({name : {}})
                    if name[0] == "b" : local_time = name[17:21] + "-" + name[21:23] + "-" + name[23:25] + "_" + name[26:28] + ":" + name[28:30]
                    if name[0] == "B" : local_time = name[17:21] + "-" + name[21:23] + "-" + name[23:25] + "_" + name[26:28] + ":" + name[28:30]
                    if str(name[0]) == "2" :  local_time = name[0:4] + "-" + name[4:6] + "-" + name[6:8] + "_" + name[9:11] + ":" + name[11:13]
                    images_dict[name]["local_time"] = local_time
                    images_dict[name]["concepts"] = {}
                    images_dict[name]["activity"] = "NULL"
                    images_dict[name]["location"] = "NULL"
                    images_dict[name]["categories"] = {}
                    images_dict[name]["attributes"] = []
                    images_dict[name]["io_score"] = "NULL"

                    sorted_data = {k: v for k, v in sorted(images_dict.items(), key=lambda item: item[0])}
        
            with open(json_path, 'w') as jsonfile:
                json.dump(sorted_data, jsonfile, indent=4)

                    
                
