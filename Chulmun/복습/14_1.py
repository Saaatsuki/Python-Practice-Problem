input_num_list = []
for key, value in {"첫":"정수","두":"부동 소수점 수"}.items():
    input_num = float(input(f"{key} 번째 ({value})를 입력하세요: "))
    input_num_list.append(input_num)
input_num_sum = 0
[input_num_sum:=input_num_sum + i for i in input_num_list]
if 100<input_num_sum:
    print(f"합이 100을 초과합니다 : {input_num_sum:.1f}")
else:
    print(f"합이 100 이하입니다 : {input_num_sum:.1f}")