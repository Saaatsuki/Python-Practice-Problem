import random

def randomSanple(argList,argK):
    if len(argList)<argK:
        raise ValueError
    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0,len(argList)-1)
        sample.append(argList_copy.pop(index))
    return sample

def getJoin(argList,argSep):
    join = ""
    index = 0
    while index<len(argList):
        join += str(argList[index])
        index += 1
        if index<len(argList):
            join += argSep
    return join

def getSplit(argTxt,argSep):
    word = ""
    word_li = []
    for char in argTxt:
        if char != argSep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)

def getIn(argBig,argSmall):
    for i in argBig:
        if i==argSmall:
            return True
    return False


com_li = randomSanple([num for num in range(1,10)],3)

game_count = 0
strike = 0
ball = 0
out = 0

while game_count<5 and strike<3 and out<3:
    strike = 0
    ball = 0
    game_count += 1
    num1 , num2 , num3 = map(int,input(f"시도 {game_count} : 입력한 숫자 - ").split())
    user_li = [num1,num2,num3]

    for index in range(3):
        if com_li[index]==user_li[index]:
            strike += 1
        elif getIn(com_li,user_li[index]):
            ball += 1
    if strike == 0 and ball == 0:
        out += 1
    print(f"{strike} Strike , {ball} Ball , {out} Out")
msg = "승리" if strike==3 else "패배"
print(f"개임 종료 : {msg}\n정답 : {getJoin(com_li,' ')}")