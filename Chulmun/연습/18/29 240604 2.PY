scores = [92,85,34,76,58,90,61,70,45,99,82,67,50,77,89]

list1 = [i for i in scores if 90 < i]
list2 = [i for i in scores if 80 <= i < 90]
list3 = [i for i in scores if 70 <= i < 80]
list4 = [i for i in scores if 60 <= i < 70]
list5 = [i for i in scores if i < 60]

lists = [list1,list2,list3,list4,list5]
count = 0
print("등급 분포 및 평균 점수:")
for i in lists:
    count += 1
    list_sum = 0
    [list_sum := list_sum + j for j in i]

    list_ave = list_sum / len(i)
    alp_list = ["A","B","C","D","F"]
    alp = alp_list[count-1] 
    print( f"{alp} 등급 : 평균 점수 = {list_ave:.2f}\n{'*'*(len(i))} ({len(i)}명)")