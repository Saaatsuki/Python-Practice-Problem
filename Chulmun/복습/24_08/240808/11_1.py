import random

def getPassword(getLen):
    big_alp_li = [chr(alp) for alp in range(ord("A"), ord("Z")+1)]
    sml_alp_li = [chr(alp) for alp in range(ord("a"), ord("z")+1)]
    num_alp_li = [chr(num) for num in range(ord("0"), ord("9")+1)]

    all_char_li = [big_alp_li, sml_alp_li, num_alp_li]

    password_li = []

    for char_list in all_char_li:
        password_li.append(random.choice(char_list))
    

    while len(password_li) < getLen:
        char_list = random.choice(all_char_li)
        password_li.append(random.choice(char_list))

    random.shuffle(password_li)

    return "".join(password_li)

pas_len = int(input("Password의 길이를 입력하세요 : "))
while pas_len < 8:
    pas_len = int(input("Password의 길이를 8글자수로 입력하세요 : "))


password = getPassword(pas_len)
print("Password:", password)
