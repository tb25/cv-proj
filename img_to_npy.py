# import numpy as np
# import os

# path = "/data_road_biking"

# for im in os.listpath.dir(path):
# 	np.save('im.npy', im)

import cv2
import glob
import numpy as np
#Train data
train = []
files = glob.glob ("/data_road_biking/*.jpg") # your image path
for myFile in files:
    image = cv2.imread (myFile)
    train.append (image)
    train_labels.append([1., 0.])

train = np.array(train,dtype='float32') #as mnist
# convert (number of images x height x width x number of channels) to (number of images x (height * width *3)) 
# for example (120 * 40 * 40 * 3)-> (120 * 4800)
# train = np.reshape(train,[train.shape[0],train.shape[1]*train.shape[2]*train.shape[3]])

# save numpy array as .npy formats
np.save('train',train)
