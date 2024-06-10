import random

def get_sum():
    sum = 0
    for i in range(3):
        input_value = int(input(f"{i+1} 번째 입력 값 : "))
        sum+=input_value
    print(sum)
random.randint(1,3)
get_sum()