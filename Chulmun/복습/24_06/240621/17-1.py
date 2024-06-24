import random

def getComRandom(argList):
    com_ran_ind = random.randint(0, len(argList) - 1)
    return argList[com_ran_ind]

def getHideIndex(argList):
    hide_count = int(len(argList) * 0.5) if (len(argList) % 2 == 0) else int(len(argList) * 0.5 + 0.5)
    return random.sample(range(len(argList)), hide_count)

word_li = []
for i in ["첫", "두", "세"]:
    word = input(f"{i}번째 단어를 입력하세요\n")
    while not 3 <= len(word) <= 20:
        word = input(f"3이상 20이하의 {i}번째 단어를 입력하세요\n")
    word_li.append(word)

com_word = getComRandom(word_li)
print(f"단어 선택완료 게임 시작합니다. 선택된 단어 : {''.join(com_word)}")

hide_index_li = getHideIndex(com_word)

com_word_hide_li = list(com_word)
for i in hide_index_li:
    com_word_hide_li[i] = "_"

game_count = 0
while "_" in com_word_hide_li:
    game_count += 1
    alp = input(f"{game_count}번째 시도 : 아래 단어를 구성하는 알파벳 한 개 입력하세요\n{''.join(com_word_hide_li)}\n")
    
    count = 0
    for i in hide_index_li[:]:  
        if com_word[i] == alp:
            com_word_hide_li[i] = alp
            hide_index_li.remove(i)  
            count += 1
    if count == 0:
        print("단어 내 포함되지 않은 알파벳입니다.")
    else:
        print(f"입력한 알파벳 단어 내 포함 : {count}글자")
print(f"Clear - 선택된 단어 : {''.join(com_word)} , 총 시도 횟수 : {game_count}")