score_li = [92,85,34,76,58,90,61,70,45,99,82,67,50,77,89]

li1 = [i for i in score_li if 90<=i]
li2 = [i for i in score_li if 80<=i<90]
li3 = [i for i in score_li if 70<=i<80]
li4 = [i for i in score_li if 60<=i<70]
li5 = [i for i in score_li if i<60]

li = [li1,li2,li3,li4,li5]
msg = ["A","B","C","D","F"]
print("등급 분포 및 평균 점수 : ")

for i in range(len(li)):
    li_sum = 0
    [li_sum:=li_sum + j for j in li[i]]
    li_avg = li_sum / len(li[i])
    li_num_len = len(li[i])
    print(f"{msg[i]} 등급 평균 점수= {li_avg:.2f}\n{'*'*li_num_len} ({li_num_len}명)")