# 数字ピラミットの練習
import random

def triRandom(argNum):
    num_k = argNum * (argNum+1) // 2
    return random.sample(range(1,10),num_k)

high = int(input("入力してネ☆彡　："))

ran_li = triRandom(high)
for i in range(1 , high+1):
    index = 0
    ran_str_li = "".join(map(str,ran_li[index:index+i]))
    print(f"{' '*(high-i)}{ran_str_li}")
    index+=1