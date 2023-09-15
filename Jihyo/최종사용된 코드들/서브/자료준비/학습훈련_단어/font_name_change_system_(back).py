import os

font_list = ["나눔 고딕","한컴 윤고딕 760","함초롱바탕"]

word_list_first = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
#ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ => 19개
word_list_second = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]
#ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ=> 21개
word_list_third = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","za","zb"]
#없음 ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ / ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ / ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ => 28개

font_list_num = ["07","08","09"]


for font in range(len(font_list)) :
    alpha_word_list_first = 0
    alpha_word_list_second = 0
    alpha_word_list_third = 0

    num = 0

    for first in range (16) :
        for second in range (12) :
                first_num = alpha_word_list_first % len(word_list_first)
                second_num = alpha_word_list_second % len(word_list_second)
                third_num = alpha_word_list_third % len(word_list_third)

                print(num)

                os.rename(f'c:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/글자 이미지 파일/이름변형본/{font_list_num[font]}/{word_list_first[first_num]}_{word_list_second[second_num]}_{word_list_third[third_num]}.{font_list_num[font]}.png',
                          f'c:/Users/USER/Desktop/동아리/글꼴 프로젝트/자료/글자 이미지 파일/글자_{font_list[font]}/글자_{font_list[font]}_{num}.png')

                num += 1
                alpha_word_list_third += 1

                if (alpha_word_list_third % len(word_list_third) == 0) : #받침을 다 돌았을 때
                     alpha_word_list_third = 0
                     alpha_word_list_second += 1
                     if (alpha_word_list_second % len(word_list_second) == 0) :
                          alpha_word_list_second = 0
                          alpha_word_list_first += 1
                          if (alpha_word_list_first % len(word_list_first) == 0) :
                               break