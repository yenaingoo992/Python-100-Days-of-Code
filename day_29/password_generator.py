import random
from random import shuffle

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
        pass_letters = [random.choice(letters) for _ in range(0, self.pass_letters)]
        pass_numbers = [random.choice(symbols) for _ in range(0, self.pass_symbols)]
        pass_symbols = [random.choice(numbers) for _ in range(0, self.pass_symbols)]

        password = pass_letters + pass_numbers + pass_symbols
        # random.sample can use to shuffle the given sequence
        # and return a new list
        shuffle(password)

        # joining the list as a string
        return "".join(password)
