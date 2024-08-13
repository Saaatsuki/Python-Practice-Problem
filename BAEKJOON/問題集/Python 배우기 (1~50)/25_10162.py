def microwave_buttons(T):
    A = 300  # 5分
    B = 60   # 1分
    C = 10   # 10秒

    a_count = T // A
    T %= A

    b_count = T // B
    T %= B

    c_count = T // C
    T %= C

    if T != 0:
        return -1
    else:
        return a_count, b_count, c_count

T = int(input())
result = microwave_buttons(T)

if result == -1:
    print(-1)
else:
    print(result[0], result[1], result[2])
