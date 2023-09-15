import fitz
from PIL import Image
#"굴림","나눔 고딕","신명조","함초롱바탕", "HY헤드라인M","궁서","바탕","한컴 소망 M","한컴 윤고딕 760","휴먼둥근헤드라인"--> 완료
font_list = ["HY헤드라인M", "나눔 고딕","한컴 윤고딕 760","함초롱바탕"] #처음에 중괄호로 해서 'set'(리스트형) 자료가 읽히지 않아 출력되지 않았음!!
#따로 손 봐야 하는 거 :
a = 25
b = 35

for font in range(len(font_list)) :
    PDF_FILE_PATH = f"c:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/글자 문서 파일/글자_{font_list[font]}.pdf" #pdf 파일 읽기
    doc = fitz.open(PDF_FILE_PATH) #파일 받기
    num = 0

    for i, page in enumerate(doc): #파일 한 페이지 가져오기
        img = page.get_pixmap() #pdf -> png로 만들기
        img.save(f"c:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/실험/sample/글자_{font_list[font]}/글자_{font_list[font]}_{i}pg.png")

        
        source = Image.open(f'c:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/실험/sample/글자_{font_list[font]}/글자_{font_list[font]}_{i}pg.png')
        img_cropped = source.crop((a,b,595-a,841-b))
        garo = (595-2*a) / 12
        sero = (841-2*b) / 16

        #페이지별 글자 자르기
        for first in range (16) :
            for second in range(12) :
                start_x = 0 + second*garo
                start_y = 0 + first*sero
                letter_cut = img_cropped.crop((start_x, start_y, start_x + garo, start_y + sero))
                letter_cut = letter_cut.resize((int(garo*2), int(sero*2)))
                #글자 자른 거 저장하기
                letter_cut.save(f'c:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/글자 이미지 파일/글자_{font_list[font]}/글자_{font_list[font]}_{num}.png')
                num += 1
                if (num == 11172) :
                    break

        if (num == 11172) :
                    break