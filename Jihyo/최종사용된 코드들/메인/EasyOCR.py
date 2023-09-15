import os
from PIL import Image
import easyocr
import numpy as np


#
font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]
file_range = range(49, 58)

# 데이터셋 변환
for font in font_list :
    os.makedirs(f"C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료_JPEG/sentence_data_{font}", exist_ok=True)

    for num in file_range:
        old_image_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료/sentence_data_{font}/sentence_data_{font}_{num}.png'
        image = Image.open(old_image_path).convert('RGB')
        jpeg_destination = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료_JPEG/sentence_data_{font}/sentence_data_{font}_{num}.jpg'
        image.save(jpeg_destination,'jpeg')
        os.remove(old_image_path)


# EasyOCR 리더 초기화
reader = easyocr.Reader(['ko'], gpu=False)  # 언어 설정 (예: 한국어)

for font in font_list :
    font_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/결과/EasyOCR/sentence_test_result_{font}'
    os.makedirs(font_path, exist_ok=True)

    for num in file_range : 
        folder_path = f"{font_path}/sentence_test_result_{font}_{num}"
        correct_folder = f"{font_path}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_정상"

        os.makedirs(folder_path, exist_ok=True)
        os.makedirs(correct_folder, exist_ok=True)

        image_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료_JPEG/sentence_data_{font}/sentence_data_{font}_{num}.jpg'

        # 이미지 열기
        image = Image.open(image_path).convert('L')

        # 이미지에서 문자 영역 감지
        results = reader.readtext(np.array(image))

        i = 0
        for detection in results: #앞에서부터 순서대로 감지함
            # 각 detection에서 bbox 추출
            bbox = detection[0]

            # 영역 좌표 추출
            x_min = int(bbox[0][0])
            y_min = int(bbox[0][1])
            x_max = int(bbox[2][0])
            y_max = int(bbox[2][1])

            # 감지된 텍스트 영역을 이미지로 저장
            detected_text_image = image.crop((x_min, y_min, x_max, y_max))
            detected_text_image.save(f'{correct_folder}/sentence_test_result_{font}_{num}_정상_{i}.png')
            i += 1