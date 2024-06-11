week_class = int(input("주당 수업 시간을 입력하세요 : "))
off = int(input("결석한 총 시간을 입력하세요 : "))
late = int(input("지각 횟수를 입력하세요 : "))

total_time = week_class * 15
off += late // 3

if week_class*0.25 <= off:
    ass_msg = "F (학점 미부여)"
else:
    ass_msg = f"{20-(20*late/total_time):.2f}"
print(f"당신의 출석 점수는 {ass_msg}점입니다.")