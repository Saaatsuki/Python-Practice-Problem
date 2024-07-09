def sort_list_max_remove(lst):
    sorted_list = []
    while lst:
        max_elem = max(lst)
        sorted_list.append(max_elem)
        lst.remove(max_elem)
    return sorted_list

menu = 0

student_file_name = []
student_file_kokugo = []
student_file_eng = []
student_file_math = []
test_sum_file = []
test_avg_file = []

output_li = ["이름", "국어", "영어", "수학", "총점", "평균", "등수"]

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
        sorted_indices = sorted(range(len(test_sum_file)), key=lambda k: test_sum_file[k], reverse=True)
        print("[학생 성적 목록]")
        print("  ".join(output_li))
        rank = 1
        for i in sorted_indices:
            print(f"{student_file_name[i]}  {student_file_kokugo[i]}  {student_file_eng[i]}  {student_file_math[i]}  {test_sum_file[i]}  {(test_avg_file[i]):.2f}  {rank}")
            rank += 1

    elif menu == 3:
        sorted_indices = sorted(range(len(test_sum_file)), key=lambda k: test_sum_file[k], reverse=True)
        print("[학생 성적 파일 출력]")
        rank = 1
        for i in sorted_indices:
            print(f"{student_file_name[i]}  {student_file_kokugo[i]}  {student_file_eng[i]}  {student_file_math[i]}  {test_sum_file[i]}  {(test_avg_file[i]):.2f}  {rank}")
            rank += 1

print("프로그램 종료")
