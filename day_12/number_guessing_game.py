import random

art = """
,---.                    ,--,--'.         ,-,-.             .           
|  -'  . . ,-. ,-. ,-.   `- |   |-. ,-.   ` | |   . . ,-,-. |-. ,-. ,-. 
|  ,-' | | |-' `-. `-.    , |   | | |-'     | |-. | | | | | | | |-' |   
`---|  `-' `-' `-' `-'    `-'   ' ' `-'    ,' `-' `-' ' ' ' `-' `-' '   
 ,-.|                                                                   
 `-+'  
"""

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_the_number(choice_number, correct_number):
    if choice_number < correct_number:
        return -1
    elif choice_number > correct_number:
        return 1
    else:
        return 0

def set_difficulity():
    level = input("Choose a difficulity. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def game():
    print(art)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    lucky_number = random.randint(1, 100)
    attempts = set_difficulity()
        
    is_game_over = False
    while not is_game_over:
        if attempts <= 0:
            is_game_over = True
            print("You've run out of guesses, you lose.")
        else: 
            print(f"You have {attempts} attempts remaining to guess the number.")
            choice = int(input("Make a guess: "))
                
            result = check_the_number(choice, lucky_number)
                
            if result == 0:
                is_game_over = True
                print(f"You got it! The answer was {lucky_number}")
            elif result == -1:
                attempts -= 1
                print("Too Low.")
            elif result == 1:
                attempts -= 1
                print("Too High.")
                    
            print("Guess Again!")

game()