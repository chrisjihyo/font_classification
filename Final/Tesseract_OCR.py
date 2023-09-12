import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/실험/model/Tesseract-OCR/tessereact.exe'  # Tesseract 실행 파일 경로 설정


from PIL import Image

# 이미지 열기
image = Image.open('C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_HY헤드라인M/문장_HY헤드라인M_0.jpg')


text = pytesseract.image_to_string(image, lang='kor')
print(text)