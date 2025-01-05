# for loop
fruits = ["Apple", "Banana", "Coconut"]

for fruit in fruits:
    print(fruit)

# finding max number in the loop
scores = [150, 142, 185, 120, 171, 184, 201, 24, 59, 68, 199]
max = 0

for score in scores:
    if max < score:
        max = score

print(f"Max number: {max}")

# range
# range(1, 10) 1 is inclusive but 10 is exclusive and 2 is step
for num in range(1, 10, 2):
    print(num) # 2, 4, 6, 8 will print due to step is 2

# adding 1 to 10 using range
sum = 0
for num in range(1, 101):
    sum += num

print(sum)
