import cv2
import numpy as np
from PIL import Image
import os


font_list_num = ["01","02","03","04","05","06","07","08","09","10"]

for num in range(len(font_list_num)):
    img = Image.open(f'c:/Users/USER/Desktop/sentence_example/sentence_{font_list_num[num]}.png')
    
    large = np.array(img)
    small = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY) #색감 흑백으로 바꾸기 / threshold를 사용하기 위해 필요

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 3)) #구조화 요소 커널의 모양 타원형으로 / morphologyEx(경계 추출) 작업을 위해 필요
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel) #그레디언트 = 팽창 - 침식 => 경계를 검출하는 효과

    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #threshold = 경계값을 기준으로 양 극단으로  값 고정시키기 / Otsu 알고리즘으로 선택된 경계 값 출력
# threshold(이미지, 픽셀 문턱값, 픽셀 문턱값보다 클 때 적용되는 최대값,문턱값 적용 방법 또는 스타일)


#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) #구조화 요소 커널의 모양 직사각형으로
#connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel) #닫힘 = 팽창 + 침식 / 닫힘 연산은 주변보다 어두운 노이즈를 제거 -> 효과적이면서 끊어져 보이는 개체를 연결하거나 구멍을 메우는 데 효과적
# using RETR_EXTERNAL instead of RETR_CCOMP
    contours, hierarchy = cv2.findContours(grad.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #객체의 외곽선 좌표를 모두 추출하는 작업 
# EXTERNAL = 계층 정보 x, 바깥 외곽선만 검출해 단순히 리스트로 묶어줌 / 
    mask = np.zeros(bw.shape, dtype=np.uint8)

    for idx in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[idx]) #해당 contour에 외접하는 똑바로 세워진 사각형 (좌상단 꼭지점 좌표 x,y, 가로폭, 세로폭)
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1) #객체의 외곽선 좌표를 이용해 외곽선을 그리는 작업 
    
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h) # 0이 아닌 값만 개수 세기
        if r > 0.45 and w > 8 and h > 8:
            cv2.rectangle(large, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)

# show image with contours rect
    cv2.imshow('rects', large)
    cv2.waitKey()

    os.mkdir(f"c:/Users/USER/Desktop/sentence_example/sentence_seperate_{font_list_num[num]}")

    for idx in range(len(contours)): #순서가 꺼꾸로 되어있음
        x, y, w, h = cv2.boundingRect(contours[idx])

        image_cut = img.crop((x, y, x + w, y + h))
        image_cut.save(f'c:/Users/USER/Desktop/sentence_example/sentence_seperate_{font_list_num[num]}/cut_{idx}.png')