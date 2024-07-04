for _ in range(3):
    li = list(map(int,input().split()))

    if li.count(0) == 0:
        print("E")
    elif li.count(0) == 1:
        print("A")
    elif li.count(0) == 2:
        print("B")
    elif li.count(0) == 3:
        print("C")
    elif li.count(0) == 4:
        print("D")
