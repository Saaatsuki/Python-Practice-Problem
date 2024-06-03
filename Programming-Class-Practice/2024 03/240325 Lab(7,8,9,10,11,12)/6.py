age = int(input("いくつなん？："))

msg = "You are in the '{}' age group."

if (13 <= age <= 19):
    print(msg.format("Teenager")) 
elif (20 <= age <= 64):
    print(msg.format("Adult"))
elif (65 <= age):
    print(msg.format("Senior"))
else:
    print(msg.format("Unknowm age group"))