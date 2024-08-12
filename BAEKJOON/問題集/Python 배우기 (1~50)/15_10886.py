T = int(input())

li = []
for _ in range(T):
    num = int(input())
    li.append(num)

if li.count(1)>li.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")