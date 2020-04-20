import os
import subprocess



if __name__ == '__main__' :

    dir_path = os.path.dirname(os.path.realpath(__file__))

    image_processing_script = dir_path + "/image_processing/code/detection.py"

    print("---------------------------------- STARTING IMAGE PROCESSING SCRIPT ----------------------------------  ")
    #exec(open(image_processing_script).read())
    subprocess.run(image_processing_script, shell=True)
    print("----------------------------------------------  END -------------------------------------------------- \n")

    text_processing_script = dir_path + "/text_processing/NLP.py"

    print("----------------------------------  STARTING TEXT PROCESSING SCRIPT ---------------------------------- ")
    exec(open(text_processing_script).read())
    print("----------------------------------------------  END -------------------------------------------------- \n")

    confidence_script = dir_path + "/text_processing/NLP_find_confidence.py"

    print("---------------------------------- STARTING IMAGE CONFIDENCE CALCULATION SCRIPT ----------------------------------")
    exec(open(confidence_script).read())
    print("----------------------------------------------  END -------------------------------------------------- \n")

    f1_script = dir_path + "/text_processing/f1_score.py"

    print("---------------------------------- STARTING F1 SCORE CALCULATION SCRIPT ----------------------------------")
    exec(open(f1_script).read())
    print("---------------------------------------------- END -------------------------------------------------- \n")


    print ( "ALL SCRIPTS ENDED")