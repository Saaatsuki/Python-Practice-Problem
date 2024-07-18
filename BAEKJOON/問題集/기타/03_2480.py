num1,num2,num3 = map(int,input().split())
li_num = [num1,num2,num3]
set_num = set(li_num)


if len(set_num)==1:
    money = 10000 + num1 * 1000
elif len(set_num)==2:
    for i in li_num:
        if li_num.count(i)==2:
            num = i
    money = 1000 + num * 100
elif len(set(set_num))==3:
    money = max(li_num) * 100

print(money)