count = int(input())

for _ in range(count):
    txt = input()
    li = []
    o_num = 0 
    for char in txt:
        if char == 'O':
            o_num += 1
            li.append(o_num)
        else:
            o_num = 0
            li.append(o_num)
    print(sum(li))