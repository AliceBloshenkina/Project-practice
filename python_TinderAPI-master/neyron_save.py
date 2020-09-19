# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, AveragePooling2D
# from tensorflow.keras.optimizers import SGD, RMSprop, Adam
# ## pip install tensorflow-datasets
# import tensorflow_datasets as tfds
# import tensorflow as tf
# import logging
# import numpy as np
# import time

# def dog_cat_model():
#   model = Sequential()
#   model.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
#   model.add(MaxPooling2D(pool_size=(2, 2)))
#   model.add(Conv2D(32, (3, 3), activation='relu'))
#   model.add(MaxPooling2D(pool_size=(2, 2)))
#   model.add(Flatten())
#   model.add(Dense(units=128, activation='relu'))
#   model.add(Dense(units=1, activation='sigmoid'))
#   model.compile(optimizer=Adam(),
#     loss='binary_crossentropy',
#     metrics=['accuracy'])
#   return model

# def dog_cat_train(model):
#   weighted=(80, 10, 10)
#   splits = tfds.load(weighted)
#   (cat_train, cat_valid, cat_test), info = tfds.load('cats_vs_dogs',
#     split=list(splits), with_info=True, as_supervised=True)

#   def pre_process_image(image, label):
#     image = tf.cast(image, tf.float32)
#     image = image/255.0
#     image = tf.image.resize(image, (128, 128))
#     return image, label

#   BATCH_SIZE = 32
#   SHUFFLE_BUFFER_SIZE = 1000
#   train_batch = cat_train.map(pre_process_image)
#   shuffle(SHUFFLE_BUFFER_SIZE)
#   repeat().batch(BATCH_SIZE)
#   validation_batch = cat_valid.map(pre_process_image)
#   repeat().batch(BATCH_SIZE)

#   t_start = time.time()
#   model.fit(train_batch, steps_per_epoch=4000, epochs=2,
#     validation_data=validation_batch,
#     validation_steps=10,
#     callbacks=None)
#   print("Training done, dT:", time.time() - t_start)

# model = dog_cat_model()
# dog_cat_train(model)
# model.save('dogs_cats.h5')

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('c:\\Users\\ALISA\\AppData\\Local\\Programs\\Python\\Python38\\Tinder_PP\\tf\\keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('c:\\Users\\ALISA\\Desktop\\images.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
#image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)
