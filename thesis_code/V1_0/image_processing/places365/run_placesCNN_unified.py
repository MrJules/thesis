# PlacesCNN to predict the scene category, attribute, and class activation map in a single pass
# by Bolei Zhou, sep 2, 2017

import torch
from torch.autograd import Variable as V
import torchvision.models as models
from torchvision import transforms as trn
from torch.nn import functional as F
import os
import numpy as np
import cv2
from PIL import Image
import json
from tqdm import tqdm

def load_labels():
    # prepare all the labels
    # scene category relevant
    file_name_category = 'categories_places365.txt'
    if not os.access(file_name_category, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/categories_places365.txt'
        os.system('wget ' + synset_url)
    classes = list()
    with open(file_name_category) as class_file:
        for line in class_file:
            classes.append(line.strip().split(' ')[0][3:])
    classes = tuple(classes)

    # indoor and outdoor relevant
    file_name_IO = 'IO_places365.txt'
    if not os.access(file_name_IO, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/IO_places365.txt'
        os.system('wget ' + synset_url)
    with open(file_name_IO) as f:
        lines = f.readlines()
        labels_IO = []
        for line in lines:
            items = line.rstrip().split()
            labels_IO.append(int(items[-1]) -1) # 0 is indoor, 1 is outdoor
    labels_IO = np.array(labels_IO)

    # scene attribute relevant
    file_name_attribute = 'labels_sunattribute.txt'
    if not os.access(file_name_attribute, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/labels_sunattribute.txt'
        os.system('wget ' + synset_url)
    with open(file_name_attribute) as f:
        lines = f.readlines()
        labels_attribute = [item.rstrip() for item in lines]
    file_name_W = 'W_sceneattribute_wideresnet18.npy'
    if not os.access(file_name_W, os.W_OK):
        synset_url = 'http://places2.csail.mit.edu/models_places365/W_sceneattribute_wideresnet18.npy'
        os.system('wget ' + synset_url)
    W_attribute = np.load(file_name_W)

    return classes, labels_IO, labels_attribute, W_attribute

def hook_feature(module, input, output):
    features_blobs.append(np.squeeze(output.data.cpu().numpy()))

def returnCAM(feature_conv, weight_softmax, class_idx):
    # generate the class activation maps upsample to 256x256
    size_upsample = (256, 256)
    nc, h, w = feature_conv.shape
    output_cam = []
    for idx in class_idx:
        cam = weight_softmax[class_idx].dot(feature_conv.reshape((nc, h*w)))
        cam = cam.reshape(h, w)
        cam = cam - np.min(cam)
        cam_img = cam / np.max(cam)
        cam_img = np.uint8(255 * cam_img)
        output_cam.append(cv2.resize(cam_img, size_upsample))
    return output_cam

def returnTF():
# load the image transformer
    tf = trn.Compose([
        trn.Resize((224,224)),
        trn.ToTensor(),
        trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return tf


def load_model():
    # this model has a last conv feature map as 14x14

    model_file = 'wideresnet18_places365.pth.tar'
    if not os.access(model_file, os.W_OK):
        os.system('wget http://places2.csail.mit.edu/models_places365/' + model_file)
        os.system('wget https://raw.githubusercontent.com/csailvision/places365/master/wideresnet.py')

    import wideresnet
    model = wideresnet.resnet18(num_classes=365)
    checkpoint = torch.load(model_file, map_location=lambda storage, loc: storage)
    state_dict = {str.replace(k,'module.',''): v for k,v in checkpoint['state_dict'].items()}
    model.load_state_dict(state_dict)
    model.eval()



    # the following is deprecated, everything is migrated to python36

    ## if you encounter the UnicodeDecodeError when use python3 to load the model, add the following line will fix it. Thanks to @soravux
    #from functools import partial
    #import pickle
    #pickle.load = partial(pickle.load, encoding="latin1")
    #pickle.Unpickler = partial(pickle.Unpickler, encoding="latin1")
    #model = torch.load(model_file, map_location=lambda storage, loc: storage, pickle_module=pickle)

    model.eval()
    # hook the feature extractor
    features_names = ['layer4','avgpool'] # this is the last conv layer of the resnet
    for name in features_names:
        model._modules.get(name).register_forward_hook(hook_feature)
    return model

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

if __name__ == '__main__' :
    print("")
    print ( "------------------------------------------PlACES365 SCRIPT ----------------------------------------- \n") 
    # load the labels
    classes, labels_IO, labels_attribute, W_attribute = load_labels()

    # load the model
    features_blobs = []
    model = load_model()

    # load the transformer
    tf = returnTF() # image transformer

    # get the softmax weight
    params = list(model.parameters())
    weight_softmax = params[-2].data.numpy()
    weight_softmax[weight_softmax<0] = 0

    # load the test image
    #img_url = 'http://places.csail.mit.edu/demo/6.jpg'
    #os.system('wget %s -q -O test.jpg' % img_url)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    image_folder = os.listdir(dir_path + "/../images")
    
    folders_paths = []


    for each_folder in image_folder : 
        if each_folder != ".gitkeep" :
            folders_paths.append(dir_path + "/../images/" + each_folder)



    for each_folder_path in folders_paths:

        images_paths = []
        images_names = []
        image_info = {}

        index_bar = getIndexPositions(each_folder_path, '/')
        folder_name = each_folder_path[index_bar[len(index_bar)-1] + 1 : len(each_folder_path)]

        json_path = dir_path + "/.." + "/json_result/" + folder_name + ".json"
        image_data = json.loads(open(json_path).read())

        folder = os.listdir(each_folder_path)


        for each_image in folder :
            if each_image.startswith("2") or each_image.startswith("b") or each_image.startswith("B"):
                if(each_image.endswith(".jpg") or each_image.endswith(".png") or each_image.endswith(".JPG") or each_image.endswith(".PNG")):
                    images_paths.append(each_folder_path + "/" + each_image) 
                    images_names.append(each_image)

        print("Processing folder : " + str(folders_paths.index(each_folder_path) + 1) + "/" + str(len(folders_paths)))
        
        for image_in_folder in tqdm(images_paths):
            
            index_bar = getIndexPositions(image_in_folder, '/')
            image_name = image_in_folder[index_bar[len(index_bar)-1] + 1: len(image_in_folder)]
            except_flag = False

            try :  img = Image.open(image_in_folder)
            except : except_flag = True

            if except_flag == True : print("Exception ocurred, skipping image name : " , image_name)

            if except_flag == False:
                input_img = V(tf(img).unsqueeze(0))
                
            
                # forward pass
                logit = model.forward(input_img)
                h_x = F.softmax(logit, 1).data.squeeze()
                probs, idx = h_x.sort(0, True)
                probs = probs.numpy()
                idx = idx.numpy()

                #print('RESULT ON ' + img_url)
                        
                # output the IO prediction
                io_image = np.mean(labels_IO[idx[:10]]) # vote for the indoor or outdoor
                
                '''
                if io_image < 0.5:
                    print('--TYPE OF ENVIRONMENT: indoor')
                else:
                    print('--TYPE OF ENVIRONMENT: outdoor')
                '''
                image_data[image_name]["io_score"] = io_image

                # output the prediction of scene category
            
                for i in range(0, 5):
                    image_data[image_name]["categories"].update({classes[idx[i]] : float(probs[i])})
                

                # output the scene attributes
                responses_attribute = W_attribute.dot(features_blobs[1])
                idx_a = np.argsort(responses_attribute)
            
                for i in range(-1,-10,-1): 
                    image_data[image_name]["attributes"].append(labels_attribute[idx_a[i]])

                json.dump(image_data, open(json_path,"w"),indent=5)
