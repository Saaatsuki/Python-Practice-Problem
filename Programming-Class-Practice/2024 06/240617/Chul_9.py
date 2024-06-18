def numberCheck(argList):
    checkNum_li = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]  
                # [(value % 8) + 2 for value in range(12)]
    mul_res_li = []
    for index in range(12):
        mul_res = int(argList[index]) * checkNum_li[index]
        mul_res_li.append(mul_res)
    mul_res_li_sum = 0
    for i in mul_res_li:
        mul_res_li_sum += i
    result = 11 - mul_res_li_sum % 11
    if result >= 10:
        result = result % 10
    if result == int(argList[12]):
        return True
    else:
        return False
    
country_num_str = input("주민 번호를 입력하세요 : ")
country_num_li = country_num_str.split("-")
country_num_li_all = "".join(country_num_li)
if numberCheck(country_num_li_all):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")