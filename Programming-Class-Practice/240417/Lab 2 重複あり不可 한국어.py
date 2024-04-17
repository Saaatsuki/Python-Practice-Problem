import random

def numbers_without_duplicates(number):
    random_numbers = [] 
    count = 0

    while count < number:
        random_number = random.randint(1,100)
        
        duplicate = False
        for num in random_numbers:
            if num == random_number:
                duplicate = True
                break
        
        if not duplicate:
            random_numbers.append(random_number)
            count += 1
    return random_numbers
        
# ① 사용자는 먼저 생성할 랜덤 정수의 개수 N을 입력합니다. 
number = int(input("N값을 입력해 주세요 (1-100) : "))
        

if (0 < number <= 100):
    random_numbers = numbers_without_duplicates(number)
    print("생성된 리스트 : ", random_numbers)
            
    while True:
        # ④ 사용자에게 리스트에서 원하는 원소의 인덱스를 입력받습니다
        index_number = int(input("원하는 원소의 인덱스를 입력해 주세요 (0-" + str(number-1) + ") : "))
                
        # ⑤ 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력합니다.
        if (0 <= index_number < number):
            print("선택한 인덱스의 원소 : ",random_numbers[index_number])
            break
        else:
            print("에러:유효한 인덱스를 범위를 벗어났습니다.")
            continue
else:
    print("N은 1이상 100이하의 정수여야 합니다.")
