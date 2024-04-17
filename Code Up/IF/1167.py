numbers =list(map(int,input("Please enter three integers☆：").split()))

numbers.sort()

msg = "The second largest number is {}!!"

print(msg.format(numbers[1]))