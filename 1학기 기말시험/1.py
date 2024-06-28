import random

def getIn(argBig,argSmall):
    for i in argBig:
        if i == argSmall:
            return True
    return False

def getCount(argList,argVal):
    count = 0
    for i in argList:
        if i == argVal:
            count += 1
    return count

def getMax(argList):
    max = argList[0]
    for i in argList:
        if max<i:
            max=i
    return max

# ユーザーからサイコロの回数を受け取る
dice_count = int(input("Enter the number of dice rolls (between 100 and 1,000,000) : "))
while not 100<=dice_count<=1000000:
    dice_count = int(input("Please enter a number within the seccified range.\nEnter the number of dice rolls (between 100 and 1,000,000) : "))

# サイコロの目の値をランダムに生成
dice_all_li = []
for _ in range(dice_count):
    dice_num = random.randint(1,6)
    dice_all_li.append(dice_num)

# 1～6それぞれの数字毎に確認、出力
count_li = []
persent_li = []
star_li = []
for i in range(6):
    if getIn(dice_all_li,i+1):
        count = getCount(dice_all_li,i+1)
        count_li.append(count)

    persent = (count_li[i] / dice_count) * 100
    persent_li.append(persent)

    max = getMax(count_li)

    star = (count_li[i] / max) * 10
    star_li.append(star)

    print(f"{i+1}: {'*'*(int(star_li[i]))} ({count_li[i]} times , {(persent_li[i]):.2f}%)")


# for i in range(1,7):
#     if getIn(dice_all_li,i):
#         count = getCount(dice_all_li,i)
#         count_li.append(count)


# for i in range(6):
#     persent = (count_li[i] / dice_count) * 100
#     persent_li.append(persent)

# max = getMax(dice_all_li)

# for i in range(6):
#     star = (count_li[i] / max) * 10
#     star_li.append(star)

# for i in range(6):
#     print(f"{i+1}: {'*'*(int(star_li[i]))} ({count_li[i]} times , {(persent_li[i]):.2f}%)")
