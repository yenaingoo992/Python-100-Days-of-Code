# printing welcome message
print("Welcome to Tip Calculator!!")

# getting total bill
total_bill = float(input("What was the total bill?\n$"))

# getting how much percentage want to give
tip_as_percent = int(input("How much percentage tip would you like to give? 10, 12 or 15?\n"))

# calculate tip based on total bill and percentage
total_tip_amount = total_bill * (tip_as_percent / 100)

# getting people count
total_people = int(input("How many people to split the bill?\n"))

# calculate the result
bill_for_each_person = round((total_bill + total_tip_amount) / total_people, 2)
print(f"Each person should pay: ${bill_for_each_person}")