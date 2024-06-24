scores = [92,85,34,76,58,90,61,70,45,99]

list1 = [i for i in scores if i >= 90]
list2 = [i for i in scores if 70 <= i < 90]
list3 = [i for i in scores if 50 <= i < 70]
list4 = [i for i in scores if i < 50]

# list1_sum = 0
# for i in list1:
#     list1_sum += i
list1_sum = 0
list2_sum = 0
list3_sum = 0
list4_sum = 0
[list1_sum := list1_sum + i for i in list1]
[list2_sum := list2_sum + i for i in list2]
[list3_sum := list3_sum + i for i in list3]
[list4_sum := list4_sum + i for i in list4]

list1_ave = list1_sum / len(list1)
list2_ave = list2_sum / len(list2)
list3_ave = list3_sum / len(list3)
list4_ave = list4_sum / len(list4)

print(f"우수 : {list1} 평균 : {list1_ave}")
print(f"양호 : {list2} 평균 : {list2_ave}")
print(f"보틍 : {list3} 평균 : {list3_ave}")
print(f"미홉 : {list4} 평균 : {list4_ave}")