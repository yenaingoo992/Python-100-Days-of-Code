from random import randint

# the following function is producing bug at random point
# figure it out the issue and fix
def roll_the_dice():
    dice_numbers = [1, 2, 3, 4, 5, 6]
    dice_num = randint(1, 6)
    print(dice_numbers[dice_num])

# roll_the_dice()

# fixed
def roll():
    dice_numbers = [1, 2, 3, 4, 5, 6]
    # randint start and end is included
    # list start from index 0, so need to fix randint start and end
    # dice_num = randint(1, 6)
    dice_num = randint(0, 5)
    print(dice_numbers[dice_num])

roll()