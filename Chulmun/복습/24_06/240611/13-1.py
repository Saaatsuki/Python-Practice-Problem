input_words = input("문자열 입력 : ")
input_word = input("단어 입력 : ")

input_words_li = input_words.split()
count = 0
for i in input_words_li:
    if input_word==i:
        count+=1

print(f"단어 '{input_word}'의 출현 빈도 : {count}")

