msg_li = ["첫","두","세"]
while True:
    num_li = []
    for i in range(3):
        num = int(input(f"{msg_li[i]} 번째 변의 길이를 입력하세요 : "))
        num_li.append(num)
    if num_li[0]+num_li[1]<num_li[2] or num_li[0]+num_li[2]<num_li[1] or num_li[1]+num_li[2]<num_li[0]:
        print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.\n삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")
    else:
        break

if num_li[0]!=num_li[1]!=num_li[2]:
    tri_msg = "부등변"
elif len(set(num_li))==2:
    tri_msg = "이등변"
else: #num_li[0]==num_li[2]:
    tri_msg = "정"

print(f"입력하신 변의 길이는 {tri_msg}삼각형을 만들 수 있습니다.")