password = input("비밀번호를 입력하세요 : ")

s_alp_tf = False
b_alp_tf = False
num_tf = False
len_tf = False

for i in password:
    if "A"<=i<="Z":
        b_alp_tf = True
    if "a"<=i<="z":
        s_alp_tf = True
    if "0"<=i<="9":
        num_tf = True

len_tf = True if 8<=len(password) else False

if s_alp_tf and b_alp_tf and num_tf and len_tf:
    msg = "합"
else:
    msg = "하지 않습"

print(f"비밀본호가 안전{msg}니다.")