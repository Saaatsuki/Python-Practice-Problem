sub_li = ["수학","과학","영어"]
score_li = []
for i in range(3):
    score = float(input(f"{sub_li[i]} 점수를 입력하세요 : "))
    score_li.append(score)
score_li_sum = 0
[score_li_sum:=score_li_sum + i for i in score_li]
score_avg = score_li_sum / len(score_li)
ass = "A" if 90<=score_avg else "B" if 80<=score_avg<90 else "C" if 70<=score_avg<80 else "D" if 60<=score_avg<70 else "F"
print(f"평균 점수는 {score_avg:.1f}점이고,학점은 {ass}입니다")