
import os

font_list = ["HY헤드라인M","굴림","궁서","나눔 고딕","바탕","신명조","한컴 소망 M","한컴 윤고딕 760","함초롱바탕", "휴먼둥근헤드라인"]

for font in font_list :
    count = 0
    for num in range(49,58) :
        # 폴더 경로 지정
        folder_path = f'c:/Users/USER/Desktop/recognize_and_cut_single_old_model/sentence_test_result_{font}/sentence_test_result_{font}_{num}/sentence_test_result_{font}_{num}_원본'

        # 폴더 내 파일 목록 얻기
        file_list = os.listdir(folder_path)

        # 파일 개수 세기
        count += len(file_list)

    #   결과 출력
    print(f'{font} 폴더 내 파일 개수: {count}개')
