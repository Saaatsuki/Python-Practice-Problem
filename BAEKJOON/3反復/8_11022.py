number = int(input())

for i in range(1,number+1):
    a , b = map(int,input().split())

    
    sumAB = a + b

    msg = "Case #{}: {} + {} = {}"
    
    print(msg.format(i,a,b,sumAB))
