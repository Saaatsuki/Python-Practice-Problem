T = int(input())

for _ in range(T):
    num = int(input())
    num_bin = bin(num)[2:]  
    num_bin = num_bin[::-1]  

    result = []
    for i in range(len(num_bin)):
        if num_bin[i] == '1':
            result.append(str(i)) 

    print(" ".join(result)) 
