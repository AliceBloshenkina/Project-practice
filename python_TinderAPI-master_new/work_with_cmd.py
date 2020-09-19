import os 
os.system("cd c:\\Users\\ALISA\\AppData\\Local\\Programs\\Python\\Python38\\Tinder_PP\\ python scripts/retrain.py
 --output_graph=c:\\Users\\ALISA\\AppData\\Local\\Programs\\Python\\Python38\\Tinder_PP\\tensorflow-for-poets-2-master\\tf_files\\retrained_graph.pb --output_labels=c:\\Users\\ALISA\\AppData\\Local\\Programs\\Python\\Python38\\Tinder_PP\\tensorflow-for-poets-2-master\\tf_files\\retrained_labels.txt --image_dir=c:\\Users\\ALISA\\AppData\\Local\\Programs\\Python\\Python38\\Tinder_PP\\tensorflow-for-poets-2-master\\tf_files\\people_photos")

python scripts/retrain.py --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/people_photos