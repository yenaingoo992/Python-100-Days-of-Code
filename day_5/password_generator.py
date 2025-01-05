import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Python password generator!")

pass_letters = int(input("How many letters would you like in your password?\n"))
pass_symbols = int(input("How many symbols would you like?\n"))
pass_numbers = int(input("How many numbers would you like?\n"))

# len() is used to find the size of the given list
letters_length = len(letters) - 1
numbers_length = len(numbers) - 1
symbols_length = len(symbols) - 1
password = ""

for index in range(0, pass_letters):
    password += letters[random.randint(0, letters_length)]

for index in range(0, pass_symbols):
    password += symbols[random.randint(0, symbols_length)]

for index in range(0, pass_numbers):
    password += numbers[random.randint(0, numbers_length)]

# random.sample can use to shuffle the given sequence
# and return a new list
shuffled_chars = random.sample(password, len(password))

# joining the list as a string
result = ''.join(shuffled_chars)

print(f"Your password: {result}")
