import random

def randomSample(argSequence , argK):
    if len(argSequence)<argK:
        raise ValueError
    
    sample = []
    argSequence_copy = argSequence.copy()
    for _ in range(argK):
        index = random.randint(0,len(argSequence_copy)-1)
        sample.extend(argSequence_copy.pop(index))
    return sample

def passwordMaker(argPassLen):
    bigAlp_li = [chr(char) for char in range(ord("A"),ord("Z")+1)]
    smallAlp_li = [chr(char) for char in range(ord("a"),ord("z")+1)]
    num_li = [chr(char) for char in range(ord("1"),ord("9")+1)]
    all_li = bigAlp_li + smallAlp_li + num_li
    return randomSample(all_li,argPassLen)

def passCheck(argPassList):
    bigAlp_TF = any("A"<=val<="Z" for val in argPassList)
    smallAlp_TF = any("a"<=val<="z" for val in argPassList)
    num_TF = any("1"<=val<="9" for val in argPassList)
    return all([bigAlp_TF, smallAlp_TF, num_TF])

password_len = int(input("パスワードの長さを入力してほしいちゃむ💛："))
while not 8<=password_len:
    password_len = int(input("8文字以上でパスワードの長さを入力してほしいちゃむ💛："))

password = passwordMaker(password_len)
while not passCheck(password):
    password = passwordMaker(password_len)

print(f"パスワードができたちゃむ💙：{''.join(password)}")