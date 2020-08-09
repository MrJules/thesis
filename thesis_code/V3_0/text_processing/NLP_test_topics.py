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
    #topic_array = [10]
    
    print("PROCESSING TEXT")

    for topic_count in tqdm(topic_array):
        #######################################################################################################################################################
        ### test topics
        
        if topic_count == 1:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Praying Rite"
            text_description  = "Find the moment when u1 was attending a praying rite with other people in the church."
            text_narrative= "To be relevant, the moment must show u1 is currently inside the church, attending a praying rite with other people. The moments that u1 is outside with the church visible or inside the church but is not attending the praying rite are not considered relevant."

        if topic_count == 2:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Lifelog data on touchscreen on the wall"
            text_description  = "Find the moment when u1 was looking at lifelog data on a large touchscreen on the wall."
            text_narrative= "To be relevant, the moment must show u1 is looking at his lifelog data on the touchscreen wall. The touchscreen wall showed a range of colorful images at that time. At some moments, u1 was talking to other people while looking at the lifelog data on the touchscreen wall. The moments that u1 is looking at the touchscreen on the wall but it did not show colorful lifelog images are not considered relevant. The moments that u1 is looking at his colorful lifelog data on a desktop monitor are also not considered relevant."
        
        if topic_count == 3:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Bus to work - Bus to home"
            text_description  = "Find the moment when u1 was getting a bus to his office at Dublin City University or was going home by bus."
            text_narrative= "To be relevant, u1 was on the bus and the destination is his home or his workplace. The moments that u1 was waiting at the bus stop or u1 was travelling on any other public transportations or the destination is not his home/workplace are not considered relevant."
        
        if topic_count == 4:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Bus at the airport"
            text_description  = "Find the moment when u1 was getting on a bus in the aircraft landing deck in the airport."
            text_narrative= "To be relevant, u1 was walking to the bus in the aircraft landing deck in the airport after. Some possible moments include u1 walking out from the airplane and u1 walking to the bus parking in the aircraft landing deck. There would be many airplanes visible. Other moments that u1 was on the bus without airplanes visible outside/u1 was at the airport but the bus is not visible/the bus is not in the aircraft landing deck are not considered relevant."
        
        if topic_count == 5:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Medicine cabinet"
            text_description  = "Find the moment when u1 was looking inside the medicine cabinet in the bathroom at home."
            text_narrative= "To be considered relevant, u1 must be at home, looking inside the opening medicine cabinet beside a mirror in the bathroom. The moments that u1 was looking inside the medicine cabinet in other places (not at home and not in the bathroom) or u1 was looking at the closed medicine cabinet are not considered to be relevant."
        
        if topic_count == 6:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Order Food in the Airport"
            text_description  = "Find the moment when u1 was ordering fast food in the airport"
            text_narrative = "To be relevant, u1 must be at the airport and ordering food. The moments that u1 was queuing to order food are also considered relevant. The moments that u1 was eating fast food or waiting for collection of food at the airport are not considered to be relevant"
        
        if topic_count == 7:
            #[TOPIC 1]
            topic = str(topic_count)
            text_title = "Seafood at Restaurant"
            text_description  = "Find moments when u1 was eating seafood in a restaurant in the evening time"
            text_narrative = "The moments show u1 was eating seafood in any restaurant in the evening time are considered relevant. Any dish has seafood as one of its parts is also considered relevant. Some examples of the seafood can be shrimp, lobster, salmon."
        

        if topic_count == 8:
            topic = str(topic_count)
            text_title = "Meeting with people"
            text_description = "Find the moments when u1 was a roundtable meeting with many people and there was pink (not red) name-cards for each person"
            text_narrative = "The moments show u1 was at a roundtable and having a meeting with many people, and with pink name-cards visible are considered relevant. The moments that people are not having a meeting are not relevant"
       
        if topic_count == 9:
            topic = str(topic_count)
            text_title = "Eating Pizza"
            text_description = "Find the moments when u1 was eating a pizza while talking to one man"
            text_narrative = "To be considered relevant, the u1 must eat or hold a pizza with a man visible in the background. The moments that u1 was talking to more than one person are not relevant"

        if topic_count == 10:
            topic = str(topic_count)
            text_title = "Socializing"
            text_description = "Find the moments when u1 was talking to a lady in a red top, standing directly in front of a poster hanging on a wall"
            text_narrative = "To be relevant, the u1 must be talking with a woman in red, who was standing right in front of a scientific research poster"
        
        ############################################################### Pre-processamento do texto ########################################################
        
        
        text_narrative = text_narrative.split(".")
        if "" in text_narrative:
            del text_narrative[text_narrative.index("")]
        

        text_narrative_final =[]
        negative_sentences = []
        for narrative in text_narrative:
            if  narrative.endswith("not considered to be relevant") or narrative.endswith("not considered relevant") or narrative.endswith("is not relevant") or narrative.endswith("are not relevant"):
                negative_sentences.append(narrative)
                
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

                if token.pos_ == "NUM" and token.text.isdigit() and len(token.text) == 4 :
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
                        if token.text != "bus" : locations.append(token.text)
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

                ################################## PROPN #######################################
                if token.pos_ == "PROPN" and token.text != "city" and token.text != "show": 
                    if pos + 1 < len(doc) and doc[pos + 1].pos_ == "PROPN" and doc[pos+1].text != "city":
                        multiple_name_relevant_thing = token.text + " " + doc[pos + 1].text
                        if multiple_name_relevant_thing not in relevant_things :
                            relevant_things.append(multiple_name_relevant_thing)
                            


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
                        if pos -1 > 0 and doc[pos - 1].dep_ != "quantmod" and not token.text.endswith("ing"):
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
                                    elif doc[pos+1].text not in relevant_things and doc[pos+1].text != "red":
                                        
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
                        if pos + 1  < len(doc) and doc[pos + 1].pos_ == "PROPN" and doc[pos + 1].dep_ == "compound":
                            if pos + 2  < len(doc) and doc[pos + 2].pos_ == "PROPN" and doc[pos + 2].dep_ == "compound":
                                if pos + 3  < len(doc) and doc[pos + 3].pos_ == "PROPN":
                                    location = doc[pos + 1 ].text + " " + doc[pos + 2 ].text + " " + doc[pos+3].text
                                    if location not in locations : locations.append(location)
                        
                        if pos + 1 < len(doc) and doc[pos+1].pos_ =="DET" and doc[pos+1].dep_ != "poss":
                            # >> at the office
                            if pos + 2 < len(doc) and doc[pos+2].pos_ == "NOUN":
                                if doc[pos + 2].dep_ == "pobj":
                                    if doc[pos +2 ].text not in locations and doc[pos +2 ].text not in relevant_things and doc[pos + 2].text != "time": # filtrar time (at this time)
                                        if pos + 3 < len(doc) and doc[pos+3].pos_ != "AUX" and doc[pos+2].text != "moments" and doc[pos+2].text != "touchscreen" and doc[pos+2].text != "mirror":
                                            if doc[pos+2].text != "bus" and doc[pos+2].text != "roundtable" and doc[pos+2].text != "lady":
                                                inside_flag = True
                                                outside_flag = False
                                                locations.append(doc[pos + 2].text)
                                            if doc[pos+2].text == "bus" : relevant_things.append(doc[pos+2].text)
                                        if pos + 3 == len(doc) and doc[pos+2].text != "moments" and doc[pos+2].text != "background" :
                                            inside_flag = True
                                            outside_flag = False
                                            locations.append(doc[pos + 2].text)
                                # car sales showroom
                                if doc[pos + 2].pos_ == "NOUN" and doc[pos + 2].dep_ == "compound":
                                    if pos + 3 < len(doc) and doc[pos + 3].pos_ == "NOUN" and doc[pos + 3].dep_ == "pobj":
                                        location = doc[pos +2 ].text + " " + doc[pos+3].text 
                                        if location not in locations  and location not in relevant_things: locations.append(location)
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
                                    
                                    if not doc[pos+2].text.endswith("ing") : double_name_relevant_thing = doc[pos + 2].text + " " + doc[pos + 3].text
                                    if double_name_relevant_thing not in relevant_things:
                                        relevant_things.append(double_name_relevant_thing)
                                else :
                                    if doc[pos + 2].dep_ == "pobj"  and token.text != "at": #(filtrar at this time)
                                        if doc[pos + 2]. text not in locations:
                                            if pos + 3 < len(doc) and doc[pos  + 3].pos_!= "AUX" and doc[pos+2].text not in relevant_things:
                                                if doc[pos+2].text == "mirror" or doc[pos+2].text == "lady"  : relevant_things.append(doc[pos+2].text)
                                                else:
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
                        if token.text not in activities: activities.append(token.text)
                        # grocery shopping
                        if token.dep_ == "relcl":
                            if pos + 1 < len(doc) and doc[pos + 1].pos_ == "PART" and doc[pos + 1].dep_ == "aux":
                                if pos + 2 < len(doc) and doc[pos + 2].pos_ == "VERB" and doc[pos + 2].dep_ == "xcomp":
                                    if pos + 3 < len(doc) and doc[pos + 3].pos_ == "NOUN" and doc[pos + 3].dep_ == "dobj":
                                        activity = token.text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos + 3].text
                                        if activity not in activities : activities.append(activity)
                                        if doc[pos+3].text not in relevant_things : relevant_things.append(doc[pos+3].text)


                        if pos - 1 < len(doc) and pos - 1 > 0 and token.dep_ == "attr":
                            if doc[pos - 1].pos_ == "NOUN" and doc[pos - 1].dep_ == "compound":
                                activities.append(doc[pos - 1].text + " " + token.text)


                        if pos + 1 < len(doc) and doc[pos +1].pos_ == "ADV" and doc[pos+1].dep_ == "advmod":
                            if doc[pos+1].text not in locations and doc[pos+1].text != "directly" and doc[pos+1].text != "right":
                                locations.append(doc[pos+1].text)
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
                        if pos + 2 < len(doc) and doc[pos +2].pos_ == "PROPN":  
                            if pos + 3 < len(doc) and doc[pos +3].pos_ == "PROPN": 
                                multiple_name_activity = doc[pos].text + " " + doc[pos + 1].text + " " + doc[pos + 2].text + " " + doc[pos +3].text 
                                activities.append(multiple_name_activity)
                                

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
                                    if doc[pos + 4].pos_ == "NOUN" and doc[pos+4].dep_ == "pobj":
                                        del activities[activities.index(multiple_name_activity)]
                                        activities.append(multiple_name_activity + " " + doc[pos+4].text)
                                    if doc[pos+4].dep_ != "pobj" and doc[pos+4].pos_ == "NOUN" and doc[pos+5].dep_ == "pobj":
                                        del activities[activities.index(multiple_name_activity)]
                                        activities.append(multiple_name_activity + " " + doc[pos+4].text + " " + doc[pos+5].text)


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

                    
                    if pos + 1 < len(doc) and doc[pos+1].pos_ == "PUNCT":
                        if pos + 2 < len(doc) and doc[pos+2].pos_ == "NOUN":
                            if pos + 3 < len(doc) and doc[pos+3].pos_ == "PUNCT":
                                if pos + 4 < len(doc) and doc[pos+4].pos_ == "NOUN":
                                    if token.text not in relevant_things : relevant_things.append(token.text)
                                    if doc[pos+2].text not in relevant_things : relevant_things.append(doc[pos+2].text)
                                    if doc[pos+4].text not in relevant_things : relevant_things.append(doc[pos+4].text)
                                    
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
                        if pos+1 < len(doc) and doc[pos+1].text == "-":
                            if pos +2 < len(doc) and doc[pos+2].pos_ == "NOUN" and doc[pos+2].dep_ == "attr":
                                multiple_name_relevant_thing = token.text + doc[pos+1].text + doc[pos+2].text
                                if multiple_name_relevant_thing not in relevant_things: relevant_things.append(multiple_name_relevant_thing)
                        
                        ## >>>> camera phone
                        if pos + 1 < len(doc) and doc[pos + 1].pos_ == "NOUN" and doc[pos + 1].dep_ != "compound" and not doc[pos + 1].text.endswith("ing"):
                            double_name_relevant_thing = token.text + " " + doc[pos + 1].text 
                            if double_name_relevant_thing not in relevant_things and double_name_relevant_thing not in locations:
                                relevant_things.append(double_name_relevant_thing)

                        if pos + 1 < len(doc) and doc[pos+1].pos_ == "PROPN" and not doc[pos + 1].text.endswith("ing"):
                            double_name_relevant_thing = token.text + " " + doc[pos + 1].text 
                            if double_name_relevant_thing not in relevant_things :
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
                        if doc[pos + 1].text not in relevant_things and doc[pos+1].text != "office":
                            if token.text != "office" : relevant_things.append(doc[pos + 1].text)        
                        if doc[pos+1].text == "office" and doc[pos+1].text not in locations: locations.append(doc[pos+1].text)      
                
            

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
                        if chunk[i].pos_ == "NOUN" and chunk[i].text not in positive_relevant_things :
                            if chunk[i].text not in locations:
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
        if "considered" in positive_activities :
            del positive_activities [positive_activities.index("considered")]
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





        text_info = {
            'topic' : topic,
            'relevant things' : positive_relevant_things,
            'activities' : positive_activities,
            'dates' : positive_dates,
            'locations' : positive_locations,
            #'other words' : other_words,
            #'other things' : other_things,
            'inside' : inside_flag,
            'outside' : outside_flag,
           # 'location or thing': location_or_thing,
            'negative relevant thing' : negative_relevant_things,
            'negative activities' : negative_activities,
            'negative locations' : negative_locations,
            'negative dates' : negative_dates,
            #'deleted word' : deleted_word
        }

        dir_path = os.path.dirname(os.path.realpath(__file__))

        json_path = open(dir_path + "/result_json_nlp/NLP_data_topic_" + str(topic) + ".json" , 'w+') # ficheiro json

        json.dump(text_info,json_path, indent= 3)

    


