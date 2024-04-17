# 使用者に文章と単語を入力
input_sentence = input("문자열 입력 : ")
input_word = input("단어 입력 : ")

#　単語を一時的に保管するリストを作成
words = []
#　現在の単語を構築するためのからの文字列を作成
current_word = ""

#　入力された文字列を一文字ずつ処理し、単語を取得
for char in input_sentence:
    #　空白でない場合、現在の単語に文字を追加
    if (char != " "):
        current_word += char
    else:
        #　空白の場合、現在の単語が完成したのでリストに追加現在の単語をリセット
        #　現在の単語をリセット
        words.append(current_word)
        current_word = ""

        
#　最後の単語を処理するために残っている場合、リストに追加        
if current_word :
    words.append(current_word)

#　単語の出現数をカウント
count = 0
for word in words:
    if (word == input_word):
        count += 1

print("단어",input_word,"의 출현 빈도 : ",count)