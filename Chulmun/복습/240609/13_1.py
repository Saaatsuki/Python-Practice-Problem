input_txt = input("문자 입력 : ")
input_txt_list = list(input_txt.split())

check_word = input("단어 입력 : ")

check_word_count = 0
for i in input_txt_list:
    if i == check_word:
        check_word_count += 1

print(f"단어 '{check_word}'의 출현 빈도 : {check_word_count}")