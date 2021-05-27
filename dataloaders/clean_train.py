from os import listdir
from os.path import isfile, join
import numpy as np 
folder = '/share/DEEPLEARNING/datasets/voc2012/VOCdevkit/VOC2012'
images = 'JPEGImages'
mask = 'SegmentationClassAug'
path = 'voc_splits/train.txt'
clean_path = 'voc_splits/clean_train.txt'
path_mask = join(folder,mask)
files_seg_aug = [f[:-4] for f in listdir(path_mask) if isfile(join(path_mask, f))]

with open(path) as f:
    train_txt = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
train_txt = [x.strip() for x in train_txt] 

clean_train = []

for e in train_txt:
    if e in files_seg_aug:
        clean_train.append(e)


textfile = open(clean_path, "w")

for element in clean_train:
    textfile.write(element + "\n")

textfile.close()





print(len(train_txt))
print(len(clean_train))
