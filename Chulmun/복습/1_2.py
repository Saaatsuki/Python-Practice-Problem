numbers = ["첫","두","세"]
tri_list = []

for i in range(3):
    num = int(input(f"{numbers[i]}번째 변의 길이 입력하세요 : "))
    tri_list.append(num)
while tri_list[0]+tri_list[1]<=tri_list[2] or tri_list[1]+tri_list[2]<=tri_list[0]:
    print("입력하신 변이 길이로는 삼각형을 만들 수 없습니다.\n삼각형을 만들기 위해서는 두 변의 길이의 합이 다른 한 변의 길이보다 커야합니다.\n다시 입력 하세요.")
    for j in range(3):
        num = int(input(f"{numbers[j]}번째 변의 길이 입력하세요 : "))
        tri_list.append(num)

output_msg = "입력하신 변이 길이로는 {}삼각형을 만들 수 있습니다."

if tri_list[0] == tri_list[1] == tri_list[2]:
    msg = "정"
elif len(set(tri_list)) == 2:
    # tri_list[0] == tri_list[1] or tri_list[0] == tri_list[2] or tri_list[1] == tri_list[2]
    msg = "이등변"
elif tri_list[0] != tri_list[1] != tri_list[2]:
    msg = "부등변"
print(output_msg.format(msg))