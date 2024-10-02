import random

def password(argInt):
    b_alp_li = [chr(alp) for alp in range(ord('A'), ord('Z') + 1)]
    s_alp_li = [chr(alp) for alp in range(ord('a'), ord('z') + 1)]
    number_li = [str(num) for num in range(0, 10)]  

    all_li = b_alp_li + s_alp_li + number_li

    pass_li = []
    while len(pass_li) < argInt:
        pass_val = random.choice(all_li)
        if pass_val not in pass_li:
            pass_li.append(pass_val)

   
    b_tf = any('A' <= i <= 'Z' for i in pass_li)
    s_tf = any('a' <= i <= 'z' for i in pass_li)
    n_tf = any(i.isdigit() for i in pass_li)  

    if b_tf and s_tf and n_tf:
        print("원셩한 Password : ", "".join(pass_li)) 
    else:
        return password(argInt)  


pass_len = int(input("Password의 길을 입력하세요 : "))
while pass_len < 8:  
    pass_len = int(input("8글자 이상로Password의 길을 입력하세요 : "))

password(pass_len)
