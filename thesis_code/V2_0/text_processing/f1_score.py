###################################################### IMPORT ######################################################

import os
from collections import Counter
from tqdm import tqdm


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

def cluster_recall(numb, topic_count):
     
    ground_images = []
    file_ground = open(groundtruth_path, "r")


    ###  Vai buscar o nome de todas as imagens no groundtruth
    for line_ground in file_ground:
        if str(line_ground[0]) == str(topic_count) and str(line_ground[0:2]) != "10":
            index_punct = getIndexPositions(line_ground, ',')
            image_name = line_ground[ index_punct[0] + 2 : index_punct[1]]
            ground_images.append(image_name)

        if str(line_ground[0:2]) == str(topic_count):
            index_punct = getIndexPositions(line_ground, ',')
            image_name = line_ground[ index_punct[0] + 2 : index_punct[1]]
            ground_images.append(image_name)

    top = []
    temp_score = 0
    i = 0
    file = open(results_path, "r")
  
    top_images = []
    inc = 0
    for line in file:
        index_punct = getIndexPositions(line, ',')
        image_name = line[index_punct[0] + 2 : index_punct[1]-1]
        image_score = float(line[index_punct[1] + 1 : len(line) - 1])
     
        if len(top) < numb:
                top.append(image_score)

        else:
            if image_score > min(top):
                top[top.index(min(top))] = image_score

       
        
        
    top.sort()  
    file.close()  
    # vai buscar o nome das imagens do top50
    
    for score in top:
        
        file = open(results_path, "r")
        for new_line in file:
            score_punct =  getIndexPositions(new_line, ',')
            new_line_score = new_line[score_punct[1] + 2 : len(new_line)-1]
            if score == float(new_line_score):
                index_punct = getIndexPositions(new_line, ',')
                image_name = new_line[ index_punct[0] + 2 : index_punct[1]-1]
                top_images.append(image_name)
                break
    
    clusters = []

    ## vai buscar os clusters dos top imagens no ficheiro clusters
    for image_name in top_images:
        file.close()
        file = open(groundtruth_path, "r")

        for line in file:
            if image_name in line :
                if ".jpg" in line : index_1 = line.index(".jpg")
                if ".JPG" in line : index_1 = line.index(".JPG")
                
                clusters.append(line[index_1 + 6])

   # print(clusters)
    
    #print(len(Counter(clusters).keys()))

    file = open(cluster_path, "r")
    max_clust = 0
    for line in file:
        if int(line[0]) == 1:
            index_1 = line.index(",")
            temp_clust = int(line[index_1 + 2])

            if temp_clust > max_clust :
                max_clust = temp_clust

    
    clust_recall = len(Counter(clusters).keys()) / max_clust
    
    return top_images, ground_images, clust_recall

def precision(top_images, ground_images):
    tp = 0
    fp = 0
    precision_n = 0

    for image in top_images: 
        if image in ground_images:
            tp = tp + 1
        if image not in ground_images:
            fp = fp + 1

    if tp + fp != 0 : precision_n = tp / (tp + fp)
    
    return precision_n

def f1_score(clust_recall, precision_n, numb):  

    dev = precision_n + clust_recall 

    if dev != 0 : 
        f1 = 2 * (precision_n * clust_recall) / dev
    else : f1 = 0
    
    return f1
#################################################################################### MAIN  #################################################################################

if __name__ == '__main__' :
    print("")
    print("-----------------------------------------------F1 CALCULATION SCRIPT----------------------------------------- \n")

    

    dir_path = os.path.dirname(os.path.realpath(__file__))
    groundtruth_path = dir_path + "/files/ImageCLEF2020_dev_gt.txt"
    cluster_path = dir_path + "/files/ImageCLEF2020_dev_clusters.txt"
    
    previous_file =os.listdir( dir_path + "/results_f1_score")
    previous_file_path = dir_path + "/results_f1_score"

    for each_file in previous_file:
        if each_file.endswith(".txt"):
            os.remove(previous_file_path + "/" + each_file)
    
    


    topic_count = 1
    
    top = [5 , 10 , 20 , 30 , 40 , 50]
    topic = [1,2,3,4,5,6,7,8,9,10]

    print("PROCESSING F1 CALCULATIONS:")

    for topic_count in tqdm(topic):

        for numb in top:

            results_path = dir_path + "/results_confidence/results_topic_" + str(topic_count) + ".txt"

            top_images, ground_images, clust_recall= cluster_recall(numb, topic_count)
            precision_n = precision(top_images, ground_images)

            f1 = f1_score(clust_recall, precision_n, numb)

            txt_path = dir_path + "/results_f1_score/results_f1_score.txt"
            f = open(txt_path,"a+")

            if numb == 5 : line = str(topic_count) + " , f1@0" + str(numb) + " : " + str(f1) + "\n"
            if numb != 5 : line = str(topic_count) + " , f1@" + str(numb) + " : " + str(f1) + "\n"

            
            f.write(line)
            f.close()      


        topic_count = topic_count + 1