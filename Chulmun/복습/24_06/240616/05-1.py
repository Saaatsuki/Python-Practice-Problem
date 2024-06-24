num_li = []
for i in ["첫","두","세"]:
    num = int(input(f"{i} 번째 수 입력 : "))
    num_li.append(num)
max_num = num_li[0]
for i in num_li:
    if max_num<i:
        max_num=i
for i in num_li:
    if len([j for j in num_li if j==i])==2:
        two_num = i
if num_li[0] != num_li[1] != num_li[2]:
    print(f"모든 수가 다릅니다 . 가장 큰 수는 {max_num}입니다.")
elif len(set(num_li))==2:
    print(f"두 수가 같습니다. ({two_num}와{two_num})")
else:
    print(f"모든 수가 같습니다.")