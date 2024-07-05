con = int(input())

li = list(map(int,input().split()))
li_max = max(li)

li2 = [(num / li_max) * 100 for num in li]
print(sum(li2) / len(li2))