def Fevonach(argLen):
    fevo_li = [1,1]
    index = 2
    for i in range(argLen):
        num = fevo_li[index-2] + fevo_li[index-1]
        index += 1
        fevo_li.append(num)
    print(fevo_li)
Fevonach(8)