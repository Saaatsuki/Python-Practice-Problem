password = input("비밀번호를 입력하세요 : ")

alpB_tf = False
alpS_tf = False
num_tf = False
count8 = False

msg_ok = "비밀번호가 안전합니다."
msg_ng = "비밀번호가 안전하지 않습니다."

for i in password:
    if "A"<=i<="Z":
        alpB_tf = True
    elif "a"<=i<="z":
        alpS_tf = True
    elif "0"<=i<="9":
        num_tf = True
if 8<=len(password):
    count8 = True

print(msg_ok) if alpB_tf and alpS_tf and num_tf and count8 else print(msg_ng)

