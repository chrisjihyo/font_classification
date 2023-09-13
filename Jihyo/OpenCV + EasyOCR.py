import os
import shutil
from PIL import Image
from PIL import ImageDraw
import easyocr
import cv2
import numpy as np
import re
import numpy as np



#
font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]


# 데이터셋 준비
for font in font_list :
    os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_data_{font}")

    for i in range(49,58): #58까지
        source = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_{font}/문장_{font}_{i}.png'
        destination = f'c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_data_{font}/sentence_data_{font}_{i}.png'
        shutil.copyfile(source, destination)


def findTallestHeight(contours) :
            heights = []

            for idx2 in range(len(contours)) :
                heights.append(cv2.boundingRect(contours[idx2])[1])     

            return max(heights)


def contains_korean(text):
    # 정규 표현식을 사용하여 주어진 문자열에서 한글 문자가 포함되어 있는지 확인
    korean_pattern = re.compile("[ㄱ-ㅎ가-힣]+")
    return bool(korean_pattern.search(text))


reader = easyocr.Reader(['ko'], gpu=False)

# OpenCV로 전처리
for font in font_list :
    os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}")
    

    for num in range(49,58) : #49,58
        os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}")
        os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_원본")
        os.mkdir(f"c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_정상")

        img = Image.open(f'c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_data_{font}/sentence_data_{font}_{num}.png')

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
        
        


        image_cut_list = []
        tallestHeight = findTallestHeight(contours)



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

            else :
                image_cut_list.append(image_cut)

        #최종적으로 저장한 이미지에 대해서 OpenCV로 전처리되어 모아진 자료들을 EasyOCR로 재검토
        for N in range(len(image_cut_list)) :
            image_path = f'c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_원본/sentence_test_result_{font}_{num}_원본_{N}.jpg'
            image_cut_list[N].save(image_path,'jpeg')
            
            
            image = Image.open(image_path).convert('L')
            results = reader.readtext(np.array(image))
            draw = ImageDraw.Draw(image)

            for detection in results:
                bbox = detection[0]
                x_min = int(bbox[0][0])
                y_min = int(bbox[0][1])
                x_max = int(bbox[2][0])
                y_max = int(bbox[2][1])

                draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=2)

                
                #만약 인식된 문자가 한글 이라면
                if contains_korean(detection[1]) == True :
                    image_cut_list[N].save(f'c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_정상/sentence_test_result_{font}_{num}_정상_{N}.png')
                    continue