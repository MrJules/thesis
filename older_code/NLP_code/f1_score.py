###################################################### IMPORT ######################################################

import os
from collections import Counter

def cluster_recall():
     
    ground_images = []
    file_ground = open(groundtruth_path, "r")


    ###  Vai buscar o nome de todas as imagens no groundtruth
    for line_ground in file_ground:
        index_1 = line_ground.index(",")

        if ".jpg" in line_ground : index_2 = line_ground.index(".jpg")
        if ".JPG" in line_ground : index_2 = line_ground.index(".JPG")

        image_name = line_ground[index_1 + 2 : index_2 + 4]
        ground_images.append(image_name)


    top = []
    temp_score = 0
    i = 0
    file = open(results_path, "r")
    top_images = []
    

    ## vai buscar o top 50 score de todas as imagens que estão presentes no groundtruth e results
 
    ## vai buscar o top 50
    for line in file:
        index_1 = line.index(",")
        index_2 = line.index(".jpg")
        image_name = line[index_1 + 2 : index_2 + 4]

        index_score = index_2 + 7
        image_score = float(line[index_score:len(line)-2]) # remove o  barra n
        if len(top) < 50:
                top.append(image_score)

        else:
            if image_score > min(top):
                top[top.index(min(top))] = image_score
    top.sort()    

    top_images = []

   # print(top)
    # vai buscar o nome das imagens do top50
    
    for score in top:
        file.close()
        file = open(results_path, "r")
        for new_line in file:
            if str(score) in new_line:
                
                index_1 = line.index(",")

                if ".jpg" in new_line : index_2 = new_line.index(".jpg")
                if ".JPG" in new_line : index_2 = new_line.index(".JPG")
                
                image_name = new_line[index_1 + 2 : index_2 + 4]
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

    print (" ------------------- CLUSTER RECALL --------------------------")
    print("Total clusters in topic: ", max_clust)
    print("Total of different clusters found: " ,len(Counter(clusters).keys()))
    print("Cluster recall : ", clust_recall)

    return top_images, ground_images, clust_recall

def precision(top_images, ground_images):
    tp = 0
    fp = 0

    for image in top_images: 
        if image in ground_images:
            tp = tp + 1
        if image not in ground_images:
            fp = fp + 1

    precision_n = tp / (tp + fp)

    print (" ------------------- PRECISION --------------------------")
    print("True positive: ", tp)
    print("False positve: " , fp)
    print("Precision: ", precision_n)

    return precision_n

def f1_score(clust_recall, precision_n):  

    f1 = 2 * (precision_n * clust_recall) / (precision_n + clust_recall)
    print (" ------------------- F1 SCORE TOP 50 -----------------------")
    print("f1 score (%) : ", f1*100)
#################################################################################### MAIN  #################################################################################

if __name__ == '__main__' :

    dir_path = os.path.dirname(os.path.realpath(__file__))
    groundtruth_path = dir_path + "/files/ImageCLEF2020_dev_gt.txt"
    cluster_path = dir_path + "/files/ImageCLEF2020_dev_clusters.txt"
    results_path = dir_path + "/results/results_topic_1.txt"

    top_images, ground_images, clust_recall= cluster_recall()
    precision_n = precision(top_images, ground_images)

    f1_score(clust_recall, precision_n)