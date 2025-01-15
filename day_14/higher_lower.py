import random
from game_data import data
from art import *

NAME = "name"
SEARCH_COUNT = "search_count"
DESCRIPTION = "description"
COUNTRY = "country"

def compare(a, b):
    print(f"Compare A: {a[NAME]}, a {a[DESCRIPTION]}, from {a[COUNTRY]}")
    print(vs)
    print(f"Compare B: {b[NAME]}, a {b[DESCRIPTION]}, from {b[COUNTRY]}")
    choice = input("What gets Googled more? Type 'A' or 'B': ").lower()
    if choice == "a":
        if a[SEARCH_COUNT] >= b[SEARCH_COUNT]:
            return 1
        else:
            return 0
    elif choice == "b":
        if b[SEARCH_COUNT] <= b[SEARCH_COUNT]:
            return 1
        else:
            return 0
    else:
        return 0

def start_game():
    score = 0
    is_game_over = False
    random.shuffle(data)

    first = 0
    second = 1

    while not is_game_over:
        print(logo)
        if score != 0:
            print(f"Your right! Current score: {score}")
        
        result = compare(data[first], data[second])
        
        if result == 0:
            is_game_over = True
            print("Sorry. That's wrong.")
        else:
            score += result
            first = second
            second += 1
            if second >= len(data):
                is_game_over = True
                print("Congratulations!!! You've answered all the choices correctly.")
            else:
                print("\033c", end="")
    
    print(f"Final Score: {score}")

start_game()