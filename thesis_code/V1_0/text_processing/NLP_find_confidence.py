###################################################### IMPORT ######################################################

import spacy
import json
import os
import datetime 
import calendar
from tqdm import tqdm

###################################################### FUNCTIONS ######################################################
def find_score (images_data, text_data,image_name, json_image_key,json_text_key):

    final_score = 0
    no_verb_flag = True

    if json_image_key == "concepts":
        max_scores = []

        for data in text_data[json_text_key]:
        
            temp_max_score = 0
            for concept in images_data[image_name][json_image_key].keys():
                sim_score = nlp(data).similarity(nlp(concept))
                
                temp_score = sim_score * images_data[image_name][json_image_key][concept]["score"]
                if temp_score > temp_max_score:
                    temp_max_score = temp_score
       
            max_scores.append(temp_max_score)
        final_score = sum(max_scores)/len(max_scores)
        return final_score  

    if json_image_key == "categories":
        indoor_score , outdoor_score = find_indoor_outdoor(images_data, image_name, json_image_key)

        if text_data[json_text_key] == True:
            final_score = indoor_score

        if text_data[json_text_key] == False:
            final_score = outdoor_score       

        return final_score  
        
    if json_image_key == "activity":
        image_info = images_data[image_name][json_image_key]

        # procura a maior semelhança entre verbo ou a frase toda
        for data in text_data[json_text_key]:
            data_nlp = nlp(data)

            temp_score = data_nlp.similarity(nlp(image_info))

            if temp_score > final_score:
                    final_score = temp_score

            for token in data_nlp:
                if token.pos_ == "VERB":     
                    temp_score = token.similarity(nlp(image_info))
               

                    if temp_score > final_score:
                        final_score = temp_score

        return final_score            

    if json_image_key == "local_time":
        year = images_data[image_name][json_image_key][0:4]
        month = images_data[image_name][json_image_key][5:7]
        day = images_data[image_name][json_image_key][8:10]
        date = day + " " + month + " " + year
        day_of_week = findDay(date)
        day_of_week = day_of_week.lower()
        year_data = []
        day_data = []

        for data in text_data[json_text_key]:
            if data.isdigit():
                year_data.append(data)
            if data == "weekend":
                day_data.append("saturday")
                day_data.append("sunday")
            if not data.isdigit() and data != "weekend":
                if data not in day_data : day_data.append(data)
                
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

        final_score = 0
        return final_score  
    
    else: 
        image_info = images_data[image_name][json_image_key]

        for data in text_data[json_text_key]:
            sim_score = nlp(data).similarity(nlp(image_info))
            temp_score = sim_score

            if temp_score > final_score:
                final_score = temp_score
                
        
        return final_score


def find_indoor_outdoor(images_data, image_name, json_image_key):
    file_path = dir_path + "/files/IO_places365.txt"
    max_1_score = 0
    max_2_score = 0
    image_indoor = "NULL"
    error = 0
    
    
    for data in images_data[image_name][json_image_key]:
        file = open(file_path, "r")
        flag_do = True
        for line in file:
            line_proc = line[3:len(line)-1]
            letter = line[1]
            if data[0] == letter:
                if data in line_proc :
                    for number in line_proc:
                        if number.isdigit():
                            if flag_do == True:

                                if number == "1":
                                    max_1_score = max_1_score  + images_data[image_name][json_image_key][data]
                                
                                if number == "2": 
                                    max_2_score = max_2_score  + images_data[image_name][json_image_key][data]

                                flag_do = False
            
    
    return max_1_score, max_2_score

def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born])
#################################################################################### MAIN  #################################################################################

if __name__ == '__main__' :
    print("")
    print("-----------------------------------------------CONFIDENCE CALCULATION SCRIPT----------------------------------------- \n")
    print("LOADING NLP MODEL ... ")
    nlp = spacy.load("en_core_web_md")     
    dir_path = os.path.dirname(os.path.realpath(__file__))
    


    previous_file =os.listdir( dir_path + "/results_confidence")
    previous_file_path = dir_path + "/results_confidence"

    for each_file in previous_file:
        if each_file.endswith(".txt"):
            os.remove(previous_file_path + "/" + each_file)



    topic_count = 1 

    while topic_count <= 10:

        text_data = dir_path + "/result_json_nlp/NLP_data_topic_" + str(topic_count) + ".json"
        images_data = dir_path + "/../image_processing/json_result/image_data.json"

        text_data = json.loads(open(text_data).read())
        images_data = json.loads(open(images_data).read())


        returned_images = []
        count_images = 0
        count_returned = 0
        
        print("PROCESSING CONFIDENCE FOR TOPIC : " + str(topic_count) + "/10")
        for image_name in tqdm(images_data.keys()):

            category_score = 0
            category_score_array = []
            temp_category_score = 0

            score_concepts = 0
            score_location = 0
            score_activities = 0
            score_date = 0
            score_indoor_outdoor = 0
            total_positive_score = 0
            total_score = 0
            
            empty = 0

            concept_flag = True
            location_flag = True
            activity_flag = True
            time_flag = True
            indoor_outdoor_flag = True

            negative_score_concepts = 0
            negative_score_location = 0
            negative_score_activities = 0
            negative_score_date = 0

            negative_empty = 0

            negative_concept_flag = True
            negative_location_flag = True
            negative_activity_flag = True
            negative_time_flag = True
            total_negative_score = 0

            #################################################################### NEGATIVE SCORE #################################################################################
            if not text_data["negative relevant thing"]:
                negative_empty = empty + 1
                negative_concept_flag = False

            if not text_data["negative activities"]:
                negative_empty = empty + 1 
                negative_location_flag = False

            if not  text_data["negative locations"]:
                negative_empty = empty + 1 
                negative_activity_flag = False

            if not text_data["negative dates"]:
                negative_empty = empty + 1
                negative_time_flag = False 

            if negative_empty != 4 : 
                if negative_concept_flag == True:
                    negative_score_concepts = 1 / (4 - empty) * find_score(images_data, text_data, image_name, "concepts" , "negative relevant thing")

                if negative_location_flag == True:
                    negative_score_location = 1 / (4 - empty) * find_score(images_data, text_data, image_name, "location", "negative locations")
                    
                if negative_activity_flag == True:
                    negative_score_activities = 1 / (4 - empty) *  find_score(images_data, text_data, image_name, "activity", "negative activities")
                    
                if negative_time_flag == True:
                    negative_score_date = 1 / (4 - empty) * find_score(images_data, text_data, image_name, "local_time", "negative dates")

            total_negative_score = abs(negative_score_concepts + negative_score_location + negative_score_activities + negative_score_date )
            #print ("Negative score: ", total_negative_score)

            

            #################################################################### POSITIVE SCORE #################################################################################
            if not text_data["relevant things"]: # empty
                empty = empty + 1
                concept_flag = False

            if not text_data["locations"]:
                empty = empty + 1 
                location_flag = False

            if not text_data["activities"]:
                empty = empty + 1 
                activity_flag = False

            if not text_data["dates"]:
                empty = empty + 1
                time_flag = False 

            if text_data["inside"] == "NULL" or text_data["outside"] == "NULL" :
                empty = empty + 1
                indoor_outdoor_flag = False

            if indoor_outdoor_flag == True:
                for category in images_data[image_name]["categories"]:
                    category_score = images_data[image_name]["categories"][category]
                    category_score_array.append(category_score)
                    
                    if category_score > temp_category_score :
                        temp_category_score = category_score     
                
                if temp_category_score < 0.15 :
                    empty = empty + 1
                    indoor_outdoor_flag = False

            
            if empty != 5:
                div = 1

                if empty == 4: div = 2
                if empty != 4: div = 1
                if location_flag == False and concept_flag == False: div = 2
                
                if concept_flag == True: 
                    if images_data[image_name]["concepts"]:
                        score_concepts = 1 / (5 - empty) * find_score(images_data, text_data, image_name, "concepts" , "relevant things") 
                    if not images_data[image_name]["concepts"]:
                        score_concepts = 0


                if location_flag == True:
                    if images_data[image_name]["location"] == "NULL" : 
                        score_location = 0
                    else:
                        score_location = 1 / (5 - empty) * find_score(images_data, text_data, image_name, "location" , "locations") 
                    
                if activity_flag == True:    
                    if images_data[image_name]["activity"] == "NULL" : 
                        score_activities = 0
                    else:
                        score_activities = 1 / (5 - empty) * find_score(images_data, text_data, image_name, "activity" , "activities") 
                

                if time_flag == True: 
                    if images_data[image_name]["local_time"] == "NULL" :
                        score_date = 0
                    else:
                        score_date = 1 / (5 - empty) * find_score(images_data, text_data, image_name, "local_time" , "dates") 
                
                if indoor_outdoor_flag == True:
                    if images_data[image_name]["categories"] == "NULL":
                        score_indoor_outdoor = 0
                    else:
                        score_indoor_outdoor = 1 / (5 - empty) * find_score(images_data, text_data, image_name, "categories" , "inside") 

                total_positive_score = (score_concepts + score_location + score_activities + score_date + score_indoor_outdoor)/div

            total_score = total_positive_score - total_negative_score


            txt_path = dir_path + "/results_confidence/results_topic_" + text_data["topic"] + ".txt"
            f = open(txt_path,"a+")
            line = text_data["topic"] + " , " + str(image_name) + " , " + str(total_score) + "\n"
            f.write(line)
            f.close()       

       
        topic_count = topic_count + 1

  