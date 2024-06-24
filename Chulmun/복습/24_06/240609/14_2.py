input_num_str = input("숫자들을 쉼표로 구분하여 입력하세요 : ")
input_num_str_list = input_num_str.split(",")
input_num_list = [int(i) for i in input_num_str_list]

output_number = []
input_num_list_sum = 0
for i in input_num_list:
    if input_num_list_sum > 100:
        break
    input_num_list_sum += i
    output_number.append(i)

input_num_list_sum_all = 0
[input_num_list_sum_all:= input_num_list_sum_all + i for i in input_num_list]
if input_num_list_sum >= 100:
    print(f"총합된 100를 초과하였습니다.\n현재까지의 입력값들 : {output_number}\n현재까지의 총합 : {input_num_list_sum}")
else:
    print(f"총합된 100를 초과하지 않았습니다.\n입력된 모든 숫자들 : {input_num_list}\n최종 총합 : {input_num_list_sum_all}")
