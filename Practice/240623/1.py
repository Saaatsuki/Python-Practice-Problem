def getSplit(argSentence, argSplit):
    word_li = []  # 分割された単語を格納するリスト
    word = ""     # 単語の文字列を累積する変数

    for char in argSentence:
        if char != argSplit:
            word += char  # 文字が区切り文字でない場合、単語に文字を追加
        else:
            if word:
                word_li.append(word)  # 単語があればリストに追加し、単語変数をリセット
                word = ""  # 単語変数を空にする
    
    if word:
        word_li.append(word)  # 最後の単語をリストに追加する
    
    return word_li  # 分割された単語のリストを返す

# 使用例:
sent = input("文章を入力してください：")
result = getSplit(sent, " ")
print(result)
