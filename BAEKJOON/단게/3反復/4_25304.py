all_money = int(input())
all_number = int(input())


moneys = []
numbers = []

for i in range(1,all_number+1):
    money,number = map(int,input().split())   
    moneys.append(money)
    numbers.append(number)
    
answer = sum([money * number for money, number in zip(moneys, numbers)])
    
if (all_money == answer):
    print("Yes")
else:
    print("No")