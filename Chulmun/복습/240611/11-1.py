import random

def passwordMaker(passwordLen):
    s_alp_tf = False
    b_alp_tf = False
    num_tf = False

    s_alp_li = [chr(i) for i in range(ord('a'), ord('z')+1)]
    b_alp_li = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    num_li = [chr(i) for i in range(ord('0'), ord('9')+1)]
    all_li = s_alp_li + b_alp_li + num_li
    pass_index_set = set()
    
    while len(pass_index_set) < passwordLen:
        pass_index_set.add(random.randint(0, len(all_li)-1))
    
    pass_index_li = list(pass_index_set)
    password_li = [all_li[i] for i in pass_index_li]
    
    for i in password_li:
        if "a" <= i <= "z":
            s_alp_tf = True
        if "A" <= i <= "Z":
            b_alp_tf = True
        if "0" <= i <= "9":
            num_tf = True

    if s_alp_tf and b_alp_tf and num_tf:
        return "".join(password_li)
    else:
        return passwordMaker(passwordLen)
                      
input_pass_len = int(input("Password의 길이를 입력하세요 : "))
while not 8<=input_pass_len:
    input_pass_len = int(input("Password의 길이를 8글자수로 입력하세요 : "))
print(passwordMaker(input_pass_len))