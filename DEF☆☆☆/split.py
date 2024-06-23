def getSplit(input_string):
    words = []
    word = ""
    
    for char in input_string:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    
    # 最後の単語を追加する
    if word:
        words.append(word)
    
    return words

# テスト用の入力文字列
input_string = "単語1 単語2 単語3"

# getSplit() 関数を使って単語を取得する
words = getSplit(input_string)
print(words)
