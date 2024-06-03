# 사용자로부터 "left", "right", "up", "down" 중 하나의 단어를 입력받습니다.
이동 = input('"left", "right", "up", "down" 중 하나의 단어를 입력해주세요 : ')

# 이동 메시지를 포맷하는 문자열입니다.
msg = "{} 이동합니다."

# 사용자가 입력한 방향에 따라 적절한 메시지를 출력합니다.
if (이동 == "left"):
    print(msg.format("왼쪽으로"))
elif (이동 == "right"):
    print(msg.format("오른쪽으로"))
elif(이동 == "up"):
    print(msg.format("위로"))
elif(이동 == "down"):
    print(msg.format("아래로"))
else:
    print("알 수 없는 명령입니다.")