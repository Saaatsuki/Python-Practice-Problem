T = int(input())
monet_li = []
for _ in range(T):
    num1 , num2 , num3 = map(int,input().split())
    li = [num1 , num2 , num3]

    if num1==num2==num3:
        money = (10000 + num1 * 1000)
    elif num1==num2:
        money = (1000 + num1 * 100)
    elif num2==num3:
        money = (1000 + num2 * 100)
    elif num1==num3:
        money = (1000 + num1 * 100)
    else:
        money = (max(li) * 100)
    
    monet_li.append(money)


print(max(monet_li))
