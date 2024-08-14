T = int(input())

for _ in range(T):
    num , name = input().split()
    name_li = list(name)
    name_li.pop((int(num))-1)
    print("".join(name_li))