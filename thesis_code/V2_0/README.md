# **code V2_0**

## Dependências necessárias a instalar

pip3 install tensorflow

pip3 install opencv-python

pip3 install keras

pip3 install imageai --upgrade

pip3 install tqdm

pip3 install torch

## SPACY installation

Seguir as instruções em : https://spacy.io/usage

Download do modelo médio : python3 -m spacy download en_core_web_md

## Downloads necessários 

No seguinte repo : https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/

→ Fazer download do ficheiro **yolo.h5**

## Cuidados necessários 

O ficheiro **yolo.h5** deve ser colocado no folder : **/V2_0/image_processing/neural_network/**

Todos os folders de imagens (2015-03-05 / 2016-04-08 / etc...) devem ser colocados no seguinte folder : **/V1_0/image_processing/images**

O ficheiro **data.json** (aquele ficheiro de 10.000.000 fornecido pelo imageclef) deve ser colocado no folder **/V2_0/image_processing/json/ground_data/** (este ficheiro serve somente para obter a "location" e "activity" das imagens processadas)

Concluidos estes passos, o programa estará pronto a correr.


## **PARA CORRER O PROGRAMA**
No folder **/V2_0/** , abrir o terminal e fazer : ./script.sh


## **RESULTADOS** 

[tópico, imagem, confiança] – folder **/V2_0/text_processing/results_confidence**

[tópico, f1_topX, score] - folder **/V2_0/text_processing/results_f1_score**