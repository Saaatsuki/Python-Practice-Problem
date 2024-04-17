# Receive a integer from a user
number = int(input("Please enter an integer of your choice: "))



# Check if the number is a multiple of 7
# Print "multiple" if the number is divisible by 7
# Otherwise, print "not multiple"
if(number % 7 == 0):
    print("multiple")
else:
    print("not multiple")