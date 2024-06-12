def get1(arg1=1,arg2=2,arg3=3,arg4=4):
    print(arg1,arg2,arg3,arg4)

get1()
get1(6,7,8,9)
get1(6)
get1(6,7)
get1(6,7,arg4=10)

print("Hello",end="")
data = [2,3,4,5]
get1(data)