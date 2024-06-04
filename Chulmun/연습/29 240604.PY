scores = [92,85,34,76,58,90,61,70,45,99,82,67,50,77,89]

list1 = [i for i in scores if 90 < i]
list2 = [i for i in scores if 80 <= i < 90]
list3 = [i for i in scores if 70 <= i < 80]
list4 = [i for i in scores if 60 <= i < 70]
list5 = [i for i in scores if i < 60]

list1_sum = 0
list2_sum = 0
list3_sum = 0
list4_sum = 0
list5_sum = 0
[list1_sum := list1_sum + i for i in list1]
[list2_sum := list2_sum + i for i in list2]
[list3_sum := list3_sum + i for i in list3]
[list4_sum := list4_sum + i for i in list4]
[list5_sum := list5_sum + i for i in list5]

list1_ave = list1_sum / len(list1)
list2_ave = list2_sum / len(list2)
list3_ave = list3_sum / len(list3)
list4_ave = list4_sum / len(list4)
list5_ave = list5_sum / len(list5)

print("등급 분포 및 평균 점수:")
print(f"A 등급 : 평균 점수 = {list1_ave:.2f}\n{'*'*(len(list1))} ({len(list1)}명)")
print(f"B 등급 : 평균 점수 = {list2_ave:.2f}\n{'*'*(len(list2))} ({len(list2)}명)")
print(f"C 등급 : 평균 점수 = {list3_ave:.2f}\n{'*'*(len(list3))} ({len(list3)}명)")
print(f"D 등급 : 평균 점수 = {list4_ave:.2f}\n{'*'*(len(list4))} ({len(list4)}명)")
print(f"F 등급 : 평균 점수 = {list5_ave:.2f}\n{'*'*(len(list5))} ({len(list5)}명)")