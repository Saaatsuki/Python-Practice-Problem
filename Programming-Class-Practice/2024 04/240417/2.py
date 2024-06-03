import random

bar = list()

for _ in range(0,5): # 0,1,2,3,4
    # bar.append(random.randint(1,100)) 
    bar.append(random.randint(1,100))
print(bar)
print(bar[1])
print(bar[4])
print(bar[4],bar[-1],bar[len(bar)-1])