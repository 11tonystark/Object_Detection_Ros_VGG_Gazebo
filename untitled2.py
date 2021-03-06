# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pvR241g57mqKOfF67AkeWhTacysP2HMH
"""

from google.colab import drive
drive.mount('/content/drive')

import keras

from keras.models import Sequential
from keras.layers.normalization import BatchNormalization


from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
from keras.layers.core import Activation,Flatten,Dense,Dropout
#from keras.layers.core import Activation,Flatten,Dense,Dropout

from keras import backend as k

train_path='/content/drive/My Drive/big_data'

from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D,MaxPooling2D
#from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
from keras.layers.core import Activation,Flatten,Dense,Dropout
from keras import backend as k
#c=conv2D+ReLU+BN
class tinyVGG:
    @staticmethod
    def build(height,width,depth,classes):
        model=Sequential()
        input_shape=(height,width,depth)
        channel_dim=-1
        if(k.image_data_format()=='channel_first'):
            input_shape=(depth,height,width)
            
        

        model.add(Conv2D(input_shape=input_shape,filters=64,kernel_size=(3,3),padding="same", activation="relu"))
        #model.add(Conv2D(64,(3,3),padding='same',input_shape=input_shape))
        #model.add(Activation('relu'))
        model.add(Conv2D(64,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128,(3,3),padding='same'))
        model.add(Activation('relu'))
       # model.add(BatchNormalization(axis=channel_dim))
        model.add(Conv2D(128,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(0.25))

        model.add(Conv2D(256,(3,3),padding='same'))
        model.add(Activation('relu'))
      #  model.add(BatchNormalization(axis=channel_dim))
        model.add(Conv2D(256,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(0.25))
        
        model.add(Flatten())
        model.add(Dense(4096))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.25))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))
        return model
        '''
        #model.add(Conv2D(64,(3,3),padding='same',input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(Conv2D(64,(3,3),padding='same'))
        model.add(Activation('relu'))
      # model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128,(3,3),padding='same'))
        model.add(Activation('relu'))
       # model.add(BatchNormalization(axis=channel_dim))
        model.add(Conv2D(128,(3,3),padding='same'))
        model.add(Activation('relu'))
     #   model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(0.25))

        model.add(Conv2D(256,(3,3),padding='same'))
        model.add(Activation('relu'))
      #  model.add(BatchNormalization(axis=channel_dim))
        model.add(Conv2D(256,(3,3),padding='same'))
        model.add(Activation('relu'))
      #  model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Dropout(0.25))
        
        model.add(Flatten())
        model.add(Dense(4096))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))
        return model
        '''
        '''
       # model.add(Conv2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
        model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
        model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(BatchNormalization(axis=channel_dim))
        #model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
       # model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
       # model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
       # model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        #model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
       # model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
       # model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
        model.add(Dropout(0.25))

        
        model.add(Flatten())
        model.add(Dense(4096))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        model.add(Dense(1))##from 3 to 2
        model.add(Activation('sigmoid'))

      '''
        return model

import matplotlib.pyplot as plt
import matplotlib
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from keras.optimizers import Adam
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from imutils import paths
import numpy as np
import os
import cv2
import pickle
import random

HP_LR= 1e-3
HP_EPOCHS=15
HP_BS = 32
HP_IMAGE_DIM=(96,96,3)
data=[]
classes=[]
imagepaths = sorted(list(paths.list_images(train_path)))
print(imagepaths)
random.seed(42)
random.shuffle(imagepaths)

for imgpath in imagepaths:
	try:
		image = cv2.imread(imgpath)
		image= cv2.resize(image,(96,96))
		image_array = img_to_array(image)
		data.append(image_array)
		label=imgpath.split(os.path.sep)[-2]
		classes.append(label)
	except Exception as e:
		print(e)

data=np.array(data,dtype='float')/255.0
labels=np.array(classes)

lb= LabelBinarizer()
labels = lb.fit_transform(labels)


xtrain,xtest,ytrain,ytest = train_test_split(data,labels,test_size=0.2,random_state=42)

aug= ImageDataGenerator(rotation_range=0.25,width_shift_range=0.1,height_shift_range=0.1,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')

model = tinyVGG.build(height=96,width=96,depth=3,classes=len(lb.classes_))

opt = Adam(lr=HP_LR,decay=HP_LR/HP_EPOCHS)

model.compile(loss='binary_crossentropy',optimizer = opt,metrics = ['accuracy'])

H=model.fit_generator(aug.flow(xtrain,ytrain,batch_size= HP_BS),validation_data=(xtest,ytest),steps_per_epoch=len(xtrain)//HP_BS,epochs=HP_EPOCHS)
model.save('mymodtt2.h5')
'''
plt.plot(H.history["acc"])
plt.plot(H.history['val_acc'])
plt.plot(H.history['loss'])
plt.plot(H.history['val_loss'])
plt.title("model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(["Accuracy","Validation Accuracy","loss","Validation Loss"])
plt.show()
'''

from keras.preprocessing import image

img = image.load_img("/content/drive/My Drive/traffic.jpeg",target_size=(96,96))
#img = image.load_img("/content/drive/My Drive/bel.jpeg",target_size=(96,96))

img = np.asarray(img)

x = img_to_array(img)
x = x/255

plt.imshow(x)

img = np.expand_dims(x, axis=0)

from keras.models import load_model

saved_model = load_model("/content/mymodtt2.h5")

output = saved_model.predict(img)

print(output)