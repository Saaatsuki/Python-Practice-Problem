def getCount(argList, argVal):
    count = 0
    for i in argList:
        if i == argVal:
            count += 1
    return count

def getMax(argList):
    max_val = argList[0]
    for i in argList:
        if i > max_val:
            max_val = i
    return max_val

import random

dice_count = int(input("サイコロを振る回数を入力してください："))
while not 100 <= dice_count <= 1000000:
    dice_count = int(input("100~1000000で、サイコロを振る回数を入力してください："))

dice_val_li = []
for _ in range(dice_count):
    dice_val = random.randint(1, 6)
    dice_val_li.append(dice_val)

count_li = []
for i in range(6):
    count = getCount(dice_val_li, i + 1)
    count_li.append(count)

max_count = getMax(count_li)

star_li = []
percent_li = []
for i in range(6):
    star = int((count_li[i] / max_count) * 10)  # 小数を整数に変換
    star_li.append(star)

    percent = count_li[i] / dice_count * 100
    percent_li.append(percent)

    print(f"{'*' * star_li[i]} ({count_li[i]} 回, {percent_li[i]:.2f} %)")
