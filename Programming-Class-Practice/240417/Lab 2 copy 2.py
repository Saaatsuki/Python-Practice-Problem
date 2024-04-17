import random

while True:
    # 사용자はまず生成するランダム整数の個数Nを入力します。
    number = int(input("N의 값을 입력하세요 (1-100): "))
    
    if 0 < number <= 100:
        random_numbers = []
        count = 0
        
        while count < number:
            random_number = random.randint(1, 100)
            
            # 生成されたランダムな数字が既存のリストに含まれているかどうかを確認します。
            duplicate = False
            for num in random_numbers:
                if num == random_number:
                    duplicate = True
                    break
            
            # 重複がない場合にのみリストに要素を追加します。
            if not duplicate:
                random_numbers.append(random_number)
                count += 1
        
        print("生成されたリスト: ", random_numbers)
        
        while True:
            # 사용자에게 리스트から 원하는 원소의 인덱스를 입력받습니다.
            index_number = int(input("원하는 원소의 인덱스를 입력하세요 (0-" + str(number-1) + "): "))
            
            # 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력합니다.
            if 0 <= index_number < number:
                print("선택한 인덱스의 원소: ", random_numbers[index_number])
                break
            else:
                print("에러: 유효한 인덱스 범위를 벗어났습니다.")
                continue
        break
    else:
        print("N은 1이상 100이하의 정수여야 합니다.")
