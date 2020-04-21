# **code V1_0**

##Instruções e Dependências necessárias :

pip3 install tensorflow

pip3 install opencv-python

pip3 install keras

pip3 install imageai --upgrade


Ir a este repo : https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/

→ Fazer download do ficheiro **yolo.h5**

Por o ficheiro yolo.h5 no folder **/V1_0/image_processing/neural_network**

Colocar todas as imagens a analisar no folder **/V1_0/image_processing/images**

Colocar o ficheiro ground_truth json (o de 10.000.000 linhas para copiar a localidade e atividade) no folder **/V1_0/image_processing/pre_process_json/ground_data**


Download spacy : python3 -m spacy download en_core_web_md

Em principio deve estar tudo operacional depois de concluídos estes passos.



## **PARA CORRER O PROGRAMA**
Ir ao folder /V1_0/ , abrir o terminal nesse ficheiro e fazer : ./script.sh


## **RESULTADOS** 
[tópico, imagem, confiança] – folder **/V1_0/text_processing/results_confidence**

[tópico, f1_topX, score] - **folder /V1_0/text_processing/results_f1_score**