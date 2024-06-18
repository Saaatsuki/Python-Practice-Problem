def get_check_digit(arg_ssid):
    #weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_values = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - sum_values % 11) % 10
    

# 유효한 주민번호 -> True else False
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크값 계산 알고리즘 구현 필요
    check_digit = get_check_digit(arg_ssid[:-1]) 
    
    if check_digit == arg_ssid[-1]:
        return True
    else:
        return False



is_valid_ssid(650212-2871727)