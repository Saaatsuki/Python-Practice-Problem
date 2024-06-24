def getSplit(argTxt,argSplit):
    word_li = []
    word = ""

    for char in argTxt:
        if char != argSplit:
            word += char
        else:
            if word:
                word_li.append(word)
                word = ""
    if word:
        word_li.append(word)
    return word_li

def strChangeInt(argList):
    return [int(val) for val in argList]


txt = input("数字を入力するちゃむ💛：")
int_li = strChangeInt(getSplit(txt,","))

output_number = []
num_sum = 0
for i in int_li:
    if num_sum > 100:
        break
    num_sum += i
    output_number.append(i)

input_num_list_sum_all = 0
[input_num_list_sum_all:= input_num_list_sum_all + i for i in int_li]
if num_sum >= 100:
    print(f"총합된 100를 초과하였습니다.\n현재까지의 입력값들 : {output_number}\n현재까지의 총합 : {num_sum}")
else:
    print(f"총합된 100를 초과하지 않았습니다.\n입력된 모든 숫자들 : {int_li}\n최종 총합 : {input_num_list_sum_all}")