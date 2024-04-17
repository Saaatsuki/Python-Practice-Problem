grade, class_number, special_number = map(int, input("Please enter your student number : ").split())

msg = "Your student number is {}{}{}!!"

if class_number < 10:
    class_number = "0" + str(class_number)

if special_number < 10:
    special_number = "0" + str(special_number)

print(msg.format(grade, class_number, special_number))
