def getSumAvg(arg1,arg2,arg3):
    sum = arg1 + arg2 + arg3
    arg = sum / 3
    return sum , arg
sum , arg =  getSumAvg(1,2,3)
print(f"{sum} {arg}")