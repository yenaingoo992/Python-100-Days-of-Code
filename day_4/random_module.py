import random

# random int -> (a <= number <= b)
random_number = random.randint(1, 10) # generate between 1 and 10
print(random_number)

# random float -> (a <= number < b)
random_number = random.random() # generate between 0 and 1.0(not included)
print(random_number)

# random float -> (a <= number <= b)
random_number = random.uniform(1, 3) # generate between 1.0 and 10.0
print(random_number)

# Head and Tail
coin = random.randint(1,10)
if coin % 2 == 0:
    print("Head")
else:
    print("Tail")
