# 1) 240606 복습
# for value in range(5):
#     print(value)

# 2) for / if / break
# for value in range(5):
#     input_value = int(input("입력 값"))
#     if input_value <= 0:
#         break
#     print(value)

# 3) for / if / break
# done_break = False
# for value in range(5):
#     input_value = int(input("입력 값"))
#     if input_value <= 0:
#         break
#     print(value)
# msg = "break 사용" if done_break else "break 미사용"
# print(msg)

# 4) break / continue
for i in range(1,3):
    for j in range(1,4):
        if i == 2:
            break
        print(f"{i}:{j}")

# 5) ***
for _ in range(4):
    for _ in range(3):
        print("*",end="")
    print()


# 6)
for i in range(3, 7):
    for j in range(1, 5, 2):
        print(i)
        if i == 5:
            continue
        for k in range(2):
            print(f"{i} {j} {k}")

    if (i + j + k) % 2 == 0:        
        print(i + j + k)
    