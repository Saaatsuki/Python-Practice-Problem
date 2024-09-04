while True:
    num = input()
    if num == "0":
        break
    else:
        num_li = list(num)

        num_li_1 = num_li[::-1]

        if num_li == num_li_1:
            print("yes")
        else:
            print("no") 