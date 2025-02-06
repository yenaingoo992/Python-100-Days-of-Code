import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


class PasswordManager:

    def __init__(self):
        self.pass_letters = random.randint(8, 10)
        self.pass_symbols = random.randint(2, 4)
        self.pass_numbers = random.randint(2, 4)

    def generate_password(self):
        password = ""
        letters_length = len(letters) - 1
        numbers_length = len(numbers) - 1
        symbols_length = len(symbols) - 1

        for index in range(0, self.pass_letters):
            password += letters[random.randint(0, letters_length)]

        for index in range(0, self.pass_symbols):
            password += symbols[random.randint(0, symbols_length)]

        for index in range(0, self.pass_numbers):
            password += numbers[random.randint(0, numbers_length)]

        # random.sample can use to shuffle the given sequence
        # and return a new list
        shuffled_chars = random.sample(password, len(password))

        # joining the list as a string
        return "".join(shuffled_chars)
