week_class = int(input("주당 수업 시간을  입력하세요 : "))
no_class = int(input("결석한 총 시간을 입력하세요 : "))
latey = int(input("지각 횟수를 입력하세요 : "))

no_class += latey // 3
total_classtime = week_class * 15

attend_count = 20 - (20*no_class/total_classtime)

if total_classtime*0.25<=no_class:
    print(f"당신의 출석 점수는 F점입니다.")
else:
    print(f"당신의 출석 점수는 {attend_count:.2f} 입니다.")