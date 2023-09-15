import os
from PIL import Image
import cv2
import numpy as np


#
font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]
file_range = range(49, 58)

# OpenCV로 전처리
for font in font_list :
    font_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/결과/OpenCV_without_Idea/sentence_test_result_{font}'
    os.mkdir(font_path)

    for num in file_range : 
        os.mkdir(f"{font_path}/sentence_test_result_{font}_{num}")
        os.mkdir(f"{font_path}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_정상")

        img = Image.open(f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료/sentence_data_{font}/sentence_data_{font}_{num}.png')

        large = np.array(img)
        gray = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 3))
        grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

        _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(grad.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        mask = np.zeros(bw.shape, dtype=np.uint8)

        for idx1 in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx1])
            mask[y:y+h, x:x+w] = 0
            cv2.drawContours(mask, contours, idx1, (255, 255, 255), -1)

            r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
            if r > 0.45 and w > 8 and h > 8:
                cv2.rectangle(large, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)


        for idx3 in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx3])

            image_cut = img.crop((x, y, x + w, y + h))
            image_cut.save(f'{font_path}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_정상/sentence_test_result_{font}_{num}_정상_{idx3}.png')