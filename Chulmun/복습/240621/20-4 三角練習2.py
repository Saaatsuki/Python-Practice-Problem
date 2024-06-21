import random

def triRandom(argNum):
    num_k = argNum * (argNum+1) // 2
    return random.sample(range(1+argNum),num_k)


tri = int(input("何段ピラミットにしますか："))
ran_li = triRandom(tri)
index = 0
for i in range(1, tri + 1):
    current_level = ran_li[index:index + i]
    ram_str = ''.join(f"{num:01d}" for num in current_level)
    print(f"{' ' * (tri - i)}{ram_str}")
    index += i