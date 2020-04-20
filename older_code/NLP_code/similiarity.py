import spacy
import json
import os

'''
#print(__file__)
#print(os.getcwd())

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = dir_path + "/small_data.json"

#images_path = os.listdir(dir_path + "/data_images")
#images_path = dir_path + "/data_images"

data = json.loads(open(data_path).read())

data_images = data.keys()
image_names = []

for name_images in data_images:
    image_names.append(name_images)


i = 0
concepts = []

while i < len(image_names):
    j = 0
    while j < len(data[image_names[i]]["concepts"].keys()):
        
        for name_concepts in data[image_names[i]]["concepts"].keys():
            concepts.append(name_concepts)

        j += 1
    i += 1

print(concepts)
'''
word_1 = "User went to the caffe on fridays"


nlp = spacy.load("en_core_web_md")
nlp_1 = nlp(word_1)
for token in nlp_1:print(token.lemma_)