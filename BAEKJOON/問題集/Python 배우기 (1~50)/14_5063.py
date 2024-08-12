T = int(input())

for _ in range(T):
    num1 , num2 , num3 = map(int,input().split())
    if num2 - num3 > num1:
        print("advertise")
    elif num2 - num3 < num1:
        print("do not advertise")
    else:
        print("does not matter")