import random

def getJoin(argList, argSep):
    result = ""
    index = 0

    while index < len(argList):
        result += str(argList[index])
        index += 1
        if index < len(argList):
            result += argSep
    return result

janken = ["✊", "✌", "✋"]
com_win = 0
user_win = 0
aiko = 0

while com_win < 2 and user_win < 2:
    com_inx = random.randint(0, 2)
    com_sel = janken[com_inx]
    user_sel = input(f"{getJoin(janken, ' ')}からひとつ選んでください: ")
    user_inx = janken.index(user_sel)

    result = com_inx - user_inx

    if result == 0:
        msg = "あいこ"
        aiko += 1
    elif result == -1 or result == 2:
        msg = "敗北"
        com_win += 1
    else:
        msg = "勝利"
        user_win += 1
    print(f"コンピューター：{com_sel}\n{msg}: {user_win}勝 {com_win}敗 {aiko}あいこ")



# 最終結果を出力
if user_win == 2:
    print("あなたの勝利です！")
else:
    print("コンピューターの勝利です！")
