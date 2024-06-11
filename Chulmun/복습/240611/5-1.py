num_li = []
for i in ["첫","두","세"]:
    num = int(input(f"{i} 번째 수 입력 : "))
    num_li.append(num)
num_li_max = num_li[0]
for i in num_li:
    if num_li_max<=i:
        num_li_max = i
    if num_li.count(i)>1:
        w_num = i

if num_li[0]!=num_li[1]!=num_li[2]:
    msg = f"모든 수가 다릅니다.가장 큰 수는 {num_li_max}입니다."
elif len(set(num_li))==2:
    msg = f"두 수가 같습니다.({w_num}와{w_num})"
else:
    msg = "모든 수가 같습니다"
print(msg)