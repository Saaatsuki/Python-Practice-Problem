score_li = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

li1 = [i for i in score_li if 90 <= i]
li2 = [i for i in score_li if 70 <= i < 90]
li3 = [i for i in score_li if 50 <= i < 70]
li4 = [i for i in score_li if i < 50]

li = [li1, li2, li3, li4]
msg = ["우수", "양호", "보통", "미흡"]

for i in range(len(li)):
    li_sum = 0
    [li_sum := li_sum + j for j in li[i]]
    li_avg = li_sum / len(li[i])
    print(f"{msg[i]} : {li[i]} 평균 : {li_avg:.2f}")
