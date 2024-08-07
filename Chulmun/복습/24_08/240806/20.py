import random

def get_split(arg_txt, arg_sep):
    word_li = []
    word = ""
    for char in arg_txt:
        if char != arg_sep:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)
    return word_li

def get_join(arg_list, arg_sep):
    result = ""
    for i in range(len(arg_list)):
        result += str(arg_list[i])
        if i < len(arg_list) - 1:
            result += arg_sep
    return result

def random_sample(arg_sequence, arg_k):
    if len(arg_sequence) < arg_k:
        raise ValueError("리스트의 길이가 샘플 수보다 적습니다.")
    
    arg_sequence_copy = arg_sequence.copy()
    sample = []
    for _ in range(arg_k):
        index = random.randint(0, len(arg_sequence_copy) - 1)
        sample.append(arg_sequence_copy.pop(index))
    return sample

while True:
    print("-" * 30)
    print("1) 구구단 출력")
    print("2) 랜덤값 삼각형 출력")
    print("3) 종료")
    print("-" * 30)

    menu = int(input("원하는 메뉴 번호를 입력하세요 : "))
    while not 1 <= menu <= 3:
        menu = int(input("1~3 사이의 값을 입력하세요 : "))

    if menu == 1:
        while True:
            gugu_input = input("출력할 구구단을 입력하세요 (예: 2, 3~5) : ")
            if "~" in gugu_input:
                start, end = map(int, get_split(gugu_input, "~"))
                gugu_li = list(range(start, end + 1))
            else:
                gugu_li = list(map(int, get_split(gugu_input, ",")))

            if all(2 <= num <= 9 for num in gugu_li):
                for num1 in gugu_li:
                    print(f"구구{num1}단:")
                    for num2 in range(1, 10):
                        print(f"{num1} X {num2} = {(num1 * num2):2d}")
                    print()
                break
            else:
                print("2~9의 숫자를 입력하세요.")
    
    elif menu == 2:
        high = int(input("몇 단의 숫자 피라미드로 출력할까요? (2 또는 3을 입력하세요): "))
        if high == 2 or high == 3:
            num_k = high * (high + 1) // 2
            li1 = random_sample(list(range(1, 10)), num_k)
            index = 0
            for i in range(1, high + 1):
                li2 = li1[index:index + i]
                li3 = get_join(li2, "")
                print(f"{' ' * (high - i)}{li3}")
                index += i
        else:
            print("2 또는 3의 숫자를 입력하세요.")
    
    elif menu == 3:
        print("프로그램을 종료합니다.")
        break
