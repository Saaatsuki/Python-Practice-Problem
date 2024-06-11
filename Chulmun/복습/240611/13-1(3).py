input_words = input("문자열 입력 : ")
input_word = input("단어 입력 : ")

def getSplit(argWords):
    words_li = []
    word = ""
    for i in argWords:
        if i != " ":
            word+=i
        else:
            words_li.append(word)
            word = ""
    if word:
        words_li.append(word)
    return words_li

input_words_li = getSplit(input_words)
count = 0
for i in input_words_li:
    if input_word==i:
        count+=1

print(f"단어 '{input_word}'의 출현 빈도 : {count}")