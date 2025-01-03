title = r"""
**********************************************************************
 _____                                    ___     _                 _ 
|_   _| __ ___  __ _ ___ _   _ _ __ ___  |_ _|___| | __ _ _ __   __| |
  | || '__/ _ \/ _` / __| | | | '__/ _ \  | |/ __| |/ _` | '_ \ / _` |
  | || | |  __/ (_| \__ \ |_| | | |  __/  | |\__ \ | (_| | | | | (_| |
  |_||_|  \___|\__,_|___/\__,_|_|  \___| |___|___/_|\__,_|_| |_|\__,_|
**********************************************************************
"""

print(title)
print("Your mission is to find the treasure.")
win = False

direction = input('Your\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()
if direction == "left":
    action = input('You\'ve come to a lake.'
                   'There\'s an island in the middle of the lake.' 
                   '\nType "swim" to swim across '
                   'or "wait" to wait for a boat!\n').lower()
    if action == "wait":
        choice = input('Which door? "red" or "blue" or "yellow"\n').lower()
        if choice == "yellow":
            win = True
        elif choice == "blue":
            print("It's a room full of fire. 🔥🔥🔥")
        elif choice == "red":
            print("You've swallowed by a giant snake. 🐍")
    else:
        print("You got attacked by angry corcodile! 🐊")
else:
    print("You Fell into a Hole. 🕳️")

if win == True:
    print("You found the treasure. You Win!")
else:
    print("Game Over!")