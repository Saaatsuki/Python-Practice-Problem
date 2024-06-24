import random

pass_len = int(input("Password의 글자수를 입력하세요 : "))

small_alp_list = [chr(i) for i in range(ord('a'),ord('z')+1)]
big_alp_list =[chr(i) for i in range(ord('A'),ord('Z')+1)]
num_list = [chr(i) for i in range(ord('0'),ord('9')+1)]
all_word_list = big_alp_list + small_alp_list + num_list

while True:
    password = random.sample(all_word_list, pass_len)
    password_join = "".join(password)
    tf_alp_s = False
    tf_alp_b = False
    tf_num = False
    for i in password:
        if 'a' <= i <= 'z':
            tf_alp_s = True
        elif 'A' <= i <= 'Z':
            tf_alp_b = True
        elif '0' <= i <= '9':
            tf_num = True
    if tf_alp_s and tf_alp_b and tf_num:
        break

print(password_join)
