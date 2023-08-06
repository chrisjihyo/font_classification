import cv2
import numpy as np
from PIL import Image
import os

img = Image.open(f'c:/Users/USER/Desktop/sentence_example/sentence_10.png')
    
large = np.array(img)
gray = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY) #색감 흑백으로 바꾸기 / threshold를 사용하기 위해 필요

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 3)) #구조화 요소 커널의 모양 타원형으로 / morphologyEx(경계 추출) 작업을 위해 필요
grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel) #그레디언트 = 팽창 - 침식 => 경계를 검출하는 효과

_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #threshold = 경계값을 기준으로 양 극단으로  값 고정시키기 / Otsu 알고리즘으로 선택된 경계 값 출력
# threshold(이미지, 픽셀 문턱값, 픽셀 문턱값보다 클 때 적용되는 최대값,문턱값 적용 방법 또는 스타일)

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
#cv2.imshow('rects', large)
#cv2.waitKey()


########### 확인 마쳤으니 검사해서 저장 ##############

def findTallestHeight() :
    heights = []

    for idx in range(len(contours)) :
        heights.append(cv2.boundingRect(contours[idx])[1])     

    return max(heights)


image_cut_list = []
tallestHeight = findTallestHeight()


# 검토해서 새로운 배열(image_cut_list)에 순서대로 저장

for idx in range(len(contours)): #순서가 꺼꾸로 되어있음
    x, y, w, h = cv2.boundingRect(contours[idx])

    image_cut = img.crop((x, y, x + w, y + h)) #좌측상단의 xy좌표, 우측하단의 xy좌표

    img_width = image_cut.size[0] #가로
    img_height = image_cut.size[1] #세로

    #cv2.imshow('cut', np.array(image_cut))
    #cv2.waitKey()

    #오차 범위는 어디까지 해야 하지...? 모든 글씨체에 적용할 수 있을까...?

    # 1. 단어로 묶여서 글자별로 잘라야 하는 경우

    # (일단 보통 글씨체들이 글자별로 봤을 때 높이와 세로가 너무 심하게 차이가 안난다는 전제하에 일단 진행)
    if (img_height*1.7 < img_width) & (img_height > tallestHeight*0.7) : #2글자 이상으로 묶여 있는 경우
        n = 1
        img_width_copy = img_width
        while (img_width_copy >= img_height) :
            img_width_copy -= img_height
            n += 1

        img_cut_width = round(img_width / n, 2)
        #print("2글자 이상으로 묶여 있는 경우")

        #잘라서 저장

        #cv2.imshow('cutcutcut', np.array(image_cut))
        #cv2.waitKey()

        for i in range(n) :
            image_cuts = image_cut.crop((i*img_cut_width, 0, (i+1)*img_cut_width, img_height))
            image_cut_list.append(image_cuts)
            #print("2글자 이상으로 묶여 있는 경우 : 컷한 거")
            #cv2.imshow('cutcutcut', np.array(image_cuts))
            #cv2.waitKey()

    # 2. 모음이나 자음이나 기호인지 확인 (contour에 있는 것들 중 가장 긴 높이 (이게 기준) 보다 높이가 0.8배보다 작은 경우 & 너비가 높이의 0.8배보다 작은 경우 -> 탈락)
    elif (tallestHeight*0.7 < img_height ) & (img_width > img_height*0.7) :
        #print("img_width : ",img_width)
        #print("img_height : ",img_height)
        #print("낱개로 원래 쪼개진 것들 중 최종적으로 살아남음")
        image_cut_list.append(image_cut)
    
for num in range(len(image_cut_list)) :
    image_cut_list[num].save(f'c:/Users/USER/Desktop/sentence_example/sentence_seperate_10/sentence_seperate_10_cut_{num}.png')

