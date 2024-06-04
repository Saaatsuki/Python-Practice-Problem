scores = [92,85,34,76,58,90,61,70,45,99]

list1 = [i for i in scores if i >= 90]
list2 = [i for i in scores if 70 <= i < 90]
list3 = [i for i in scores if 50 <= i < 70]
list4 = [i for i in scores if i < 50]

lists = [list1,list2,list3,list4]
result = ["우수","양호","보통","미흡"]

for i in range(len(lists)):
    list_sum = 0
    [list_sum := list_sum + j for j in lists[i]]
    list_ave = list_sum / len(lists[i])
    print(f"{result[i]} : {lists[i] } 평균 : {list_ave}")