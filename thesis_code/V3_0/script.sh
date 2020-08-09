
cd image_processing
python3 template_json.py
python3 detection.py
cd places365
python3 run_placesCNN_unified.py
cd ..
python3 process_jsons.py
cd ..
cd text_processing
python3 NLP.py
python3 find_confidence.py
python3 f1_score.py
