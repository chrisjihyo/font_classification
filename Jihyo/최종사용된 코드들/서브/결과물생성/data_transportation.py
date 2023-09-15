import os
import shutil

#"OpenCV_without_Idea","OpenCV","EasyOCR","OpenCV_EasyOCR"
font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]
code_list = ["EasyOCR_OpenCV"]
file_range = range(49, 58)

for code in code_list:
    for font in font_list:
        path = f'C:/Users/USER/Desktop/데이터/{code}'
        os.makedirs(path, exist_ok=True)
        new_path = f'C:/Users/USER/Desktop/데이터/{code}/result_{font}'
        os.makedirs(new_path, exist_ok=True)

        for num in file_range:
            folder_path = f'C:/Users/USER/Desktop/동아리/글꼴 프로젝트/논문자료/실험/결과/{code}/sentence_test_result_{font}/sentence_test_result_{font}_{num}'
            correct_folder = f'{folder_path}/sentence_test_result_{font}_{num}_정상'

            # correct_folder 안에 있는 파일 목록 가져오기
            files_in_correct_folder = os.listdir(correct_folder)

            # 각 파일을 new_path로 이동
            for file_name in files_in_correct_folder:
                source = os.path.join(correct_folder, file_name)
                destination = os.path.join(new_path, file_name)
                shutil.copy(source, destination)
        