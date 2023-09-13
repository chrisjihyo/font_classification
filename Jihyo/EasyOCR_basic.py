"""
old_image_path = 'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_HY헤드라인M/문장_HY헤드라인M_0.png'
image = Image.open(old_image_path).convert('RGB')
image.save('C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_HY헤드라인M/문장_HY헤드라인M_0.jpg','jpeg')
"""

#이 코드를 사용할 때 주의사항 : jpg 파일만 불러올 수 있음.

from PIL import Image, ImageDraw
import easyocr
import numpy as np

old_image_path = 'c:/Users/USER/Desktop/sentence_example/sentence_seperate_01/sentence_seperate_01_cut_0.png'
image = Image.open(old_image_path).convert('RGB')
image.save('c:/Users/USER/Desktop/sentence_example/sentence_seperate_01/sentence_seperate_01_cut_0.jpg','jpeg')


# 이미지 파일 경로
image_path = 'c:/Users/USER/Desktop/sentence_example/sentence_seperate_01/sentence_seperate_01_cut_0.jpg'

# EasyOCR 리더 초기화
reader = easyocr.Reader(['ko'], gpu=False)  # 언어 설정 (예: 한국어)

# 이미지 열기
image = Image.open(image_path).convert('L')

# 이미지에서 문자 영역 감지
results = reader.readtext(np.array(image))

# 이미지에 감지된 영역 그리기
draw = ImageDraw.Draw(image)

for detection in results: #앞에서부터 순서대로 감지함
    # 각 detection에서 bbox 추출
    bbox = detection[0]

    # 영역 좌표 추출
    x_min = int(bbox[0][0])
    y_min = int(bbox[0][1])
    x_max = int(bbox[2][0])
    y_max = int(bbox[2][1])

    #print(x_min,", ",x_max)
    print(detection[1])
    
    # 영역 그리기
    draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=2)

# 이미지를 파일로 저장
image.save('C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/실험/newmodel_sample_cut/sentence_seperate_01_cut_2.jpg')

# 이미지를 화면에 표시
image.show()
