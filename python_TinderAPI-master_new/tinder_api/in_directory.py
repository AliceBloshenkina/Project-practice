import os
from shutil import move

def __init__(IMAGE_FOLDER):
    POS_FOLDER = IMAGE_FOLDER+"positive"
    NEG_FOLDER = IMAGE_FOLDER+"negative"
    MAIN_DIRECTORY = 'c:\\Users\\ALISA\\AppData\\Local\\Programs\\Python\\Python38\\Tinder_PP\\tensorflow-for-poets-2-master\\tf_files\\people_photos\\'

    images = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
    positive_images = filter(lambda image: (image.startswith("1_")), images)
    negative_images = filter(lambda image: (image.startswith("0_")), images)

    for pos in positive_images:
        move(IMAGE_FOLDER+pos, POS_FOLDER)

    for neg in negative_images:
        move(IMAGE_FOLDER+neg, NEG_FOLDER)

    # move(POS_FOLDER, MAIN_DIRECTORY)
    # move(NEG_FOLDER, MAIN_DIRECTORY)
    


