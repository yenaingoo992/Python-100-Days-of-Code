print("Welcome to Pizza Delivery Python Program!")

size = input("What size pizza do you want? S, M or L: ")

bill = 0
if size == "s" or size == "S":
    bill += 15
elif size == "m" or size == "M":
    bill += 20
elif size == "l" or size == "L":
    bill += 25
else:
    print("Thank you!")
    quit()

pepperoni = input("Do you want to put pepperoni on your pizza? Y or N: ")
if pepperoni == "y" or pepperoni == "Y":
    if size == "s" or size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 1

print(f"Total bill: ${bill}")
