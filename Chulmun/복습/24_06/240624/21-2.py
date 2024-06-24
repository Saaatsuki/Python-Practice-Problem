# 対象となる文字列を設定
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 文字列を単語ごとに分割し、リストに格納
word_list = []
word = ""
for char in sentence:
    if char != " " and char != "\n":
        word += char
    else:
        if word:
            word_list.append(word)
            word = ""
if word:
    word_list.append(word)

# 改行を除いた文字列を文字ごとに分割し、リストに格納
char_list = []
for char in sentence:
    if char != " " and char != "\n":
        char_list.append(char)

# 特定の文字列の位置を検索する関数を定義
def find_word_positions(target_word):
    positions = []
    current_word = ""
    newline_count = 0
    for index in range(len(sentence)):
        current_word += sentence[index]
        if (sentence[index] == " " and current_word.strip() == target_word) or (sentence[index] == "\n" and current_word.strip() == target_word):
            position = index - (len(current_word) - 1) + (4 * newline_count)
            positions.append(position)
        if sentence[index] == " " or sentence[index] == "\n":
            if sentence[index] == "\n":
                newline_count += 1
            current_word = ""
    if current_word.strip() == target_word:
        position = index - (len(current_word) - 1) + (4 * newline_count)
        positions.append(position)
    return positions, newline_count

# ユーザーに検索する文字列を入力させるループ
while True:
    input_word = input("検索する文字列を入力してください: ")
    count = 0
    for word in word_list:
        if word == input_word:
            count += 1
    if count > 0:
        print("検索された文字列の個数:", count)
        break
    print("該当する文字列がありません。もう一度入力してください。")

# 入力された文字列の位置と改行数を取得し表示
positions, newline_count = find_word_positions(input_word)
print("検索された文字列の位置:", positions)

# 単語数と改行を除いた文字数を計算し表示
print(f"単語の個数: {len(word_list)}\n全体の文字数: {len(char_list)}")
print("行数:", newline_count + 1)