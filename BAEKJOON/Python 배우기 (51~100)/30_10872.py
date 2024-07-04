def getX(argList):
    res = 1
    for i in argList:
        res *= i
    return res

num = int(input())

li = []
for i in range(num):
    li.append(i+1)

print(getX(li))