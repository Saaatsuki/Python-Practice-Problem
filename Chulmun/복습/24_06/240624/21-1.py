def get_in(arg_big, arg_small):
    for val in arg_big:
        if val == arg_small:
            return True
    return False

def get_len(arg_sequence):
    length = 0
    for _ in arg_sequence:
        length += 1
    return length

def get_count(arg_sequence, arg_check):
    count = 0
    for val in arg_sequence:
        if val == arg_check:
            count += 1
    return count

def get_split(arg_txt, arg_sep_list):
    word_li = []
    word = ""
    for char in arg_txt:
        if not get_in(arg_sep_list, char):
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
            word_li.append(char)  # 追加: セパレータ自体もリストに含める
    if word:
        word_li.append(word)
    return word_li

sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

txt_word_li = get_split(sentence, [" ", "\n"])
txt_alp_li = [alp for alp in sentence]

user_word = input("単語を入力してください：")
while not get_in(txt_word_li, user_word):
    user_word = input("この単語はテキストに含まれていません\n単語を入力してください：")

# 入力された単語の個数
word_count = get_count(txt_word_li, user_word)

# 改行の数
enter_count = get_count(txt_alp_li, "\n")
line_count = enter_count + 1

# 全体の単語の数
all_word_count = get_len(txt_word_li)

# スペースと改行を引いた全体の文字数
all_alp_count = get_len(txt_alp_li) - (enter_count + get_count(txt_alp_li, " "))

# 入力された単語の位置（改行を4文字分、スペースを1文字分として計算）
word_inx_li = []
current_pos = 0
for inx, word in enumerate(txt_word_li):
    if word == user_word:
        word_inx_li.append(current_pos)
    
    if word == "\n":
        current_pos += 4  # 改行を4文字分として計算
    elif word == " ":
        current_pos += 1  # スペースを1文字分として計算
    else:
        current_pos += get_len(word)  # 単語の長さを追加

print(f"入力された単語の数：{word_count}")
print(f"入力された単語の位置：{word_inx_li}")
print(f"テキストの単語の数：{all_word_count}")
print(f"テキストの文字数：{all_alp_count}")
print(f"行数：{line_count}")