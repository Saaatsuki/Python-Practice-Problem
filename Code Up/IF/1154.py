# Receive two integers from a user
num1,num2 = map(int,input("Please input two integers: ").split())

# Calculate the difference between the two numbers and print it
# Print the difference if num1 is greater than num2
# Otherwise, print the difference if num2 is greater than or equal to num1
print(abs(num1 - num2))