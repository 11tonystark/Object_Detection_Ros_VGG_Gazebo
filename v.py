from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
#from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
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
        model.add(Dense(3))
        model.add(Activation('softmax'))

      
        return model