age = int(input("나이를 입력하세요 : "))
event_code = input("예약하려는 이벤트 코드를 입력하세요 ('E1', 'E2', 'E3'): ")
while event_code not in ("E1", "E2", "E3"):
    event_code = input("'E1', 'E2', 'E3'를 입력하세요: ")

reservation_date = int(input("원하는 예약 날짜를 입력하세요 : "))
while not 1 <= reservation_date <= 31:
    reservation_date = int(input("1-31의 예약 날짜를 입력하세요 : "))

tf_age = True
tf_date = True
msg_result = ""

if event_code == "E1":
    tf_age, msg_result = (True, "") if age >= 18 else (False, "나이 제한으로 인해")
elif event_code == "E2":
    tf_date, msg_result = (True, "") if reservation_date % 2 == 0 else (False, "선택하신 날짜에는 예약할 수 없습니다.")
else:  # event_code == "E3"
    tf_age = age >= 16
    tf_date = reservation_date % 7 == 0
    if not tf_age and not tf_date:
        msg_result = "나이 제한으로 인해 선택하신 날짜에는 예약할 수 없습니다."
    elif not tf_age:
        msg_result = "나이 제한으로 인해 예약할 수 없습니다."
    elif not tf_date:
        msg_result = "선택하신 날짜에는 예약할 수 없습니다."

false_msg = f"{msg_result}"
if not tf_age or not tf_date:
    print(false_msg)
else:
    print("예약이 완료되었습니다!!")
