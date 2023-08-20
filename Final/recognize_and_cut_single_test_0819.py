import os
import shutil
from PIL import Image
import cv2
import numpy as np

#
font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]

"""
# test 데이터셋 준비
for font in font_list :
    #os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_test/sentence_data_{font}")

    for i in range(49,58):
        source = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_{font}/문장_{font}_{i}.png'
        destination = f'c:/Users/USER/Desktop/recognize_and_cut_single_test/sentence_data_{font}/sentence_data_{font}_{i}.png'
        shutil.copyfile(source, destination)
"""


# test
for font in font_list :
    os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_test/sentence_test_result_{font}")

    for num in range(49,58) :
        img = Image.open(f'c:/Users/USER/Desktop/recognize_and_cut_single_test/sentence_data_{font}/sentence_data_{font}_{num}.png')

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
        
        def findTallestHeight() :
            heights = []

            for idx2 in range(len(contours)) :
                heights.append(cv2.boundingRect(contours[idx2])[1])     

            return max(heights)


        image_cut_list = []
        tallestHeight = findTallestHeight()



        for idx3 in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx3])

            image_cut = img.crop((x, y, x + w, y + h))

            img_width = image_cut.size[0]
            img_height = image_cut.size[1]

            if (img_height*1.7 < img_width) & (img_height > tallestHeight*0.7) :
                n = 1
                img_width_copy = img_width
                while (img_width_copy >= img_height) :
                    img_width_copy -= img_height
                    n += 1
                
                img_cut_width = round(img_width / n, 2)

                for i in range(n) :
                    image_cuts = image_cut.crop((i*img_cut_width, 0, (i+1)*img_cut_width, img_height))
                    image_cut_list.append(image_cuts)

            elif (tallestHeight*0.7 < img_height ) & (img_width > img_height*0.7) :
                image_cut_list.append(image_cut)
            
        for num in range(len(image_cut_list)) :
            image_cut_list[num].save(f'c:/Users/USER/Desktop/recognize_and_cut_single_test/sentence_test_result_{font}/sentence_test_result_{font}_{num}_cut_{n}.png')

    


