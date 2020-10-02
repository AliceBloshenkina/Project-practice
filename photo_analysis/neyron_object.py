import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2

model = tensorflow.keras.models.load_model('c:\\Users\\ALISA\\like_dislike.h5', compile=True)

# images = []
# for image_name in image_list:         
img = cv2.imread('c:\\Users\\ALISA\\Desktop\\dislike.jpg')     
img = cv2.resize(img,(150,150))     
#images.append(img)  
images = np.asarray(img)
img = np.reshape(img,[1,150,150,3])
classes = model.predict_classes(img)
print(classes)

img = cv2.imread('c:\\Users\\ALISA\\Desktop\\image.jpg')     
img = cv2.resize(img,(150,150))     
#images.append(img)  
images = np.asarray(img)
img = np.reshape(img,[1,150,150,3])

classes = model.predict_classes(img)

print(classes)