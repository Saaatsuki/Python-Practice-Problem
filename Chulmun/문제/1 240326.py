# 사용자로부터 나이를 입력받습니다.
age = int(input("나이를 입력해주세요："))

# 나이에 따라 사용 가능한 이용자 유형을 나타내는 메시지를 설정합니다.
msg = "{} 이용관을 사용할 수 있습니다."


# 나이에 따라 조건 분기하여 메시지를 표시합니다.
if (age  <= 12):
    print(msg.format("어린이"))
elif (13 <= age <= 18):
    print(msg.format("창소년"))
elif (19 <= age):
    print(msg.format("성인"))