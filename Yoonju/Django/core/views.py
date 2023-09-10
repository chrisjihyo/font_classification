import os
import cv2
from PIL import Image
import numpy as np

import tensorflow as tf
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError

from django.core.files.storage import FileSystemStorage


class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def index(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        # Read the image
        imag=cv2.imread(path)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))

        test_image =np.expand_dims(resized_image, axis=0) 

        # load model
        model = tf.keras.models.load_model(os.getcwd() + '/model.h5')

        result = model.predict(test_image) 
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
        print("Prediction: " + str(np.argmax(result)))

        if (np.argmax(result) == 0):
            prediction = "굴림"
        elif (np.argmax(result) == 1):
            prediction = "궁서"
        elif (np.argmax(result) == 2):
            prediction = "나눔고딕"
        elif (np.argmax(result) == 3):
            prediction = "바탕"
        elif (np.argmax(result) == 4):
            prediction = "신명조"
        elif (np.argmax(result) == 5):
            prediction = "한컴소망 M"
        elif (np.argmax(result) == 6):
            prediction = "한컴윤고딕 760"
        elif (np.argmax(result) == 7):
            prediction = "한초롬바탕"
        elif (np.argmax(result) == 8):
            prediction = "휴멍둥근헤드라인"
        else:
            prediction = "Unknown"
        
        return TemplateResponse(
            request,
            "index.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "index.html",
            {"message": "No Image Selected"},
        )