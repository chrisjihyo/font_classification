import os
import shutil
#from PIL import Image


#
font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]
file_range = range(49, 58)

# 데이터셋 준비
for font in font_list :
    path = f"C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/자료/sentence_data_{font}"
    os.mkdir(path)

    for num in file_range:
        source = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/문장 이미지 파일/문장_{font}/문장_{font}_{num}.png'
        destination = f'{path}/sentence_data_{font}_{num}.png'
        shutil.copyfile(source, destination)
"""
        old_image_path = destination
        image = Image.open(old_image_path).convert('RGB')
        jpeg_destination = f'{path}/sentence_data_{font}_{num}.jpg'
        image.save(jpeg_destination,'jpeg')
        os.remove(destination)"""