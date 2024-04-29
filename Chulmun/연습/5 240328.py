# Receive age and reservation code and reservationdate information from users
age = int(input("Please enter your age🐼："))
event_code = input("Please enter your reservation code🐰：")
reservation_date = int(input("Please enter a reservation date🐨："))

# Check the event code and age to determine the reservation result and print the appropriate message
if ((event_code == "E1") and (1 <= reservation_date <= 30)):
    if (age >= 18):
        print("Your reservation has been completed╰(*°▽°*)╯")
    else:
        print("I couldn't make a reservation for this event because your age is not enough(ToT)/~~~") 

elif ((event_code == "E2") and (1 <= reservation_date <= 30)):
    if (reservation_date %2==0):
        print("Your reservation has been completed╰(*°▽°*)╯") 
    else:
        print("Your reservation could not be made on the selected date(>_<)") 

elif ((event_code == "E3") and (1 <= reservation_date <= 30)):
    if ((age >= 16) and (reservation_date %7==0)):
        print("Your reservation has been completed╰(*°▽°*)╯")
    elif ((age < 16) and (reservation_date %7==0)):
        print("I couldn't make a reservation for this event because your age is not enough(ToT)/~~~") 
    elif ((age >= 16) and (reservation_date %7!=0)):
        print("Your reservation could not be made on the selected date(>_<)") 
    else:
        print("US>Exit the program as this is an invalid input( ﾉ ﾟｰﾟ)ﾉ")        
        
else:
    print("US>Exit the program as this is an invalid input( ﾉ ﾟｰﾟ)ﾉ")
          