## Subscripting
print("Hello"[-5])

## Check the data type
print(type("Hello"))
print(type(123_456))
print(type(3.1419))
print(type(True))

## Type conversions
# to string
print(str(123))

# to int
print(int("456"))

# to float
print(float(20))

# to boolean
print(bool(1))

## Math operations
print(1 + 2) # 3
print(5 - 6) # -1
print(8 / 2) # 4
print(9 / 4) # 2.25
print(9 // 4) # 2
print(2 ** 3) # 8

# PEMDAS -> () > ** > * or / > + or -
print(3 * 3 + 3 / 3 - 3) # 7

## f-String
age = 20
height = 45.9

print(f"Age is {age} and Height is {height}")