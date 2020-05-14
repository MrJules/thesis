###################################################### IMPORT ######################################################
import spacy
import json
import os
import datetime 
import calendar
from tqdm import tqdm
from pathlib import Path

###################################################### FUNCTIONS ######################################################
def find_score_date (images_data,image_name, json_image_key, day_data, year_data):
    final_score = 0

    year = images_data[image_name][json_image_key][0:4]
    month = images_data[image_name][json_image_key][5:7]
    day = images_data[image_name][json_image_key][8:10]
    date = day + " " + month + " " + year
    day_of_week = findDay(date)
    day_of_week = day_of_week.lower()
   
    if not year_data:
        for days in day_data:
            if days == day_of_week:
                final_score = 1
                return final_score

    if not day_data:
        for years in year_data:
            if years == year:
                final_score = 1
                return final_score

    if year_data and day_data:
        for years in year_data:
            if years == year:
                for days in day_data:
                    if days == day_of_week:
                        final_score = 1
                        return final_score
    return final_score 
    
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born])

def find_score_concepts (images_data, text_data,image_name, json_image_key,json_text_key):
    final_score = 0
    max_scores = []

    for data in text_data[json_text_key]:
        scores = []
        for concept in images_data[image_name][json_image_key]: #images_data[image_name][json_image_key].keys()
                for i in concept.keys():
                    temp_sim = nlp(data).similarity(nlp(i))
                    if temp_sim > 0.35 :
                        #temp_score = temp_sim * images_data[image_name][json_image_key][concept]["score"]
                        temp_score = temp_sim * concept[i]["score"]
                        scores.append(temp_score)
        if scores : 
            max_scores.append(max(scores))
    if max_scores:
        final_score = sum(max_scores)/len(max_scores)
    #final_score = temp_max_score


    return final_score 

def find_score_location (images_data, text_data,image_name, json_image_key,json_text_key,):
    final_score = 0
    image_info = images_data[image_name][json_image_key]

    for data in text_data[json_text_key]:
        sim_score = nlp(data).similarity(nlp(image_info))
        if sim_score > final_score:
            final_score = sim_score
    return final_score

def find_score_activity (images_data, text_data,image_name, json_image_key,json_text_key):
    final_score = 0
    image_info = images_data[image_name][json_image_key]
    # procura a maior semelhança entre verbo ou a frase toda
    for data in text_data[json_text_key]:
        temp_score = nlp(data).similarity(nlp(image_info))

        if temp_score > final_score:
                final_score = temp_score

        for token in nlp(data):
            if token.pos_ == "VERB":     
                temp_score = token.similarity(nlp(image_info))
                if temp_score > final_score:
                    final_score = temp_score

    return final_score

def find_score_indoor_outdoor(images_data, text_data, image_name, json_image_key, json_text_key):
    final_score = 0

    if text_data[json_text_key] == True :
        final_score = 1 - images_data[image_name][json_image_key]

    if text_data[json_text_key] == False:
        final_score =  images_data[image_name][json_image_key]

    else :
        return final_score


########################################################   MAIN  #######################################################

if __name__ == '__main__':
    print("")
    print("-----------------------------------------------CONFIDENCE CALCULATION SCRIPT----------------------------------------- \n")
    print("")
    print("LOADING NLP MODEL ... ")

    nlp = spacy.load("en_core_web_md")     
    ################################################################## clear previous .txt - begin
    dir_path = os.path.dirname(os.path.realpath(__file__))
    previous_file_path = os.path.join(dir_path, "results_confidence")

 
    for each_file in os.listdir(previous_file_path):
        if each_file.endswith(".txt"):
            os.remove(os.path.join(previous_file_path , each_file))
    ################################################################## clear previous .txt - end

    json_folder_path = os.path.join(dir_path , "../image_processing/json/json_result") 
    json_folder = os.listdir(json_folder_path)
    if ".gitkeep" in json_folder : del json_folder[json_folder.index(".gitkeep")]
    
    json_result_folder = os.path.join(dir_path, "result_json_nlp")

    topic = 0
    for each_file in os.listdir(json_result_folder):
        if each_file.endswith(".json"):
            topic += 1
    

    ######################################################################################### TOPIC START - BEGIN
    topic_count = 1
    ######################################################################################### TOPIC START - END

    while topic_count <= topic:
        print("")
        print("PROCESSING CONFIDENCE FOR TOPIC : " + str(topic_count) + "/10")
        print("")
        
        text_data_path = dir_path + "/result_json_nlp/NLP_data_topic_" + str(topic_count) + ".json"
        text_data = json.loads(open(text_data_path).read())

        ############################## - Variables json - Begin
        empty = 1
        #
        date_flag = True
        concept_flag = True
        location_flag = True
        activity_flag = True
        indoor_outdoor_flag = True
        #
        total_weight = 1 
        weight_concept = 0
        weight_activity = 0
        weight_indoor_outdoor = 0
        weight_location = 0
        change_weight = 0
        #
        negative_concept_flag = True
        negative_activity_flag = True
        negative_location_flag = True
        negative_date_flag = True
        #
        negative_total_weight = 0.35
        negative_weight_concept = 0
        negative_weight_activity = 0
        negative_weight_location = 0
        negative_change_weight = 0
        #
        lines = []
        #
        ################################################################## - check status json - Begin
        ##########   negatives
        if not text_data["negative relevant thing"]:
            negative_concept_flag = False

        if not text_data["negative activities"]:
            negative_activity_flag = False

        if not text_data["negative locations"]:
            negative_location_flag = False

        if not text_data["negative dates"]:
            negative_date_flag = False
        ##########   positives
        if not text_data["dates"]:
            date_flag = False

        if not text_data["relevant things"]:
            concept_flag = False
           
        if not text_data["locations"]:
            location_flag = False

        if not text_data["activities"]:
            activity_flag = False
 
        if text_data["inside"] == "NULL" or text_data["outside"] == "NULL" :
            indoor_outdoor_flag = False

        ################################################################## - check status - END
        
        ################################################################## - adjust weights - Begin
       
        while total_weight > 1e-10:

            if concept_flag == True:
                change_weight = total_weight/600
                weight_concept += change_weight
                total_weight -=  change_weight
                
            if activity_flag == True:
                change_weight = total_weight / 1500
                weight_activity+= change_weight
                total_weight -= change_weight

            if location_flag == True:
                change_weight = total_weight / 1500
                weight_location += change_weight
                total_weight -= change_weight

            if indoor_outdoor_flag == True :
                change_weight = total_weight / 2000
                weight_indoor_outdoor += change_weight
                total_weight -= change_weight
        
        #negative_concept_flag = False
        #negative_activity_flag = False
        #negative_location_flag = False
        
        if negative_concept_flag == True or negative_activity_flag == True or negative_location_flag == True:
            while negative_total_weight > 1e-10:

                if negative_concept_flag == True:
                    negative_change_weight = negative_total_weight / 1000
                    negative_weight_concept += negative_change_weight
                    negative_total_weight -=  negative_change_weight
                    
                if negative_activity_flag == True:
                    negative_change_weight = negative_total_weight / 2500
                    negative_weight_activity += negative_change_weight
                    negative_total_weight -= negative_change_weight

                if negative_location_flag == True:
                    negative_change_weight = negative_total_weight / 2500
                    negative_weight_location += negative_change_weight
                    negative_total_weight -= negative_change_weight

        
        ################################################################## - adjust weights - End
        if negative_date_flag == True:
            negative_year_data = []
            negative_day_data = []
            for data in text_data["negative dates"]:
                if data.isdigit():
                    negative_year_data.append(data)
                if data == "weekend":
                    negative_day_data.append("saturday")
                    negative_day_data.append("sunday")
                if not data.isdigit() and data != "weekend":
                    if data not in day_data : negative_day_data.append(data)
        ########################################################## - text dates - begin
        if date_flag == True:
            year_data = []
            day_data = []
            for data in text_data["dates"]:
                if data.isdigit():
                    year_data.append(data)
                if data == "weekend":
                    day_data.append("saturday")
                    day_data.append("sunday")
                if not data.isdigit() and data != "weekend":
                    if data not in day_data : day_data.append(data)
        ########################################################## - text dates - End 

        for each_json in json_folder:
            if each_json.endswith(".json"):
                print("Processing Json file :" + str(json_folder.index(each_json)+1) + "/" + str(len(json_folder)))

                json_path = os.path.join(json_folder_path, each_json)
                images_data = json.loads(open(json_path).read())

                for image_name in tqdm(images_data.keys()):
                    
                    # ############################## - Variables Image- Begin
                    total_score = 0
                    total_positive_score = 0
                    total_negative_score = 0
                    #
                    score_concepts = 0
                    score_activities = 0
                    score_date = 0
                    score_location = 0
                    score_indoor_outdoor = 0
                    #
                    negative_score_concepts = 0
                    negative_score_location = 0
                    negative_score_activities = 0
                    negative_score_date = 0
                    #
                    skip_flag = False
                    #
                    ############################## - Variables Image - End

                    ###########################o################################################################### - check if image as negative date - Begin
                    if negative_date_flag == True and skip_flag == False:
                        if images_data[image_name]["local_time"] == "NULL":
                            skip_flag = True # discard the image
                        else:
                            negative_score_date = find_score_date(images_data, image_name, "local_time", negative_day_data, negative_year_data)
                            if negative_score_date == 1: skip_flag = True # discard the image
                    ############################################################################################## - check if image as negative - End

                    ################################################################################################## -  check date of image - Begin
                    if date_flag == True and skip_flag == False:
                        if images_data[image_name]["local_time"] == "NULL":
                            skip_flag = True # discard the image
                        else:
                            score_date = find_score_date(images_data, image_name, "local_time", day_data, year_data)
                            if score_date != 1: skip_flag = True # discard the image
                    ################################################################################################## -  check date of image - End
                    
                    ################################################################################################## -  check concepts of image - Begin
                    if concept_flag == True and skip_flag == False:
                        if not images_data[image_name]["concepts"]:
                            skip_flag = True # discard the image
                        if images_data[image_name]["concepts"]:
                                score_concepts = find_score_concepts(images_data, text_data, image_name, "concepts" , "relevant things") 
                                if score_concepts < 0.3  : skip_flag = True
                    ################################################################################################### -  check concepts of image - End

                    ################################################################################################### -  check the rest - Begin
                    if skip_flag == False:
                        
                        if location_flag == True:
                            if images_data[image_name]["location"] != "NULL" :
                                score_location =  find_score_location(images_data, text_data, image_name, "location" , "locations") 
                            
                        if activity_flag == True:    
                            if images_data[image_name]["activity"] != "NULL" : 
                                score_activities = find_score_activity(images_data, text_data, image_name, "activity" , "activities") 
                        
                        if indoor_outdoor_flag == True:
                            if images_data[image_name]["io_score"] != "NULL" or images_data[image_name]["io_score"] != {}:
                                score_indoor_outdoor = find_score_indoor_outdoor(images_data, text_data, image_name, "io_score" , "inside")

                        total_positive_score = weight_concept * score_concepts + weight_location * score_location + weight_activity * score_activities + weight_indoor_outdoor * score_indoor_outdoor

                        if negative_location_flag == True:
                            if images_data[image_name]["location"] != "NULL" :
                                negative_score_location = find_score_location(images_data, text_data, image_name, "location" , "negative locations") 
                        
                        if negative_activity_flag == True:
                            if images_data[image_name]["activity"] != "NULL" : 
                                negative_score_activities = find_score_activity(images_data, text_data, image_name, "activity" , "negative activities")

                        if negative_concept_flag == True : 
                            if images_data[image_name]["concepts"] != []:
                                negative_score_concepts = find_score_concepts(images_data, text_data, image_name, "concepts" , "negative relevant thing") 

                        total_negative_score = negative_weight_concept * negative_score_concepts + negative_weight_activity * negative_score_activities + negative_weight_location * negative_score_location
                    #################################################################################################### -  check the rest - End
                    
                    total_score = total_positive_score - total_negative_score
                    if total_score < 0.25 : total_score = 0
                    if total_score != 0 :
                        line = text_data["topic"] + " , " + str(image_name) + " , " + str(total_score) + "\n"
                        lines.append(line)

        txt_path = dir_path + "/results_confidence/results_topic_" + text_data["topic"] + ".txt"
        f = open(txt_path,"a+")
        for line in lines:
            f.write(line)
        f.close()
        
        topic_count += 1 


 
    

