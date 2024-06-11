Error = False
age = int(input("나이를 입력하세요 : "))
Error = True if age<0 else False
code = input("예약하려는 이벤트 코드를 입력하세요 (E1,E2,E3):")
Error = True if code!="E1" or code!="E2" or code!="E3" else False
date = int(input("원하는 예약 날짜를 입력하세요 : "))
Error = True if not 1<=date<=31 else False

if Error:
    msg = "잘못된 입력입니다.프로그램을 종료합니다."
else:
    if code=="E1":
        if 18<=age:
            msg = "예약이 완료되었습니다!"
        else:
            msg = "나이 제한으로 예약할 수 없습니다."
    elif code=="E2":
        if date%2==0:
            msg = "예약이 완료되었습니다!"
        else:
            msg = "선택하신 날짜에는 예약할 수 없습니다."
    else: # code=="E3"
        if not 16<=age and date%7==0:
            msg = "나이 제한으로 예약할 수 없습니다."
        elif not date%7==0 and 16<=age:
            msg = "선택하신 날짜에는 예약할 수 없습니다."
        elif not not 16<=age and not date%7==0:
            msg = "선택하신 날짜 & 나이 제한으로 예약할 수 없습니다."
        else: #elif 16<=age and date%7==0
            msg = "예약이 완료되었습니다!"

print(msg)