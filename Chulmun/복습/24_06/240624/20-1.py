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

def get_in(arg_big, arg_small):
    for val in arg_big:
        if val == arg_small:
            return True
    return False

def random_sample(arg_sequence, arg_k):
    if len(arg_sequence) < arg_k:
        raise ValueError("リストの長さがサンプル数よりも少ないです")
    
    arg_sequence_copy = arg_sequence.copy()
    sample = []
    for _ in range(arg_k):
        index = random.randint(0, len(arg_sequence_copy) - 1)
        sample.append(arg_sequence_copy.pop(index))
    return sample
    
while True:
    print("-" * 20)
    print("1）九九の段")
    print("2）数字ピラミット")
    print("3）終了")
    print("-" * 20)

    menu = int(input("メニュー番号を選択してください："))

    if menu == 1:
        while True:
            gugu_input = input("出力したい九九の段を入力してください（例: 2, 3~5）：")
            if "~" in gugu_input:
                start, end = map(int, get_split(gugu_input, "~"))
                gugu_li = list(range(start, end + 1))
            else:
                gugu_li = list(map(int, get_split(gugu_input, ",")))

            if all(2 <= num <= 9 for num in gugu_li):
                for num1 in gugu_li:
                    print(f"{num1}の段:")
                    for num2 in range(1, 10):
                        print(f"{num1} × {num2} = {num1 * num2}")
                    print()
                break
            else:
                print("2～9の数字を入力してください。")

    elif menu == 2:
        high = int(input("何段の数字ピラミットにしますか？ (2または3を入力してください): "))
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
            print("2または3の数字を入力してください。")
    
    elif menu == 3:
        print("プロジェクトを終了します。")
        break

    else:
        print("1～3のメニュー番号を選んでください。")
