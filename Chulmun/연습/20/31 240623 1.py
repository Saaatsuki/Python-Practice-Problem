sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""


sentence_alp = [alp_com for alp_com in sentence]
print(sentence_alp)

sentence_li = []
for alp in range(len(sentence_alp)):
    if alp==" ":
        sentence_li.append()


sentence_word = ["pos","pos","hello","bar","foo","bar","foo","pos","kin","pos","test","test","pos"]


# while True:
user_word = input("검색할 문자열을 입력하세요 : ")
# if not user_word in sentence_word:
#     print("해당 문자열 업습니다. 다시 입력하세요.")

# else:
count = 0
for word in sentence_word:
    if word == user_word:
        count+=1
word_count = 0
for i in sentence_word:
    word_count+=1
enter_count = 0
for i in sentence_alp:
    if i == "\n":
        enter_count+=1
enter_count_result = enter_count+1
space_count = 0
for i in sentence_alp:
    if i == " ":
        space_count+=1
alp_count = 0
for i in sentence:
    alp_count+=1
alp_count_result = alp_count - (enter_count + space_count)
# break

print(f"入力した単語の個数：{count}\n全体の単語の個数；{word_count}\n全体の文字数：{alp_count_result}\n空白の数{enter_count_result}")

        
        


    
