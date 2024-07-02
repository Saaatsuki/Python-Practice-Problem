def getCount(argList, argVal):
    count = 0
    for char in argList:
        if char == argVal:
            count += 1
    return count

li = []
for i in range(3):
    num = int(input())
    li.append(num)

numX_res = li[0] * li[1] * li[2]
str_numX_res = str(numX_res)
str_numX_res_li = list(str_numX_res)

for num in range(ord("0"), ord("9") + 1):
    num_str = chr(num)
    print(getCount(str_numX_res_li, num_str))