
cd image_processing
python3 detection.py

cd pre_process_json
python3 copy_json.py
cd ..
cd places365
python3 run_placesCNN_unified.py
cd ..
cd ..
cd text_processing
python3 NLP.py
python3 NLP_find_confidence.py
python3 f1_score.py
