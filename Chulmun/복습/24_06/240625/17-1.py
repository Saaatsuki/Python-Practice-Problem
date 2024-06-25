import random

def randomSample(argList,argK):
    if len(argList)<argK:
        raise ValueError
    sample = []
    argList_li = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList_li)-1)
        sample.append(argList_li.pop(index))
    return sample

def getIn(argBig,argSmall):
    for i in argBig:
        if i == argSmall:
            return True
    return False

def getJoin(argList,argSep):
    join = ""
    index = 0
    while index<len(argList):
        join += argList[index]
        index += 1
        if index<len(argList):
            join += argSep
    return join

word_li = []
for i in ["첫","두","세"]:
    word = input(f"{i}번째 단어를 입력 하세요\n")
    while not 3<=len(word)<=20:
        word = input(f"3이상 20이하 글자로 구성된 {i}번째 단어를 입력 하세요\n")

    word_li.append(word)

com_word_index = random.randint(0, len(word_li) - 1)
com_word = word_li[com_word_index]
com_word_li = list(com_word)
print(f"단어 선택 완료 개임를 시착합니다.선택된 단어 : {com_word}")

com_word_len = len(com_word) 
hide_count = int(com_word_len * 0.5) if com_word_len % 2 == 0 else int(com_word_len * 0.5 + 0.5)

hide_index = randomSample([num for num in range(com_word_len)], hide_count)

com_word_hide = com_word_li[:]
for index in hide_index:
    com_word_hide[index] = "_"

game_count = 0
while getIn(com_word_hide,"_"):
    game_count += 1
    alp = input(f"{game_count}번째 시도 : 아래 단어을 구성하는 알파벳 한 개 입력하세요.\n{getJoin(com_word_hide,' ')}\n")


    count = 0
    for index in hide_index:
        if com_word_li[index]==alp:
            com_word_hide[index]=alp
            count += 1
    if count == 0:
        msg = "단어 내 포함되지 않은 알파벳입니다."
    else:
        msg = f"입력한 알파벳 단어 내 포함 : {count}글자"
    print(msg)
print(f"Clear - 선택된 단어 : {com_word} , 총 시도 횟수 : {game_count}")