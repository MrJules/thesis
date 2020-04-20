###################################################### IMPORT ######################################################

import spacy
import json
import os

###################################################### FUNCTIONS ######################################################

def find_negative (images_data, text_data, returned_images,image_name, json_image_key,json_text_key):

    if json_image_key == "concepts":
        for concept in images_data[image_name][json_image_key].keys():
            image_info = concept
            if image_name not in returned_images: break
                
            for negative_data in text_data[json_text_key]:
        
                if image_name not in returned_images : break
        
                if nlp(negative_data).similarity(nlp(image_info)) >= 0.8:
                    del returned_images[returned_images.index(image_name)]
                    print("Negative picture", image_name)
                    return returned_images 
        return returned_images     
    if json_image_key == "local_time":
        image_info = images_data[image_name][json_image_key][0:4]
    else:
        image_info = images_data[image_name][json_image_key]
    

    for negative_data in text_data[json_text_key]:
        
        if image_name not in returned_images : break
        
        if nlp(negative_data).similarity(nlp(image_info)) >= 0.8:
            del returned_images[returned_images.index(image_name)]
            print("Negative picture", image_name)
    return returned_images


def find_image (images_data, text_data, returned_images,image_name, json_image_key,json_text_key):
    sim_score = 0.8
    
    if json_image_key == "concepts":
        for concept in images_data[image_name][json_image_key].keys():
            image_info = concept
            for data in text_data[json_text_key]:

                if nlp(data).similarity(nlp(image_info)) >= sim_score and image_name not in returned_images:
                    returned_images.append(image_name)
                    print("Saved" , image_name)
                    return returned_images
        
        return returned_images  

    if json_image_key == "local_time":
        image_info = images_data[image_name][json_image_key][0:4]
        sim_score = 1

    else:
        image_info = images_data[image_name][json_image_key]

    for data in text_data[json_text_key]:
        if nlp(data).similarity(nlp(image_info)) >= sim_score and image_name not in returned_images:
            returned_images.append(image_name)
            print("Saved" , image_name)
            return returned_images
                
    return returned_images

###################################################### MAIN ######################################################

if __name__ == '__main__' :

    dir_path = os.path.dirname(os.path.realpath(__file__))
    text_data = dir_path + "/NLP_data.json"
    images_data = dir_path + "/small_data.json"

    text_data = json.loads(open(text_data).read())
    images_data = json.loads(open(images_data).read())

    nlp = spacy.load("en_core_web_md")  # make sure to use larger model

    returned_images = []

    count_images = 0
    count_returned = 0


    # Find positives
    for image_name in images_data.keys():
        print(image_name)
        returned_images = find_image(images_data, text_data, returned_images, image_name, "concepts" , "relevant things")
        returned_images = find_image(images_data, text_data, returned_images, image_name, "location" , "locations")
        returned_images = find_image(images_data, text_data, returned_images, image_name, "activity" , "activities")
        returned_images = find_image(images_data, text_data, returned_images, image_name, "local_time" , "dates")

        count_images = count_images + 1

        # if score > 0.8 : returned_images.append()
    count_returned = len(returned_images)

    ### Find Negatives
    for image_name in returned_images:
        print(image_name)
        returned_images = find_negative(images_data, text_data, returned_images, image_name, "concepts" , "negative relevant thing")
        returned_images = find_negative(images_data, text_data, returned_images, image_name, "location", "negative locations")
        returned_images = find_negative(images_data, text_data, returned_images, image_name, "activity", "negative activities")
        returned_images = find_negative(images_data, text_data, returned_images, image_name, "local_time", "negative dates")

    count_final = len(returned_images)    

    print("Returned Images : ",returned_images)
    print("")
    print("Total images analysed :" , count_images)
    print("Total images with positve features :" , count_returned)
    print("Total images with negative features (deleted) :" , count_returned - count_final)
    print("Total images returned:" , count_final)
    print("")
