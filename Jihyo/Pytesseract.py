from PIL import Image
from PIL import ImageDraw
import pytesseract
#export TESSDATA_PREFIX='C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/실험/model/tesseract/tessdata'


# 이미지를 열고 문자 영역 감지
image_path = 'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_궁서/문장_궁서_57.jpg'
image = Image.open(image_path)
boxes = pytesseract.image_to_boxes(image, lang='kor')
print(boxes)

# 이미지를 그릴 복사본 만들기
image_copy = image.copy()
draw = ImageDraw.Draw(image_copy)

# 감지된 영역 처리 및 이미지에 그리기
for box in boxes.splitlines():
    b = box.split()
    char = b[0]
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    
    # 감지된 영역을 사각형으로 그리기
    draw.rectangle([x, y, w, h], outline='red', width=2)


# 이미지를 파일로 저장
image_copy.save('C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/실험/newmodel_sample_cut/sentence_seperate_01_cut_1.png')

# 이미지를 화면에 표시
image_copy.show()
