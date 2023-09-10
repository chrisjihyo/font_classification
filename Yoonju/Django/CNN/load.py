import os
import cv2
from PIL import Image
import numpy as np

data=[]
labels=[]

# ----------------
# LABELS
# 01(굴림) 0
# 02(궁서) 1
# 03(나눔고딕) 2
# 04(바탕) 3
# 05(신명조) 4
# 06(한컴소망 M) 5
# 07(한컴윤고딕 760) 6
# 08(한초롬바탕) 7
# 09(휴멍둥근헤드라인) 8
# ----------------

# 01(굴림) 0
daisys = os.listdir(os.getcwd() + "/CNN/data/01")
for x in daisys:
    imag=cv2.imread(os.getcwd() + "/CNN/data/01/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# 02(궁서) 1
dandelions = os.listdir(os.getcwd() + "/CNN/data/02/")
for x in dandelions:
    imag=cv2.imread(os.getcwd() + "/CNN/data/02/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# 03(나눔고딕) 2
roses = os.listdir(os.getcwd() + "/CNN/data/03/")
for x in roses:
    imag=cv2.imread(os.getcwd() + "/CNN/data/03/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

# 04(바탕) 3
sunflowers = os.listdir(os.getcwd() + "/CNN/data/04/")
for x in sunflowers:
    imag=cv2.imread(os.getcwd() + "/CNN/data/04/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)

# 05(신명조) 4
tulips = os.listdir(os.getcwd() + "/CNN/data/05/")
for x in tulips:
    imag=cv2.imread(os.getcwd() + "/CNN/data/05/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)

# 06(한컴소망 M) 5
sunflowers = os.listdir(os.getcwd() + "/CNN/data/06/")
for x in sunflowers:
    imag=cv2.imread(os.getcwd() + "/CNN/data/06/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(5)

# 07(한컴윤고딕 760) 6
tulips = os.listdir(os.getcwd() + "/CNN/data/07/")
for x in tulips:
    imag=cv2.imread(os.getcwd() + "/CNN/data/07/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(6)

# 08(한초롬바탕) 7
sunflowers = os.listdir(os.getcwd() + "/CNN/data/08/")
for x in sunflowers:
    imag=cv2.imread(os.getcwd() + "/CNN/data/08/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(7)

# 09(휴먼둥근헤드라인) 8
tulips = os.listdir(os.getcwd() + "/CNN/data/09/")
for x in tulips:
    imag=cv2.imread(os.getcwd() + "/CNN/data/09/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(8)

fonts=np.array(data)
labels=np.array(labels)

np.save("fonts", fonts)
np.save("labels", labels)