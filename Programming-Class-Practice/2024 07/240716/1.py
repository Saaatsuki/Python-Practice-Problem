# Sorting -> 정렬 -> 
# 1) 오름차순 : 1, 2, 3, 4
# 2) 내림차순 : 4, 3, 2, 1

# 자료구조
# 1차원 자료구조 -> List

# 1 ~ 100사이 숫자 10개를 리스트에 저장하라.
import random

# Matrix
bar = [
        [
            [13, 8],[55, 85] # 13
        ],
        [
            [10, 20],[30, 40] # 10
        ] ,
        [
            [40, 50],[60, 70] # 40
        ] 
    ]   

def get_value(bar):
    return sum([ item for record in bar for item in record])
    # sum = 0
    # for record in bar:
    #     for item in record:
    #         sum += item
    # return sum


result = sorted(bar,  key = get_value , reverse=True) 

print(result) 

