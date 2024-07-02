coordinates = ["x", "y"]
values = []

for i in coordinates:
    value = int(input(f"{i} 좌표를 입력하세요. : "))
    values.append(value)

x = values[0]
y = values[1]

msg = "이 값의 사건은 {}입니다."

if x > 0 and y > 0:
    print(msg.format("1"))
elif x < 0 and y > 0:
    print(msg.format("2"))
elif x < 0 and y < 0:
    print(msg.format("3"))
elif x > 0 and y < 0:
    print(msg.format("4"))
else:
    print("0")
