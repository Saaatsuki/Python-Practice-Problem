scores = [92,85,34,76,58,90,61,70,45,99]

list_1 = [i for i in scores if i >= 90]
list_2 = [i for i in scores if 70 <= i < 90]
list_3 = [i for i in scores if 50 <= i < 70]
list_4 = [i for i in scores if i < 50]

# list_1_sum = 0
# # for i in list_1:
# #     list_1_sum += i
list_1_sum = 0
list_2_sum = 0
list_3_sum = 0
list_4_sum = 0
[list_1_sum := list_1_sum + i for i in list_1]
[list_2_sum := list_2_sum + i for i in list_2]
[list_3_sum := list_3_sum + i for i in list_3]
[list_4_sum := list_4_sum + i for i in list_4]

list_1_ave = list_1_sum / len(list_1)
list_2_ave = list_2_sum / len(list_2)
list_3_ave = list_3_sum / len(list_3)
list_4_ave = list_1_sum / len(list_4)

print(f"우수 : {list_1} 평균 : {list_1_ave}")
print(f"양호 : {list_2} 평균 : {list_2_ave}")
print(f"보틍 : {list_3} 평균 : {list_3_ave}")
print(f"미홉 : {list_4} 평균 : {list_4_ave}")