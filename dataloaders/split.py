from os import listdir
from os.path import isfile, join
import numpy as np 
folder = '/share/DEEPLEARNING/datasets/voc2012/VOCdevkit/VOC2012'
images = 'JPEGImages'
mask = 'SegmentationClassAug'
path = 'voc_splits/clean_train.txt'

examples = 2126

with open(path) as f:
    onlyfiles = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
onlyfiles = np.array([x.strip() for x in onlyfiles] )
np.random.shuffle(onlyfiles)

supervised = onlyfiles[:examples]
unsupervised = onlyfiles[examples+2:examples*2+2]

print(len(supervised))
print(len(unsupervised))


f_supervised = str(examples)+'_train_supervised.txt'
f_unsupervised = str(examples)+'_train_unsupervised.txt'

# Supervised
textfile = open(join('voc_splits',f_supervised), "w")

for element in supervised:
    textfile.write('/'+join(images,element+'.jpg')+' '+'/'+join(mask,element+'.png') + "\n")

textfile.close()

# Unsupervised 
textfile = open(join('voc_splits',f_unsupervised), "w")

for element in unsupervised:
    textfile.write('/'+join(images,element+'.jpg')+' '+'/'+join(mask,element+'.png') + "\n")

textfile.close()


