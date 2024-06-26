import random

def randomSample(argSequence, argK):
    if len(argSequence) < argK:
        raise ValueError("argK is larger than the length of argSequence")
    
    sample = []
    argSequence_copy = argSequence.copy()
    for _ in range(argK):
        index = random.randint(0, len(argSequence_copy) - 1)
        sample.append(argSequence_copy.pop(index))
    return sample

def passwordMaker(argPassLen):
    bigAlp_li = [chr(char) for char in range(ord("A"), ord("Z") + 1)]
    smallAlp_li = [chr(char) for char in range(ord("a"), ord("z") + 1)]
    num_li = [chr(char) for char in range(ord("0"), ord("9") + 1)]
    all_li = bigAlp_li + smallAlp_li + num_li
    password = randomSample(all_li, argPassLen)
    return password, all_li

def passCheck(argPassList):
    bigAlp_TF = any("A" <= val <= "Z" for val in argPassList)
    smallAlp_TF = any("a" <= val <= "z" for val in argPassList)
    num_TF = any("0" <= val <= "9" for val in argPassList)
    return all([bigAlp_TF, smallAlp_TF, num_TF])

# パスワードの長さをユーザーに入力させる
password, all_li = passwordMaker(1)  # all_li を初期化するために一度関数を呼び出す
password_len = int(input(f"パスワードの長さを入力してください（8文字以上{len(all_li)}文字以下）: "))

# パスワードの長さが8文字以上であり、all_li の長さ以下であることを確認
while not 8 <= password_len <= len(all_li):
    password_len = int(input(f"8文字以上{len(all_li)}文字以下でパスワードの長さを入力してください: "))

# パスワードとall_liを生成
password, all_li = passwordMaker(password_len)

# パスワードが条件を満たすか確認し、満たさない場合は再生成
while not passCheck(password):
    password, _ = passwordMaker(password_len)

# 最終的なパスワードを表示
print(f"生成されたパスワード: {''.join(password)}")
