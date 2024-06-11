input_words = input("문자열 입력 : ")
input_word = input("단어 입력 : ")

word_li = []
word = ""
for i in input_words:
    if i != " ":
        word += i
    else:
        word_li.append(word)
        word = ""
if word:
    word_li.append(word)

count = 0
for i in word_li:
    if input_word == i:
        count += 1

print(f"단어 '{input_word}'의 출현 빈도 : {count}")
