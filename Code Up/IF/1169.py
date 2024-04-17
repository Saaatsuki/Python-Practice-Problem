grade, class_number, name_number = map(int, input("Please enter your student number : ").split())


if name_number < 10:
    student_number = str(grade) + str(class_number) + '0' + str(name_number)
else:
    student_number = str(grade) + str(class_number) + str(name_number)

print(student_number)