def rank_elements(lst):
    """
    指定されたリスト内の各要素に対して順位をつける関数。
    
    パラメータ:
        lst (list): 数字を含むリスト。
    
    戻り値:
        list: 各要素の順位を示すリスト。
    """
    indexed_lst = list(enumerate(lst))
    sorted_lst = sorted(indexed_lst, key=lambda x: x[1], reverse=True)
    ranks = [0] * len(lst)
    current_rank = 1
    for i, (index, value) in enumerate(sorted_lst):
        if i > 0 and value == sorted_lst[i - 1][1]:
            ranks[index] = current_rank
        else:
            current_rank = i + 1
            ranks[index] = current_rank
    return ranks

menu = 0

student_file_name = []
student_file_kokugo = []
student_file_eng = []
student_file_math = []
test_sum_file = []
test_avg_file = []

while menu != 4:
    print("\n[메뉴 선택]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 화면 출력")
    print("3. 학생 성적 파일 출력")
    print("4. 종료")

    menu = int(input("메뉴를 선택하세요 : "))

    if menu == 1:
        name = input("학생 이름 : ")
        kokugo = int(input("국어 점수 : "))
        eng = int(input("영어 점수 : "))
        math = int(input("수학 점수 : "))
        student_file_name.append(name)
        student_file_kokugo.append(kokugo)
        student_file_eng.append(eng)
        student_file_math.append(math)
        test_sum = kokugo + eng + math
        test_avg = test_sum / 3
        test_sum_file.append(test_sum)
        test_avg_file.append(test_avg)

    elif menu == 2:
        ranks = rank_elements(test_sum_file)
        print("[학생 성적 목록]")
        print("{:<12} {:<5} {:<5} {:<5} {:<5} {:<7} {:<10}".format("이름", "국어", "영어", "수학", "총점", "평균", "등수"))
        for i in range(len(student_file_name)):
            print("{:<12} {:<5} {:<5} {:<5} {:<5} {:<7.2f} {:<10}".format(student_file_name[i], student_file_kokugo[i], student_file_eng[i], student_file_math[i], test_sum_file[i], test_avg_file[i], ranks[i]))

    elif menu == 3:
        ranks = rank_elements(test_sum_file)
        for i in range(len(student_file_name)):
            print("{:<12} {:<5} {:<5} {:<5} {:<5} {:<7.2f} {:<10}".format(student_file_name[i], student_file_kokugo[i], student_file_eng[i], student_file_math[i], test_sum_file[i], test_avg_file[i], ranks[i]))