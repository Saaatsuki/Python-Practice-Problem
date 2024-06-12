# for num1 in range(2,10):
#     print(f"\n{num1}의 단")
#     for num2 in range(1,10):
#         print(f"{num1}X{num2}={num1*num2}")


def getGugu(arg1,arg2=0):
    # if arg2!=0:
    #     li = [i for i in range(arg1,arg2+1)]
    # else:
    #     li = [arg1]
    if arg2==0:
        arg2=arg1
    for num1 in range(arg1, arg2+1):
        print(f"\n{num1}의 단")
        for num2 in range(1,10):
            print(f"{num1} X {num2} = {num1*num2}")

getGugu(2)