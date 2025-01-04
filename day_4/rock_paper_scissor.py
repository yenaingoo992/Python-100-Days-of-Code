import random

rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissor]

choice = int(input("What is your choice? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n"))

if choice < 0 or choice > 2:
    print("Please Type only 0 or 1 or 2. Game Over!!!")
    quit()
else:
    print(f"You choose:\n{game[choice]}")
    
computer_choice = random.randint(0, 2)
print(f"Computer choose:\n{game[computer_choice]}")

if choice == computer_choice:
    print("That\'s a Draw!")
    
else:
    if choice == 0: # rock
        if computer_choice == 1: # paper
            print("You Lose!")
        else: # scissor
            print("You Win!")
            
    elif choice == 1: # paper
        if computer_choice == 2: # scissor
            print("You Lose!")
        else: # rock
            print("You Win")
    
    elif choice == 2: # scissor
        if computer_choice == 0: #rock
            print("You Lose!")
        else: # paper
            print("You Win!")