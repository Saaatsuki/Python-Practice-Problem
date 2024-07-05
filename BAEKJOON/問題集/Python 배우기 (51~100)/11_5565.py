sum_num = int(input())

li = []
for _ in range(9):
    val = int(input())
    li.append(val)

print(sum_num - (sum(li)))

