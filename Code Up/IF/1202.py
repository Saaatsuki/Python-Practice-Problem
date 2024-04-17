def assessment (test):
    
    msg = "Your assessment is {} !!!"
    
    if (test >= 90):
        print(msg.format("A"))
    elif (test >= 80):
        print(msg.format("B"))
    elif (test >= 70):
        print(msg.format("C"))
    elif (test >= 60):
        print(msg.format("D"))
    elif (test < 60):
        print(msg.format("F"))

test = int(input("Please enter your score : "))

assessment(test)