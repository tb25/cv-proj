# cv-proj

git clone https://github.com/AntreasAntoniou/DAGAN.git

modify the data set by converting all of the images to .npy format

then create a new class in data.py  or use the one provided in this repo with the proper load_dataset function
and make sure to update the class name in the script if you make it yourself.

finally create a new training script similar to the one provided in the DAGAN dir or use dog.py.

run the script with adding the train.npy file into the data sets. 

this has the chiuaua class from the Stanford dogs dataset http://vision.stanford.edu/aditya86/ImageNetDogs/



Then clone https://github.com/mjdietzx/SimGAN.git

change the original dataset to .h5 format and then run the training script provided with the 
generated images from the DAGAN in .h5 format as well as the original real images also in .h5

check out the slides at: https://docs.google.com/presentation/d/1brSZnAa2EZ6tBdxGZcyG0jfIJDji_q0o3sVm2pYwoCU/edit?usp=sharing
