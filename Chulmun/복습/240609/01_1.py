age = int(input("사용자의 나야를 입력해주세요 : "))
msg_output = "{}이용관을 사용할 수 었습니다."

if age <= 12 :
    msg = "어린이"
elif 12 < age < 18 :
    msg = "청소년"
else:
    msg = "성인"

print(msg_output.format(msg))