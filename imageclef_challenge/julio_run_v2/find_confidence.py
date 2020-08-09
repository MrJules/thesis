###################################################### IMPORT ######################################################
import spacy
import simplejson as json
import os
import datetime 
import calendar
from tqdm import tqdm
from pathlib import Path
import csv


def Nmaxelements(list1, N): 
    final_list = [] 
    list_backup = list1.copy()
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    return final_list , list_backup

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

def find_score_concepts (images_data, text_data):
    final_score = 0
    max_scores = []
    temp_max_score = 0

    for data in text_data:
        scores = []
        for concept in images_data.keys():
                    temp_sim = data.similarity(nlp(concept))
                    if temp_sim > 0.3 :
                        temp_score = temp_sim * images_data[concept]["score"]
                        if temp_score > temp_max_score :
                            temp_max_score = temp_score
                        scores.append(temp_score)
        if scores : 
            max_scores.append(max(scores))
    if max_scores:
        final_score = sum(max_scores)/len(max_scores)
    final_score = temp_max_score


    return final_score 

def find_score_location (images_data, text_data):
    final_score = 0
    image_info = images_data

    for data in text_data:
        sim_score = data.similarity(nlp(image_info))
        if sim_score > final_score:
            final_score = sim_score
    return final_score

def find_score_activity (images_data, text_data):
    final_score = 0

    image_info = nlp(images_data)
    # procura a maior semelhança entre verbo ou a frase toda
    
    for data in text_data:
        temp_score = data.similarity(image_info)

        if temp_score > final_score:
            final_score = temp_score
   
    return final_score

def find_score_indoor_outdoor(images_data, text_data, image_name, json_image_key, json_text_key):
    final_score = 0

    if text_data[json_text_key] == True :
        final_score = 1 - float(images_data[image_name][json_image_key])
        return final_score

    if text_data[json_text_key] == False:
        final_score =  float(images_data[image_name][json_image_key])
        return final_score

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
        if each_file.endswith(".txt") or each_file.endswith(".csv"):
            os.remove(os.path.join(previous_file_path , each_file))
    ################################################################## clear previous .txt - end

    json_folder_path = os.path.join(dir_path , "json_images") 
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

    #while topic_count <= topic:
    while topic_count <= 10:
        print("")
        print("PROCESSING CONFIDENCE FOR TOPIC : " + str(topic_count) + "/10")
        print("")
        
        all_images = []
        all_scores = []

        text_data_path = dir_path + "/result_json_nlp/NLP_data_topic_" + str(topic_count) + ".json"
        text_data = json.loads(open(text_data_path).read())

        ############################## - Variables json - Begin
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
        
        ################################################################## - check status json - Begin
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
                change_weight = total_weight /1500
                weight_activity+= change_weight
                total_weight -= change_weight

            if location_flag == True:
                change_weight = total_weight / 1500
                weight_location += change_weight
                total_weight -= change_weight

            if indoor_outdoor_flag == True :
                change_weight = total_weight / 1000
                weight_indoor_outdoor += change_weight
                total_weight -= change_weight
        
        #negative_concept_flag = False
        #negative_activity_flag = False
        #negative_location_flag = False
        
    
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




        ######################################################### faster text processing
        if concept_flag == True : 
            nlp_relevant_things = []
            for data in text_data["relevant things"]:
                nlp_relevant_things.append(nlp(data))

        if activity_flag == True:
            nlp_activity = []
            for data in text_data["activities"]:
                nlp_activity.append(nlp(data))

        if location_flag == True:
            nlp_location = []
            for data in text_data["locations"]:
                nlp_location.append(nlp(data))

         ######################################################### faster text processing


        for each_json in json_folder:
            lines = []
            if each_json.endswith(".json"):
                print("Processing Json file :" + str(json_folder.index(each_json)+1) + "/" + str(len(json_folder)))

                json_path = os.path.join(json_folder_path, each_json)
                images_data = json.loads(open(json_path).read())

                for image_name in tqdm(images_data.keys()):
                    try : 
                        # ############################## - Variables Image- Begin
                        total_score = 0
                        total_positive_score = 0
                        total_negative_score = 0
                        score_activities = 0
                        score_date = 0
                        score_location = 0
                        score_indoor_outdoor = 0
                        
                        #
                        skip_flag = False
                        #
                        ############################## - Variables Image - End

                        ###########################o################################################################### - check if image as negative date - Begin

                        ################################################################################################## -  check date of image - Begin
                        if date_flag == True and skip_flag == False:
                            if images_data[image_name]["local_time"] == "NULL":
                                skip_flag = True # discard the image
                            else:
                                score_date = find_score_date(images_data, image_name, "local_time", day_data, year_data)
                                if score_date != 1: skip_flag = True # discard the image
                        ###########################################images_data, text_data, image_name, "location" , "negative locations##################################################### -  check date of image - End
                        
                        ################################################################################################## -  check concepts of image - Begin
                        if concept_flag == True and skip_flag == False:
                            if not images_data[image_name]["concepts"]:
                                skip_flag = True # discard the image
                            if images_data[image_name]["concepts"]:
                                    score_concepts = find_score_concepts(images_data[image_name]["concepts"], nlp_relevant_things) 
                                    if score_concepts < 0.15  : skip_flag = True
                        ################################################################################################### -  check concepts of image - End

                        ################################################################################################### -  check the rest - Begin
                        if skip_flag == False:
                            
                            if location_flag == True:
                                if images_data[image_name]["location"] != "NULL" :
                                    score_location =  find_score_location(images_data[image_name]["location"], nlp_location) 
                                
                            if activity_flag == True:    
                                if images_data[image_name]["activity"] != "NULL" : 
                                    score_activities = find_score_activity(images_data[image_name]["activity"], nlp_activity) 
                            
                            if indoor_outdoor_flag == True:
                                if images_data[image_name]["io_score"] != "NULL" :
                                    score_indoor_outdoor = find_score_indoor_outdoor(images_data, text_data, image_name, "io_score" , "inside")

                            total_positive_score = weight_concept * score_concepts + weight_location * score_location + weight_activity * score_activities + weight_indoor_outdoor * score_indoor_outdoor

                      
                        #################################################################################################### -  check the rest - End
                        
                        total_score = total_positive_score 

                        if total_score <= 0.25 : total_score = 0
                    
                        if total_score != 0 :
                        # line = text_data["topic"] + " , " + str(image_name) + " , " + str(total_score) + "\n"
                            #lines.append(line)
                            all_scores.append(total_score)
                            all_images.append(image_name)
                    
                    except : print ("Error ocurred reading : ", image_name)
                    
        top_50, all_scores = Nmaxelements(all_scores, 50)
        
        for score in top_50 :
            index = all_scores.index(score)
            top_images = all_images[index]
            line = text_data["topic"] + " , " + str(top_images) + " , " + str(score) + "\n"
            txt_path = dir_path + "/results_confidence/confidence_score.csv"
            f = open(txt_path,"a+") 
            f.write(line)
            f.close()
                    
        topic_count += 1 


 
    

