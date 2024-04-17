# receive an integer from a user
number = int(input("How many points did you get??："))

msg = ("Your score is {}!!")


# Evaluate the results based on the number entered and print a message
if (90 <= number <= 100):
    print(msg.format("A"))
elif (70 <= number <= 89):
     print(msg.format("B"))
elif (40 <= number <= 69):
    print(msg.format("C"))
elif (0 <= number <= 39):
    print(msg.format("D"))
else:# Outputs an error message if the value entered is outside the acceptable range
    print("Error")