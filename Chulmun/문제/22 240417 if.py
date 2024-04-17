input_sentence = input("문자열 입력 : ")
input_word = input("단어 입력 : ")

# 文字列を単語のリストに分割
words = input_sentence.split()

count = 0

# 単語のリストをループして、指定された単語の出現回数をカウント
for word in words:
    # 大文字小文字を区別せずに比較
    if word.lower() == input_word.lower():
        count += 1

print("단어", input_word, "의 출현 빈도 : ", count)
