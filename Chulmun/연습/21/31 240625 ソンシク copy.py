# 要求事項
# 1. 事前に入力された文章から検索文字列を入力し、
# 2. 入力された文字列がある場合、検索結果を出力してプログラムを終了する
# 3. もし検索結果がない場合は、検索文字列を再入力させる


# 文字列検索のための事前入力文
sentence = """      pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 改行文字が含まれた複数行文字列を出力
# print(sentence)

# """ """ 構文は複数行文字列を定義するために使用される
# これを活用して改行文字が含まれた複数行文字列を効率的に作成できる

word = "" # 単語
sentence_list = [] # sentenceをリスト化する
line = 1 # 行数
index = 0
index_list = [0] # 単語が含まれている全体のインデックスリスト
# 全体の文字数を数えるための変数設定
all_word = 0 # 総文字数
spacebar = 0 # スペース
enterword = 0 # 改行文字

for i in sentence:
    
    # 空白を見つけた場合 + wordに単語がある場合
    if i == " "  and word != "":
        sentence_list.append(word)
        word = ""
        index += 1
        index_list.append(index)
        spacebar += 1
    
    # 空白を見つけた場合 + wordに単語がない場合 (スペースが2回以上)
    elif i == " " and word == "":
        index += 1
        spacebar += 1

    # 行が終わったとき
    elif i =="\n":
        # wordに単語を追加
        if word:
            sentence_list.append(word)
            word = ""
            index_list.append(index+1)
        line += 1 # 行が終わったとき行数を1追加
        index += 5
        enterword += 1
    
    # 単語の場合
    else:
        word += i # wordに該当単語を追加
        index += 1
    
    all_word += 1 # 総文字数 += 1

# ループが終了した後、最後の単語を追加
if word:
    sentence_list.append(word)
    index_list.append(index)

# 総文字数計算
really_all_word = all_word - spacebar - enterword

# 文字列検索
while True:
    user_input = input("検索する文字列を入力してください: ")
    
    # 文字列がsentence_listに存在しない場合
    if user_input not in sentence_list:
        print("該当文字列がありません。再入力してください。")
        continue
    
    count_word = 0 # 検索された文字列の数
    index = 0 # 該当単語があるインデックス番号
    index_list1 =[] # 該当単語があるインデックス番号を追加
    
    for i in sentence_list:
        # 検索した文字列が一致する場合
        if i == user_input:
            count_word += 1 # 検索された文字 + 1
            index_list1.append(index_list[index])

        # 一致しない場合はインデックスのみ + 1
        index += 1
            
    print(f"検索された文字列の数: {count_word}")
    print(f"検索された文字列の位置: {index_list1}")
    print(f"単語の数: {index}")
    print(f"総文字数: {really_all_word}")
    print(f"行数: {line}")
    break
