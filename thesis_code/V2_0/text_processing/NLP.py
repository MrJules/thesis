import spacy
import json
import os
from tqdm import tqdm

if __name__ == '__main__' :
        
    # Load English tokenizer, tagger, parser, NER and word vectors
    print("")
    print("-----------------------------------------------TEXT PROCESSING SCRIPT----------------------------------------- \n")
    print("LOADING NLP MODEL ... \n")
    nlp = spacy.load("en_core_web_md")
    # nlp = spacy.load("en_core_web_md") # medium model

    ####################################################################### imageClef Topics #############################################################################################
    topic_array = [1,2,3,4,5,6,7,8,9,10]
    
    print("PROCESSING TEXT")
    for topic_count in tqdm(topic_array):

        if topic_count == 1:
            #[TOPIC 1]
            topic = "1"
            text_title = "Having Beers in a Bar"
            text_description  = "Find the moment in 2015 and 2016 when u1 enjoyed beers in the bar"
            text_narrative= "To be considered relevant, u1 must be clearly in a bar. Any moments that u1 drinks beers at home or outside without the bar view are not considered relevant."

        if topic_count == 2:
            #[TOPIC 2]
            topic = "2"
            text_title = "Building Personal Computer"
            text_description  = "Find the moment when u1 built my personal computer from scratch."
            text_narrative= "To be considered relevant, u1 must be clearly at the office with the PC parts on the table. Any moments that the u1 is not in the office or there are no PC parts/uncompleted PCs on the table are not considered relevant."


        if topic_count == 3:
            #[TOPIC 3]
            topic = "3"
            text_title = "In A Toy Shop"
            text_description  = "Find the moment when u1 was looking at items in a toyshop."
            text_narrative= "To be considered relevant, u1 must be clearly in a toyshop. Various toys are being examined, such as electronic trains, model kits and board games. Being in an electronics store, or a supermarket, are not considered to be relevant."


        if topic_count == 4:
            #[TOPIC 4]
            topic = "4"
            text_title = "Television Recording"
            text_description  = "Find the moments when u1 was being recorded for a television show."
            text_narrative= "To be considered relevant, there must clearly be a television camera in front of u1. The moments the interviewer/cameramen is interviewing/recording u1 are also considered relevant. This can take place at home or in another location. All recording took place in one day and in more than one location."


        if topic_count == 5:
            #[TOPIC 5]
            topic = "5"
            text_title = "Public Transport In Home Country"
            text_description  = "Find the moments in 2015 and 2018 when u1 was using public transports in my home country (Ireland)."
            text_narrative= "Taking any form of public transport in Ireland is considered relevant, such as bus, taxi, train and boat. The moments that u1 is driving a car is not relevant."


        if topic_count == 6:
            #[TOPIC 6]
            topic = "6"
            text_title = "Seaside Moments"
            text_description  = "Find moment(s) in which u1 was walking by the sea taking photos or eating ice cream."
            text_narrative= "To be considered relevant, u1 must be taking a walk by the sea or eating ice cream and the sea is clearly visible. u1 must also be shown taking a photo with his/her camera phone or holding the ice cream cone at this time. On the beach or walking on a pier are both considered relevant once u1 is taking a photo or eating ice cream."


        if topic_count == 7 : 
            #[TOPIC 7]
            topic = "7"
            text_title = "Grocery Stores"
            text_description  = "Find moment(s) in 2016 and 2018 when u1 was grocery shopping on the weekends."
            text_narrative= "To be considered relevant, u1 must be clearly in a grocery shop and buy something from it. Any moments on Saturdays and Sundays when u1 was in a grocery store and visibly interacting with products are also considered relevant."

        if topic_count == 8 : 
            #[TOPIC 8]
            topic = "8"
            text_title = "Photograph of The Bridge"
            text_description  = "Find the moment when u1 was taking a photo of a bridge."
            text_narrative= "Moments when u1 was walking on a street without stopping to take a photo of a bridge are not relevant. Any other moment showing a bridge when a photo was not being taken are also not considered to be relevant."

        if topic_count == 9 :
            #[TOPIC 9]
            topic = "9"
            text_title = "Car Repair"
            text_description  = "Find the moment when u1 was repairing his car in the garden."
            text_narrative= "Moments when u1 was repairing his car in the garden with the gloves on his hand. Sometimes, he also held the hammer and his phone and these moments are also considered relevant. The moments when u1 was with the cars without showing repair action are not considered relevant."

        if topic_count == 10 :
            #[TOPIC 10]
            topic = "10"
            text_title = "Monsters"
            text_description  = "Find the moment(s) when u1 was looking at an old clock, with flowers visible, with a small monster watching u1."
            text_narrative= "Moments when u1 was at home, looking at an old clock, with flowers visible, with a lamp and perhaps two small monsters watching u1 are considered relevant. One of the monsters might be a long rabbit. The moments without one of the aforementioned conditions: monsters, flowers, and old clock are not considered relevant."

        #######################################################################################################################################################
        '''
        #[TOPIC 1] - 2019
        text_title = "Icecream by the sea"
        text_description = "Find the moment when u1 was eating an icecream beside the sea."
        text_narrative = "To be relevant, the moment must show both the ice cream with cone in the hand of u1 as well as the sea clearly visible. Any moments by the sea, or eating an ice cream which do not occur together are not considered to be relevant. "
        '''

        '''
        #[TOPIC 2] - 2019
        text_title = "Having food in a restaurant"
        text_description = "Find the moment when u1 was eating food or drinking in a restaurant."
        text_narrative = "U1 was eating food in a restaurant while away from home. Any kinds of dishes are relevant. Only Drinking coffee and have dessert in a cafe won't be relevant"
        '''

        '''
        #[TOPIC 3] - 2019
        text_title = "Watching Videos"
        text_description = "Find the moment when u1 was watching video when using other digital devices."
        text_narrative = "To be relevant, u1 must be watching videos in any location and any digital devices can be considered. For example: TV machine, tablet, mobile phone, laptop, desktop computer."
        '''
        '''
        #[TOPIC 5] - 2019
        text_title = "Photograph of a Bridges"
        text_description = "Find the moment when u1 was taking a photo of a bridge."
        text_narrative = "U1 was walking on a pedestrian street and stopped to take a photo of a bridge. Moments when u1 was walking on a street without stopping to take a photo of a bridge are not relevant. Any other moment showing a bridge when a photo was not being taken are also not considered to be relevant."
        '''

        '''
        #[TOPIC 5] - 2019
        text_title = "Grocery shopping"
        text_description = "Find the moment when u1 was shopping for food in a grocery shop."
        text_narrative = "To be considered relevant, u1 must be clearly in a grocery shop and bought something from the it"
        '''
        '''
        #[TOPIC 6] - 2019
        text_title = "Playing a Guitar"
        text_description = "Find the moment when U1 or a man is playing guitar in view."
        text_narrative = " Any use of guitars indoors could be considered relevant. Any type of Guitar could be considered as relevant."
        '''

        '''
        #[TOPIC 7] - 2019
        text_title = "Cooking"
        text_description = "Find moments when u1 was cooking food."
        text_narrative = "The moments shows U1 was cooking food at any places are relevant"
        '''
        '''
        #[TOPIC 8] - 2019
        text_title = "Car Sales Showroom"
        text_description = "Find the moments when u1 was in a car sales showroom."
        text_narrative = " u1 visited a car sales showroom a few times. Relevant moments show u1 indoors in a car sales showroom, either looking at cars or waiting for a salesman sitting at a table. Any moments looking at cars while outside of a showroom are not considered relevant"
        '''
        '''
        #[TOPIC 10] - 2019
        text_title = "Paper or book reviewing"
        text_description = "Find all moments when u1 was reading a paper or book."
        text_narrative = "To be relevant, the paper or book must be visible in front of U1 and sometimes U1 use a pen to mark on the paper or book"
        '''
        ############################################################### Pre-processamento do texto ########################################################

        text_narrative = text_narrative.split(".")
        if "" in text_narrative:
            del text_narrative[text_narrative.index("")]

        text_narrative_final =[]
        negative_sentences = []
        for narrative in text_narrative:
            if  narrative.endswith("not considered to be relevant") or narrative.endswith("not considered relevant") or narrative.endswith("is not relevant") or narrative.endswith("are not relevant"):
                negative_sentences.append(narrative)
                break
            else : 
                text_narrative_final.append(narrative) 


        texts_unprocessed = []
        texts = []
        texts_unprocessed.append(text_title)
        texts_unprocessed.append(text_description)

        for narrative in text_narrative_final:
            texts_unprocessed.append(narrative)

        negative_text =[]



        if "" in texts_unprocessed : del texts_unprocessed[texts_unprocessed.index("")]

        for text in texts_unprocessed:
            text = text.lower()
            #text = text.replace(".","")
            #text = text.replace(",","")
            if text.startswith("find moment(s) in which"):
                text = text[25:]

            if text.startswith("find the moments") : 
                #text.strip('find the moment')
                text = text[17:] 

            if text.startswith("find the moment") : 
                #text.strip('find the moment')
                text = text[16:] 

            if text.startswith("find moments") : 
                #text.strip('find the moment')
                text = text[13:] 

            if text.startswith("to be considered relevant") :
                text = text[26:]

            if text.startswith("the moments") :
                text = text[12:]

            if text.startswith("find all moments") :
                text = text[17:]

            if text.startswith(" relevant moments"):
                text = text[18:]

            if text.startswith(" any moments"):
                text = text[13:]
            texts.append(text)

        # garante que as frases negativas ficam no fim
        for text in negative_sentences:
            text = text.lower()
            negative_text.append(text)
            texts.append(text)
            

        activities = []
        positive_activities = []
        negative_activities = []

        locations = []
        positive_locations = []
        negative_locations = []

        relevant_things = []
        positive_relevant_things = []
        negative_relevant_things = []

        dates = []
        positive_dates = []
        negative_dates = []

        other_things = []
        other_words = []
        location_or_thing = []

        inside_flag = False
        outside_flag = True

        # arrays para os chunk
        chunk_activites = []
        chunk_relevant_things = []
        chunk_locations = []

        flag_delete = 0
        days_week = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday", "weekend"]
        days_week_plural = ["mondays", "tuesdays", "wednesdays", "thursdays", "fridays", "saturdays", "sundays", "weekends"]
        ################################################################################## INICIO ############################################################################

        for text in texts:
            pos = 0
            count = 0
            doc = nlp(text)
            
            

            if text in negative_text:
                flag_delete += 1

                if flag_delete ==  1:
                    relevant_things = []
                    activities = []
                    locations = []
                    dates = []
                
            for token in doc :

                # >>>>>>>> Procura as datas

                if token.pos_ == "NUM" and token.text.isdigit():
                    dates.append(token.text)
                
                if token.text in days_week_plural:
                    index = days_week_plural.index(token.text)
                    dates.append(days_week[index])

                if token.text in days_week:
                    if token.text not in dates:
                        dates.append(token.text)

                if token.pos_ == "ADV":
                    if token.text == "inside" or token.text == "outside":
                        if pos + 1 < len(doc) and doc[pos +1].pos_ == "ADP":
                            if pos + 2  < len(doc) and doc[pos +2 ].pos_ == "DET":
                                if pos +3  < len(doc) and doc[pos +3].pos_ == "NOUN" and doc[pos + 3 ].dep_ == "pobj":
                                    if doc[pos+3].text not in locations: locations.append(doc[pos+3].text)      
            
                ###############################################################################################################
                ##################### Ver o visualizer  do SpaCy para entender melhor esta parte ##############################


                # Depois do "compound" 
                # um "dobj" é sempre algo relevante ou local
                if token.dep_ == "dobj" and token.pos_ != "NUM" and token.text != "something" and not token.text.endswith("room") :
                    if token.text not in relevant_things and token.text not in locations:
                        relevant_things.append(token.text)
                if token.dep_ == "dobj" and token.pos_ != "NUM" and token.text != "something" and  token.text.endswith("room") :
                    if token.text not in relevant_things and token.text not in locations:
                        locations.append(token.text)
                # um "pobj" é sempre algo relevante ou local
                # in a toy shop
                    # in - ADP 
                    # a - det
                    # toy - noun
                    # shop - noun - pobj
                    # se shop for pobj deve ser local

                ################################## POBJ ##########################################
                if token.dep_ == "pobj":
                    if pos - 1 > 0 and pos - 1 < len(doc) and doc[pos - 1].dep_ == "amod" and doc[pos - 1].pos_ == "ADJ":
                        double_name_relevant_thing = doc[pos - 1].text + " " + token.text
                        if double_name_relevant_thing not in relevant_things:
                            relevant_things.append(double_name_relevant_thing)

                ################################## ADJ ##########################################
                if token.pos_ == "ADJ" and token.text != "few"  and  pos - 1 > 0 and doc[pos - 1].dep_!= "quantmod":
                    if pos + 1 < len(doc) and doc[pos + 1].pos_ == "NOUN":
                        double_name_relevant_thing = token.text + " " + doc[pos + 1].text 
                        if double_name_relevant_thing not in relevant_things:
                            relevant_things.append(double_name_relevant_thing)

                        if doc[pos + 1].text not in relevant_things:
                            relevant_things.append(doc[pos + 1].text)

                        ## no pc parts/uncompleted pcs
                        if pos - 5 > 0 and doc[pos - 5].text == "no" and doc[pos-5].pos_ == "DET":
                            positive_relevant_things.append(double_name_relevant_thing)
                            positive_relevant_things.append(doc[pos+1].text)

                ################################## Compound ##########################################
                if token.dep_ == "compound" or token.dep_ == "amod":
                    if pos + 1 < len(doc) and doc[pos+1].pos_ == "NOUN" and doc[pos+1].dep_ != "pobj" and not doc[pos+1].text.endswith("ing") and not doc[pos +1].text.endswith("room"):
                        if pos -1 > 0 and doc[pos - 1].dep_ != "quantmod":
                            double_name_relevant_thing = token.text + " " + doc[pos + 1].text
                            if double_name_relevant_thing not in locations  and double_name_relevant_thing not in relevant_things:
                                relevant_things.append(double_name_relevant_thing)
                        
                    if pos + 1 < len(doc) and doc[pos+1].pos_ == "NOUN" and doc[pos+1].dep_ != "pobj" and doc[pos+1].text.endswith("ing"):
                        double_name_activity = token.text + " " + doc[pos + 1].text
                        if double_name_activity not in activities:
                            activities.append(double_name_activity)
                    if pos + 1 < len(doc) and doc[pos+1].pos_ == "NOUN" and doc[pos+1].dep_ != "pobj" and doc[pos+1].text.endswith("room"):
                        if token.text + " " + doc[pos + 1].text not in locations:
                            locations.append(token.text + " " + doc[pos + 1].text)
                ################################## ADP ##########################################

                # >>>>>>>> in a toy shop
                if token.pos_ == "ADP":
                    
                    if token.text != "on" and token.text != "with" and token.text != "for" and token.text != "of" and token.text != "from":
                        if pos + 1  < len(doc) and doc[pos + 1].pos_ == "NOUN" and doc[pos + 1].dep_ == "pobj":
                            if pos + 2 < len(doc) and doc[pos + 2].pos_ != "ADP":  ### in front of (front nao é localidade)
                                if doc[pos+ 1].text not in locations:
                                    if pos - 1 > 0 and doc[pos -1].text == "looking":
                                        if token.text not in relevant_things : relevant_things.append(doc[pos +1].text)
                                    else:
                                    
                                        # the office
                                        locations.append(doc[pos + 1].text)
                                        inside_flag = True
                                        outside_flag = False
                                        
                                        ### > at home or outside
                                        if doc[pos+2].pos_ ==  "CCONJ" :
                                            if pos + 3 < len(doc) and doc[pos+3].dep_ == "conj" and doc[pos+3].pos_ != "VERB" and doc[pos + 3].pos_ != "ADP": #Added this (25):
                                                locations.append(doc[pos+3].text)
                            
                        if pos + 1  < len(doc) and doc[pos + 1].pos_ == "NOUN" and doc[pos + 1].dep_ != "pobj":
                            if pos + 2 < len(doc) and doc[pos + 2].pos_ == "NOUN" and doc[pos + 2].dep_ == "pobj":
                                double_name_location = doc[pos + 1].text + " " + doc[pos + 2].text
                                locations.append(double_name_location)
                        # >>>> in Ireland        
                        if pos + 1  < len(doc) and doc[pos + 1].pos_ == "PROPN" and doc[pos + 1].dep_ == "pobj":
                            if doc[pos + 1].text not in locations:
                                locations.append(doc[pos + 1].text)
                        if pos + 1 < len(doc) and doc[pos+1].pos_ =="DET":
                            # >> at the office
                            if pos + 2 < len(doc) and doc[pos+2].pos_ == "NOUN":
                                if doc[pos + 2].dep_ == "pobj":
                                    if doc[pos +2 ].text not in locations and doc[pos +2 ].text not in relevant_things and doc[pos + 2].text != "time": # filtrar time (at this time)
                                        if pos + 3 < len(doc) and doc[pos+3].pos_ != "AUX":
                                            inside_flag = True
                                            outside_flag = False
                                            locations.append(doc[pos + 2].text)
                                        if pos + 3 == len(doc):
                                            inside_flag = True
                                            outside_flag = False
                                            locations.append(doc[pos + 2].text)
                                # car sales showroom
                                if doc[pos + 2].pos_ == "NOUN" and doc[pos + 2].dep_ == "compound":
                                    if pos + 3 < len(doc) and doc[pos + 3].pos_ == "NOUN" and doc[pos + 3].dep_ == "compound":
                                        if pos + 5 < len(doc) and doc[pos + 5].pos_ == "NOUN" and doc[pos + 5].dep_ == "pobj":
                                            if doc[pos + 2].text + " " + doc[pos + 3].text + " " + doc[pos + 5].text not in locations:
                                                inside_flag = True
                                                outside_flag = False
                                                locations.append(doc[pos + 2].text + " " + doc[pos + 3].text + " " + doc[pos + 5].text)

                                if pos +3 < len(doc) and doc[pos + 3].dep_ == "pobj":
                                    double_name_location = doc[pos + 2].text + " " + doc[pos + 3].text
                                    if double_name_location not in locations:
                                        locations.append(double_name_location)
                                        inside_flag = True
                                        outside_flag = False
                                        # > eletronics store, or a supermarket
                                        if pos + 5 < len(doc) and doc[pos + 5].pos_ == "PUNCT":
                                            if pos + 5 < len(doc) and doc[pos + 5].pos_ == "CCONJ":
                                                if pos + 6 < len(doc) and doc[pos + 6].pos_ == "DET":
                                                    if pos + 7 < len(doc) and doc[pos + 7].pos_ == "NOUN":
                                                        locations.append(doc[pos+7].text)

                                if pos + 3 < len(doc) and doc[pos + 3].dep_ != "pobj" and doc[pos+3].pos_ == "NOUN":
                                    double_name_relevant_thing = doc[pos + 2].text + " " + doc[pos + 3].text
                                    if double_name_relevant_thing not in relevant_things:
                                        relevant_things.append(double_name_relevant_thing)
                                else :
                                    if doc[pos + 2].dep_ == "pobj"  and token.text != "at": #(filtrar at this time)
                                        if doc[pos + 2]. text not in locations:
                                            if pos + 3 < len(doc) and doc[pos  + 3].pos_!= "AUX" and doc[pos+2].text not in relevant_things:
                                                locations.append(doc[pos + 2].text)
                                                inside_flag = True
                                                outside_flag = False
                                            if doc[pos + 1].text == "another":
                                                double_name_location = doc[pos + 1].text + " " + doc[pos + 2].text
                                                locations.append(double_name_location)
                                        
                    if token.text == "with" or token.text == "for" or token.text == "of":
                        if pos + 1 < len(doc) and doc[pos+1].pos_ =="DET":
                            if pos + 2 < len(doc) and doc[pos+2].pos_ == "NOUN":    ## filtrar on the beach :
                                if pos + 3 < len (doc) and doc[pos +3].pos_ == "NOUN" and doc[pos + 3].dep_ == "pobj":
                                    double_name_relevant_thing = doc[pos + 2].text + " " + doc[pos + 3].text
                                    if double_name_relevant_thing not in relevant_things:
                                        relevant_things.append(double_name_relevant_thing)
                                if doc[pos + 2].text not in location_or_thing and doc[pos + 2].text not in dates and doc[pos + 2].dep_ == "pobj":
                                    #location_or_thing.append(doc[pos + 2].text)
                                    if pos - 1 > 0 and doc[pos -1].text != "inside" and doc[pos -1].text != "outside":
                                        relevant_things.append(doc[pos + 2].text)
                        # on his hand
                        if pos + 1 < len(doc) and doc[pos +1].pos_ == "PRON" and doc[pos + 1].dep_ == "poss":
                            if pos + 2 < len(doc) and doc[pos +2].pos_ == "NOUN" and doc[pos +2 ].dep_ == "pobj":
                                if doc[pos +2].text not in relevant_things:
                                    relevant_things.append(doc[pos +2].text)



                    ## >> on the table, on the beach, on the pier
                    if token.text == "on":
                        if pos + 1 < len(doc) and doc[pos+1].pos_ =="DET":
                            if pos + 2 < len(doc):  
                                if doc[pos+2].pos_ == "NOUN" or doc[pos + 2].pos_ == "ADJ":  ## filtrar on the beach :
                                    if pos + 3 < len (doc) and doc[pos +3].pos_ == "NOUN" and doc[pos + 3].dep_ == "pobj":
                                        double_name_relevant_thing = doc[pos + 2].text + " " + doc[pos + 3].text
                                        if double_name_relevant_thing not in relevant_things:
                                            location_or_thing.append(double_name_relevant_thing)
                                    if doc[pos + 2].text not in location_or_thing and doc[pos + 2].text not in dates and doc[pos + 2].dep_ == "pobj":
                                        #location_or_thing.append(doc[pos + 2].text)
                                        location_or_thing.append(doc[pos + 2].text)
                
                        # on his hand
                        if pos + 1 < len(doc) and doc[pos +1].pos_ == "PRON" and doc[pos + 1].dep_ == "poss":
                            if pos + 2 < len(doc) and doc[pos +2].pos_ == "NOUN" and doc[pos +2 ].dep_ == "pobj":
                                if doc[pos +2].text not in relevant_things:
                                    location_or_thing.append(doc[pos +2].text)  

            ################################## VERB ##########################################
                # >>> being recorded for a television show
                if token.pos_== "VERB":
                    
                    if token.text.endswith("ing") or token.text.endswith("ed"):
                        # grocery shopping
                    
                        if pos - 1 < len(doc) and pos - 1 > 0 and token.dep_ == "attr":
                            if doc[pos - 1].pos_ == "NOUN" and doc[pos - 1].dep_ == "compound":
                                activities.append(doc[pos - 1].text + " " + token.text)



                        if pos +1 < len(doc) and doc[pos + 1].pos_ == "NOUN" and doc[pos + 1].dep_ == "dobj":
                            double_name_activity = token.text + " " + doc[pos + 1].text
                            if double_name_activity not in activities:
                                activities.append(double_name_activity)

                        if pos + 1 < len(doc) and doc[pos + 1].pos_ == "ADJ":
                            if pos + 2 < len(doc) and doc[pos + 2].pos_ == "NOUN":
                                multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text
                                activities.append(multiple_name_activity)
                        # >>> eating ice cream
                        if  pos + 1 < len(doc) and doc[pos + 1].dep_ == "compound":
                            if pos + 2 < len(doc) and doc[pos + 2].pos_== "NOUN" and doc[pos + 2].dep_ == "dobj":
                                multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text
                                if multiple_name_activity not in activities:
                                    activities.append(multiple_name_activity)

                        if pos + 1 < len(doc) and doc[pos + 1].pos_ == "DET" and doc[pos + 1].text != "any":
                            if pos + 2 < len(doc) and doc[pos + 2].pos_ == "NOUN" and doc[pos + 2].dep_ == "dobj":
                                multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text
                                if multiple_name_activity not in activities:
                                    activities.append(multiple_name_activity)

                            # >>> holding the ice cream cone
                            if pos + 2  < len(doc) and doc[pos + 2].pos_ == "NOUN" and doc[pos + 2].dep_ == "compound":
                                if pos + 3 < len(doc) and doc[pos + 3 ].pos_ == "NOUN" and doc[pos + 3].dep_ == "compound":
                                    if pos + 5 < len(doc) and doc[pos + 5 ].pos_ == "NOUN" and doc[pos + 5 ].dep_ == "dobj":
                                        multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos + 3].text + " " + doc[pos + 5].text
                                        if multiple_name_activity not in activities:
                                            activities.append(multiple_name_activity)
                        
                        # >>>> repairing his car
                        if pos + 1 < len(doc) and doc[pos + 1].dep_ == "poss":
                            if pos + 2 < len(doc) and doc[pos + 2].dep_ == "dobj" and doc[pos + 2].pos_ == "NOUN":
                                multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text
                                if multiple_name_activity not in activities:
                                    activities.append(multiple_name_activity)

                    if pos + 1 < len(doc) and doc[pos + 1].pos_ == "ADP":
                        if pos + 2 < len(doc) and doc[pos +2].pos_ == "NOUN":   
                            multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text
                            activities.append(multiple_name_activity)
                        if pos + 2 < len(doc) and doc[pos + 2].pos_ == "DET":
                            if pos + 3 < len(doc) and doc[pos + 3].pos_ == "NOUN":
                                # >>>> Walking by the sea
                                ##>>>> walking on a pier
                                if pos + 5 < len(doc) and doc[pos + 5].pos != "NOUN":
                                    multiple_name_activity = doc[pos].text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos +3].text 
                                    activities.append(multiple_name_activity)
                                if pos + 5 < len(doc) and doc[pos + 5].pos_ == "NOUN":
                                    if pos - 1 > 0 and pos - 1 < len(doc) and doc[pos - 1].pos_ == "AUX" and doc[pos - 1].dep_ == "auxpass":
                                        multiple_name_activity = doc[pos - 1].text + " " + doc[pos].text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos +3].text + " " + doc[pos +5].text 
                                        activities.append(multiple_name_activity)
                            ## >>> looking at an old clock
                            if pos + 3 < len(doc) and doc[pos + 3].pos_ == "ADJ" and doc[pos + 3].dep_ == "amod":
                                if pos + 5 < len(doc) and doc[pos + 5].pos_ == "NOUN" and doc[pos + 5].dep_ == "pobj":

                                    multiple_name_activity = doc[pos].text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos +3].text + " " + doc[pos +5].text
                                    if multiple_name_activity not in activities:
                                        activities.append(multiple_name_activity)


                    if pos + 1 < len(doc) and doc[pos + 1].text == "/":
                        if pos + 2 < len(doc):
                            if doc[pos + 2].pos_ == "VERB" or doc[pos + 2].pos_ == "NOUN":
                                if token.text not in activities : activities.append(token.text)
                                if doc[pos + 2].text not in activities: activities.append(doc[pos + 2].text)

                ################################################## NOUN ##########################################

                if token.pos_ == "NOUN":
                    
                    ## >>> flowers visible
                    if pos + 1 < len(doc) and doc[pos + 1].pos_ == "ADJ" and token.dep_ =="nsubj":
                        if token.text not in relevant_things: 
                            relevant_things.append(token.text)
                        double_name_relevant_thing = token.text + " " + doc[pos + 1].text
                        if double_name_relevant_thing not in relevant_things: 
                            relevant_things.append(double_name_relevant_thing)

                    if pos + 1 < len(doc) and doc[pos + 1].text == "/":
                        if pos + 2 < len(doc):
                            if doc[pos + 2].pos_ == "NOUN" or doc[pos + 2].pos_ == "PROPN":
                                if token.text not in relevant_things : relevant_things.append(token.text)
                                if doc[pos + 2].text not in relevant_things: relevant_things.append(doc[pos + 2].text)

                    # >>>>>> toys are being examined
                    if pos + 1 < len(doc) and doc[pos + 1].pos_ == "AUX":
                        if pos + 2 < len(doc) and doc[pos +2].pos_ == "AUX":
                            if pos + 3 < len(doc) and doc[pos + 3].pos_ == "VERB" and doc[pos + 3].text.endswith("ed"):
                                multiple_name_activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos + 3].text
                                activities.append(multiple_name_activity)
                    
                    if token.dep_ == "compound":
                        ## >>>> camera phone
                        if pos + 1 < len(doc) and doc[pos + 1].pos_ == "NOUN" and doc[pos + 1].dep_ != "compound" and not doc[pos + 1].text.endswith("ing"):
                            double_name_relevant_thing = token.text + " " + doc[pos + 1].text 
                            if double_name_relevant_thing not in relevant_things and double_name_relevant_thing not in locations:
                                relevant_things.append(double_name_relevant_thing)
                        ## >> ice cream cone
                        if pos + 1 < len(doc) and doc[pos + 1].pos_ == "NOUN" and doc[pos+1].dep_ == "compound":
                            if pos + 2 < len(doc) and doc[pos + 2].pos_ == "NOUN":
                                if pos + 3 < len(doc) and doc[pos + 3].pos_ != "NOUN":
                                    multiple_name_relevant_thing = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text 
                                    if multiple_name_relevant_thing not in relevant_things and multiple_name_relevant_thing not in locations:
                                        relevant_things.append(multiple_name_relevant_thing)
                
                ######################################### PRON ##############################################

                if token.pos_ == "DET" and token.dep_ == "poss":
                    if pos + 1 < len(doc) and doc[pos + 1].pos_ == "NOUN":
                        if doc[pos + 1].text not in relevant_things:
                            relevant_things.append(doc[pos + 1].text)              
                
            



                pos = pos + 1

            
            if text not in negative_text:
                positive_relevant_things = relevant_things.copy()
                positive_locations = locations.copy()
                positive_dates = dates.copy()
                positive_activities = activities.copy()

            if text in negative_text:
                negative_relevant_things = relevant_things.copy()
                negative_locations = locations.copy()
                negative_dates = dates.copy()
                negative_activities = activities.copy() 

        ######################################################################### Chunks ##################################################################### 

        for text in texts:

            if text in negative_text: break

            doc = nlp(text)


            for chunk in doc.noun_chunks:
                
                i = 0
                # >>>>>>> chunks de apenas uma palvra
                if len(chunk) == 1 and chunk[i].is_stop == False:
                    if chunk[i].pos_ == "NOUN" and chunk[i].text not in chunk_relevant_things:
                        chunk_relevant_things.append(chunk.text)

                        ############################### atençao a isto #####################################
                        if chunk[i].dep_ == "pobj" or chunk[i].dep_ == "conj":
                            if chunk[i].text not in positive_relevant_things and chunk[i].text not in positive_relevant_things and  chunk[i].text not in positive_locations and chunk[i].text not in positive_dates:
                                if not chunk[i].text.endswith("ing"): #filtrar alguns verbos que possam vir para aqui
                                    positive_relevant_things.append(chunk[i].text)
                        ###################################################################################
                
                # >>>>>>>>>>> Impede chunks de apenas uma palvra
                if len(chunk) > 1: 
                    while i < len(chunk):
                        if chunk[i].pos_ == "VERB" or chunk[i].text.endswith("ing"):
                            if chunk.text not in chunk_activites:
                                chunk_activites.append(chunk.text)
                            
                        if chunk[i].pos_ == "DET":
                            if i + 1 < len(chunk) and chunk[i + 1].pos_ == "NOUN" and chunk[i + 1].text not in chunk_locations:
                                chunk_locations.append(chunk[i + 1].text)
                        
                        if chunk[i].pos_ == "ADJ":
                            if i + 1 < len(chunk) and chunk[i + 1].pos_ == "NOUN" and chunk.text not in chunk_relevant_things:
                                chunk_relevant_things.append(chunk.text)
                        i = i +1

        ################################################### Esta parte "Tenta" limpar alguns erros ################################################
        for text in texts:
            doc = nlp(text)
            for token in doc:
                
                    if token.text in positive_dates:
                        if token.text in positive_relevant_things:
                            del positive_relevant_things[relevant_things.index(token.text)]
                        if token.text in location_or_thing:
                            del location_or_thing[location_or_thing.index(token.text)]
                    if token.pos_ != "PUNCT" and token.text != " " and token.text != "  ":
                        if token.text not in positive_relevant_things:
                            if token.text not in positive_locations:
                                if token.text not in positive_activities:
                                    if token.text not in  other_things:
                                        if token.text not in positive_dates:
                                            if token.text not in location_or_thing:
                                            # Para remover palavras comuns como : in, at, is
                                                if token.is_stop == False:  
                                                    if token.pos_ == "NOUN" and token.text not in other_things and token.text not in other_words:
                                                        other_things.append(token.text)   
                                                    if token.text not in other_words and token.text not in other_words and token.text not in other_things: 
                                                        other_words.append(token.text)

        for stuff in location_or_thing:
            if stuff in days_week or stuff in days_week_plural:
                del location_or_thing[location_or_thing.index(stuff)]

        ###################################################### USO DAS PALAVRAS NEGATIVAS ###############################################################
                    
        if "u1" in positive_relevant_things:
            del positive_relevant_things[positive_relevant_things.index("u1")]
        if "u1" in positive_locations:
            del positive_locations[positive_locations.index("u1")]
        if not positive_locations:
            inside_flag = "NULL"
            outside_flag = "NULL"
        if ("sea" or "garden") in locations :
            inside_flag = False
            outside_flag = True


        ###################################################### USO DAS PALAVRAS NEGATIVAS ###############################################################


        for thing in positive_relevant_things:
            for negative_thing in negative_relevant_things:
                if nlp(thing).similarity(nlp(negative_thing)) > 0.8:
                    del negative_relevant_things[negative_relevant_things.index(negative_thing)]

        for activity in positive_activities:
            for negative_activity in negative_activities:
                if nlp(activity).similarity(nlp(negative_activity)) > 0.8:
                    del negative_activities[negative_activities.index(negative_activity)]          

        for loc in positive_locations:
            for negative_location in negative_locations:
                if nlp(loc).similarity(nlp(negative_location)) > 0.8:
                    del negative_locations[negative_locations.index(negative_location)]

        for date in positive_dates:
            for negative_date in negative_dates:
                if nlp(date).similarity(nlp(negative_date)) > 0.8:
                    del negative_dates[negative_dates.index(negative_date)]

        ###################################################### remover relevant things muito parecidas ###############################################################
        temp_array = positive_relevant_things.copy()
        deleted_word = []
        for thing in positive_relevant_things:
            for temp_thing in temp_array:
                if nlp(thing).similarity(nlp(temp_thing)) == 1 : break
                if nlp(thing).similarity(nlp(temp_thing)) > 0.85: 
                    deleted_word.append(temp_thing)
                    del positive_relevant_things[positive_relevant_things.index(temp_thing)]

        ############################################################## PRINTS ##################################################################

        '''
        print("")    
        print("Chunk relevant things: ", chunk_relevant_things)
        print("Chunk Locations: ", chunk_locations)
        print("Chunk activities: ", chunk_activites)
        
        print("")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: POSITIVE ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        print("Relevant things", positive_relevant_things)
        print("Activities", positive_activities)
        print("Dates", positive_dates)
        print("Locations: ", positive_locations)
        print("Location or Thing", location_or_thing)
        print("User inside: ", inside_flag)
        print("User outside: ", outside_flag)



        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: NEGATIVE ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("Negative Relevant thing", negative_relevant_things)
        print("Activities", negative_activities)
        print("Dates", negative_dates)
        print("Locations: ", negative_locations)



        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: RANDOM ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("Other words: ", other_words)
        print("other things" , other_things)
        print("deleted" , deleted_word)
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("")
        '''
        ######################################################################################################################################



        text_info = {
            'topic' : topic,
            'relevant things' : positive_relevant_things,
            'activities' : positive_activities,
            'dates' : positive_dates,
            'locations' : positive_locations,
            'other words' : other_words,
            'other things' : other_things,
            'inside' : inside_flag,
            'outside' : outside_flag,
            'location or thing': location_or_thing,
            'negative relevant thing' : negative_relevant_things,
            'negative activities' : negative_activities,
            'negative locations' : negative_locations,
            'negative dates' : negative_dates,
            'deleted word' : deleted_word
        }

        dir_path = os.path.dirname(os.path.realpath(__file__))

        json_path = open(dir_path + "/result_json_nlp/NLP_data_topic_" + str(topic) + ".json" , 'w+') # ficheiro json

        json.dump(text_info,json_path, indent= 3)

    


