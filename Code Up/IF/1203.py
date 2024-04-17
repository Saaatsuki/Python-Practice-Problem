def shape_measurement (bmi):

    msg = "Your body is {}" 
  
    if (bmi <= 10):
        print(msg.format("normal"))
    elif (10 < bmi <= 20):
        print(msg.format("obesity"))
    elif (20 <= bmi):
        print(msg.format("hyper obesity"))

bmi = int(input("Please enter your BMI : "))
shape_measurement(bmi)