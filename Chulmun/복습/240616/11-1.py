import random
def passwordMachine(passLen):
    alpBig_li = [chr(i) for i in range(ord("A"),ord("Z")+1)]
    alpSmall_li = [chr(i) for i in range(ord("a"),ord("z")+1)]
    num_li_li = [chr(i) for i in range(ord("0"),ord("9")+1)]
    all_word_li = [alpBig_li,alpSmall_li,num_li_li]

    alpBig_tf = False
    alpSmall_tf = False
    num_tf = False
    pass_count_tf = False 

    while alpBig_tf and alpSmall_tf and num_tf and pass_count_tf:
        password_index_set = set()
        while passLen<=len(password_index_set):
            password_index = random.randint(0,len(all_word_li)-1)
            password_index_set.add(password_index)
        password_index_li = list(password_index_set)    
        password_li = []
        for i in password_index_li:
            password_li.append(all_word_li[i])

        for i in password_li:
            if "A"<=i<="Z":
                alpBig_tf = True
            elif "a"<=i<="z":
                alpSmall_tf = True
            elif "0"<=i<="9":
                num_tf = True
        
        pass_count_tf = True if passLen<=password_li else False
    return "".join(map(str,password_li))
    
password_len = int(input("パスワードの文字数を入力してください："))
while not 8<=password_len:
    password_len = int(input("パスワードの文字数を8文字以上で入力してください："))

passwordMachine(password_len)