li = []
for _ in range(10):
    num = int(input())
    li.append(num)

avg = sum(li) / 10

cou_li = []
for i in li:
    cou = li.count(i)
    cou_li.append(cou)

idx = cou_li.index(max(cou_li))
print(int(avg))
print(li[idx])