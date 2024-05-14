import random

msg = "{}！！現在の勝敗： {}勝 {}負 {}あいこ"

lose = 0
win = 0
aiko = 0

while (win < 2 and lose < 2):
    
    janken = input("바위✊ 가위✌ 보✋중 하나를 입력하세요 : ")

    jankens = ["바위✊","가위✌", "보✋"]
    computer_janken = random.choice(jankens)
    
    if (janken=="바위✊" or janken=="가위✌" or janken=="보✋"):
        
        print("Computer ;",computer_janken)
        if((computer_janken=="바위✊" and janken=="가위✌")or(computer_janken=="가위✌" and janken=="보✋")or(computer_janken=="보✋" and janken=="바위✊")):
            lose += 1
            result = "敗北"
            print(msg.format(result,win,lose,aiko))
        elif((computer_janken=="가위✌" and janken=="바위✊")or(computer_janken=="보✋" and janken=="가위✌")or(computer_janken=="바위✊" and janken=="보✋")):     
            win  += 1
            result = "勝利"
            print(msg.format(result,win,lose,aiko))
        elif(computer_janken==janken):
            aiko += 1
            result = "あいこ"
            print(msg.format(result,win,lose,aiko))
        
    else:
        print("바위✊ 가위✌ 보✋중에서 선택하세요!!!")
        continue
    
msg2 = "{}勝　{}負　{}愛子"

if (lose == 2):
    winner="computer🖥"
elif (win == 2):
    winner="使用者👤"
    
print("決着：",msg2.format(win,lose,aiko))
print("勝者：",winner)