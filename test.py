
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib

import numpy as np
import os
import cv2
import pickle
import random

img = image.load_img("/home/tony/gaip/bot1/img/rolls.jpeg",target_size=(96,96))
img = np.asarray(img)
x = img_to_array(img)
x = x/255
plt.imshow(x)
img = np.expand_dims(x, axis=0)

saved_model = load_model("/home/tony/gaip/bot1/mymod1.h5")
output = saved_model.predict(img)
print(output)
