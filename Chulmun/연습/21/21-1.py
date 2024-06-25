def get_length(arg):
    count = 0
    for _ in arg:
        count += 1
    return count

def is_in_list(small_item, big_list):
    for item in big_list:
        if item == small_item:
            return True
    return False
        
def get_sum(num_list):
    total_sum = 0
    for num in num_list:
        total_sum += num
    return total_sum

# 入力文字列
input_string = """   pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 一文字毎のリストを作成
char_list = [char for char in input_string]

search_word = input("검색할 문자열을 입력하세요 : ")

# 単語毎のリストを作成
word_list = []
position_list = []
current_word = ""
char_index = 0
line_offset = 0

for i in range(len(input_string)):
    if input_string[i] != " " and input_string[i] != "\t" and input_string[i] != "\n":
        if current_word == "":
            char_index = i
        current_word += input_string[i]
    else:
        if current_word:
            word_list.append(current_word)
            if current_word == search_word:
                position_list.append(char_index + line_offset * 4)
            current_word = ""
        if input_string[i] == "\n":
            line_offset += 1
if current_word:
    word_list.append(current_word)
    if current_word == search_word:
        position_list.append(char_index + line_offset * 4)

# 入力された単語の数
search_word_count = 0
for word in word_list:
    if word == search_word:
        search_word_count += 1

# 全体の単語数
total_word_count = get_length(word_list)

# 改行の数
newline_count = 0
for char in char_list:
    if char == "\n":
        newline_count += 1
total_line_count = newline_count + 1

# スペースの数
space_count = 0
for char in char_list:
    if char == " ":
        space_count += 1

# 全体の文字数
total_char_count = get_length(char_list)
char_count = total_char_count - (newline_count + space_count)

print(f"검색할 문자열의 출현 횟수: {search_word_count}")
print(f"검색할 문자열의 위치: {position_list}")
print(f"단어의 총 개수: {total_word_count}")
print(f"전체 문자 수 (개행 및 공백 제외): {char_count}")
print(f"줄 수: {total_line_count}")
