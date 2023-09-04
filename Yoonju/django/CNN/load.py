import os
import cv2
from PIL import Image
import numpy as np

data=[]
labels=[]

# ----------------
# LABELS
# daisy 0
# dandelion 1
# rose 2
# sunflower 3
# tulip 4
# ----------------

# Daisy 0
daisys = os.listdir(os.getcwd() + "/CNN/data/daisy")
for x in daisys:
    imag=cv2.imread(os.getcwd() + "/CNN/data/daisy/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# Dandelion 1
dandelions = os.listdir(os.getcwd() + "/CNN/data/dandelion/")
for x in dandelions:
    imag=cv2.imread(os.getcwd() + "/CNN/data/dandelion/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# Roses 2
roses = os.listdir(os.getcwd() + "/CNN/data/rose/")
for x in roses:
    imag=cv2.imread(os.getcwd() + "/CNN/data/rose/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

# Sunflowers 3
sunflowers = os.listdir(os.getcwd() + "/CNN/data/sunflower/")
for x in sunflowers:
    imag=cv2.imread(os.getcwd() + "/CNN/data/sunflower/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)

# Tulips 4
tulips = os.listdir(os.getcwd() + "/CNN/data/tulip/")
for x in tulips:
    imag=cv2.imread(os.getcwd() + "/CNN/data/tulip/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)


flowers=np.array(data)
labels=np.array(labels)

np.save("flowers", flowers)
np.save("labels", labels)