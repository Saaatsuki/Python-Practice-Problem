T = int(input())

li = []
for _ in range(T):
    num = int(input())
    li.append(num)

li.sort()


print("\n".join(map(str,li)))