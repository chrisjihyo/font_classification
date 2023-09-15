import os
import shutil
#"HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"


# 사용할 폰트와 범위 설정
font_list = ["굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]
file_range = range(49, 58)

for font in font_list:
    for num in file_range:
        folder_path = f'c:/Users/USER/Desktop/recognize_and_cut_single_new_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}'
        original_folder = f'{folder_path}/sentence_test_result_{font}_{num}_원본'
        correct_folder = f'{folder_path}/sentence_test_result_{font}_{num}_정상'
        abnormal_folder = f'{folder_path}/sentence_test_result_{font}_{num}_비정상'

        os.makedirs(abnormal_folder, exist_ok=True)  # 비정상 이미지 저장 폴더 생성

        # 원본 이미지와 정상 이미지 파일 목록을 가져옵니다.
        original_files = os.listdir(original_folder)
        correct_files = os.listdir(correct_folder)

        # 비정상 이미지 폴더의 이미지 목록을 가져옵니다.
        abnormal_files = os.listdir(abnormal_folder)

        for original_file in original_files:
            original_number = int(original_file.rsplit('_', 1)[1].split('.')[0])

            print("원본 num : "+str(original_number))
            
            # 원본 이미지 파일명에서 맨 마지막 숫자를 추출합니다.
            if original_number not in [int(file.rsplit('_', 1)[1].split('.')[0]) for file in correct_files] and original_file not in abnormal_files:
                source = os.path.join(original_folder, original_file)
                destination = os.path.join(abnormal_folder, original_file)
                shutil.copyfile(source, destination)