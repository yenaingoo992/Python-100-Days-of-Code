import random
from hang_man_ascii_art import *
from words import fruits

life = 6
result = list()
hangmanpics_len = len(HANGMANPICS)

def show_hangman():
    index = hangmanpics_len - (life + 1)
    print(HANGMANPICS[index])

# show how many life remains
def show_life():
    print(f"**************************************LIVES LEFT: {life}/{hangmanpics_len - 1} **************************************")

# show the result
def show_result():
    result_str = ""
    for word in result:
        result_str += word
    print(f"Word to guess: {result_str}")

print(WELCOME_MESSAGE)

random.shuffle(fruits)
chosen_word = list(random.choice(fruits))

# generate blanks for word_to_guess
for letter in chosen_word:
    result.append("_")

while life >= 1 and result.count("_") > 0:
    show_hangman()
    show_result()
    show_life()
    user_guess = input("Guess a letter: ").lower()

    index = 0
    can_guess_a_word = False
    
    while index < len(chosen_word):
        
        # if user's guess word contains in the letter
        if chosen_word[index] == user_guess:
            # put the letter to the result to the same index
            result[index] = chosen_word[index]
            # remove the correct word, incaseof duplicate check 
            chosen_word[index] = "_"
            
            can_guess_a_word = True
            user_guess = ""
    
        index += 1

    # reduce a life if user's guess is wrong
    if can_guess_a_word:
        can_guess_a_word = False
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        life -= 1

show_hangman()

# if there is no life remain, game over
if life > 1:
    print("Congratulations 🎉🎉🎉. You win!!!")
else:
    print("Game Over! You lost all of your lives. You Die 😂😂😂")