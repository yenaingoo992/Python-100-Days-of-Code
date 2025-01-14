# Value error can happen when we expect to get int from user
# but user input other values and int() can not change into error

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical number such as 15.")
    age = int(input("Enter your age: "))

if age > 18:
    print(f"You can drive at age {age}.")
    