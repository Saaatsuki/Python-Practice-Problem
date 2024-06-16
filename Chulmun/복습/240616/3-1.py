Error = True
while Error:
    error_msg = "잘못된 입력입니다. 프로그램 종료합니다."
    age = int(input("나이를 입력하세요 : "))
    if age < 0:
        print(error_msg)
        break
    code = input("예약하려는 이벤트코드를 입력하세요 : ")
    if code not in ["E1", "E2", "E3"]:
        print(error_msg)
        break  
    date = int(input("원하는 예약 날짜는 입력하세요 : "))
    if not 0 < date <= 31:
        print(error_msg)
        break
    msg_ok = "예약 완료되었습니다!"
    msg_ng = "{} 예약할 수 없습니다." 

    age_tf = True
    date_tf = True
    if code=="E1":
        (age_tf,msg) = (False,"나이 제한으로 임해") if age<18 else (True,"")
    if code=="E2":
        (date_tf,msg) = (False,"선택하신 날짜에는") if date%2!=0 else (True,"")
    if code=="E3":
        if age<16 and date%7!=0:
            age_tf = False
            date_tf = False
            msg = "선택하신 날짜랑 나이 제한으로 임해"
        elif age<16:
            (age_tf,msg) = (False,"나이 제한으로 임해")
        elif date%7!=0:
            (date_tf,msg) = (False,"선택하신 날짜에는")

    print(msg_ok) if age_tf and date_tf else print(msg_ng.format(msg))
    Error = False