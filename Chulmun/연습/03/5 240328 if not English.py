# Receive age and reservation code and reservation date information from users
age = int(input("Please enter your age🐼："))
event_code = input("Please enter your reservation code🐰：")
reservation_date = int(input("Please enter a reservation date🐨："))

# Define the dictionary containing event information
events = {
    "E1": {"age_limit": 18, "date_restrictions": None},
    "E2": {"age_limit": None, "date_restrictions": "even"},
    "E3": {"age_limit": 16, "date_restrictions": "multiple_of_7"}
}

# Check if the event code is valid
if event_code not in events:
    print("Invalid event code. Exiting the program.")
    exit()

# Check if the reservation date is valid
if not (1 <= reservation_date <= 30):
    print("Invalid reservation date. Exiting the program.")
    exit()

# Check if the age meets the age limit for the event
if events[event_code]["age_limit"] is not None and age < events[event_code]["age_limit"]:
    print("Age restriction: You cannot make a reservation for this event.")
elif events[event_code]["date_restrictions"] == "even" and reservation_date % 2 != 0:
    print("Date restriction: Your reservation could not be made on the selected date.")
elif events[event_code]["date_restrictions"] == "multiple_of_7" and reservation_date % 7 != 0:
    print("Date restriction: Your reservation could not be made on the selected date.")
else:
    print("Your reservation has been completed╰(*°▽°*)╯")

          