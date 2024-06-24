input_words = input("문자열 입력 : ")
input_word = input("단어 입력 : ")

count = 0
index = 0
while index < len(input_words):
    if input_words[index:index+len(input_word)] == input_word:
        count += 1
        index += len(input_word)
    else:
        index += 1

print(f"단어 '{input_word}'의 출현 빈도 : {count}")