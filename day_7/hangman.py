import random
import hang_man_ascii_art

word_list = ["apple", "watermelon", "peaches", "carrot", "coconut"]
life = 7
result = list()
hangmanpics_len = len(hang_man_ascii_art.HANGMANPICS)

def show_hangman():
    index = hangmanpics_len - life 
    print(hang_man_ascii_art.HANGMANPICS[index])

# show how many life remains
def show_life():
    print(f"**************************************LIVES LEFT: {life}/{hangmanpics_len} **************************************")

# show the result
def show_result():
    result_str = ""
    for word in result:
        result_str += word
    print(f"Word to guess: {result_str}")

print(hang_man_ascii_art.WELCOME_MESSAGE)

random.shuffle(word_list)
word_to_guess = list(word_list[random.randint(0, len(word_list) - 1)])

# generate blanks for word_to_guess
for letter in word_to_guess:
    result.append("_")

while life > 0 and result.count("_") > 0:
    show_hangman()
    show_result()
    show_life()
    user_guess = input("Guess a letter: ").lower()

    index = 0
    can_guess_a_word = False
    
    while index < len(word_to_guess):
        
        # if user's guess word contains in the letter
        if word_to_guess[index] == user_guess:
            # put the letter to the result to the same index
            result[index] = word_to_guess[index]
            # remove the correct word, incaseof duplicate check 
            word_to_guess[index] = "_"
            
            can_guess_a_word = True
            user_guess = ""
    
        index += 1

    # reduce a life if user's guess is wrong
    if can_guess_a_word:
        can_guess_a_word = False
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        life -= 1

# if there is no life remain, game over
if life < 1:
    print("Game Over! You lost all of your lives. You Die 😂😂😂")
else:
    print("Congratulations 🎉🎉🎉. You win!!!")