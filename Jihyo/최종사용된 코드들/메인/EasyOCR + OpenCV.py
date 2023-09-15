import os
from PIL import Image
import easyocr
import cv2
import numpy as np
import re


#"HY헤드라인M",
font_list = ["굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]
file_range = range(49, 58)

def findTallestHeight(contours) :
            heights = []

            for idx2 in range(len(contours)) :
                heights.append(cv2.boundingRect(contours[idx2])[1])     

            return max(heights)


def contains_korean(text):
    # 정규 표현식을 사용하여 주어진 문자열에서 한글 문자가 포함되어 있는지 확인
    korean_pattern = re.compile("[ㄱ-ㅎ가-힣]+")
    return bool(korean_pattern.search(text))


# EasyOCR 리더 초기화
reader = easyocr.Reader(['ko'], gpu=False)  # 언어 설정 (예: 한국어)


# EasyOCR로 먼저 작업
for font in font_list :
    font_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/결과/EasyOCR_OpenCV/sentence_test_result_{font}'
    os.makedirs(font_path, exist_ok=True)

    for num in file_range : 
        folder_path = f"{font_path}/sentence_test_result_{font}_{num}"
        original_folder = f"{font_path}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_원본"
        correct_folder = f"{font_path}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_정상"

        os.makedirs(folder_path, exist_ok=True)
        os.makedirs(original_folder, exist_ok=True)
        os.makedirs(correct_folder, exist_ok=True)

        image_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료_JPEG/sentence_data_{font}/sentence_data_{font}_{num}.jpg'

        # 이미지 열기
        image = Image.open(image_path).convert('L') #image_path에 있는 이미지 파일을 열고, 이를 그레이스케일로 변환하여 image 변수에 저장하는 코드

        # 이미지에서 문자 영역 감지
        results = reader.readtext(np.array(image))

        
        for detection_num in range(len(results)): #앞에서부터 순서대로 감지함
            # 각 detection에서 bbox 추출
            bbox = results[detection_num][0]

            # 영역 좌표 추출
            x_min = int(bbox[0][0])
            y_min = int(bbox[0][1])
            x_max = int(bbox[2][0])
            y_max = int(bbox[2][1])

            #만약 인식된 문자가 한글이 하나라도 포함되면 원본으로 저장됨.
            if contains_korean(results[detection_num][1]) == True :
                detected_text_image = image.crop((x_min, y_min, x_max, y_max))
                detected_text_image.save(f'{original_folder}/sentence_test_result_{font}_{num}_원본_{detection_num}.png')

                gray = np.array(detected_text_image)

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
                        cv2.rectangle(gray, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)

                image_cut_list = []
                tallestHeight = findTallestHeight(contours)

                for idx3 in range(len(contours)):
                    x, y, w, h = cv2.boundingRect(contours[idx3])

                    image_cut = detected_text_image.crop((x, y, x + w, y + h))

                    img_width = image_cut.size[0]
                    img_height = image_cut.size[1]

                    # 1. 단어로 묶여서 글자별로 잘라야 하는 경우

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
                    
                    # 2. 모음이나 자음이나 기호인지 확인 (contour에 있는 것들 중 가장 긴 높이 (이게 기준) 보다 높이가 0.8배보다 작은 경우 & 너비가 높이의 0.8배보다 작은 경우 -> 탈락)
                    elif (tallestHeight*0.7 < img_height ) & (img_width > img_height*0.7) :
                        image_cut_list.append(image_cut)

                    for N in range(len(image_cut_list)) :
                        image_cut_list[N].save(f'{correct_folder}/sentence_test_result_{font}_{num}_정상_{N}.png')