txt = input("문자열 입력 : ")
word = input("단어 입력 : ")

txt_li = txt.split()
word_count = len([i for i in txt_li if i==word])
print(f"단어 '{word}'의 출현 빈도 : {word_count}")