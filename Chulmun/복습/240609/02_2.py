suject_name = ["수학","과학","영어"]
suject_count_li = []
for i in range(3):
    suject_count = int(input(f"{suject_name[i]} 점수 입력하세요 : "))
    suject_count_li.append(suject_count)
suject_count_li_sum = 0
[suject_count_li_sum := suject_count_li_sum + i for i in suject_count_li]
suject_count_li_avg = suject_count_li_sum / len(suject_count_li)

if 90 <= suject_count_li_avg :
    msg = "A"
elif 80 <= suject_count_li_avg < 90:
    msg = "B"
elif 70 <= suject_count_li_avg < 80:
    msg = "C"
elif 60 <= suject_count_li_avg < 70 :
    msg = "D"
else :
    msg = "F"

print(f"평균 점수는 {suject_count_li_avg} 점이고, 학점은 {msg} 입니다.")