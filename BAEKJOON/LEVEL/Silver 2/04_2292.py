N = int(input())

if N == 1:
    print(1)
else:
    layer = 1
    cou = 1

    while N > cou:
        cou += 6 * layer
        layer += 1
    
    print(layer)
