import art

def add(n1, n2):
    """receive 2 numbers as input, then return the added result"""
    return n1 + n2

def substract(n1, n2):
    """receive 2 numbers as input, then return the substracted result"""
    return n1 - n2

def multiply(n1, n2):
    """receive 2 numbers as input, then return the multiplied result"""
    return n1 * n2

def divide(n1, n2):
    """receive 2 numbers as input, then return the divided result"""
    return n1 / n2

operation_dictionary = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

print(art.calculator)

def calculator():
    result = 0.0
    n1 = float(input("What's the first number: "))
    should_accumulate = True
    while should_accumulate:
        operation = input("Pick an operation (+, -, *, /): ")
        n2 = float(input("What's the next number: "))
        result = operation_dictionary[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        should_carry_the_result = input(f"Type 'y' to continuing calculation with {result} or type 'n' to start a new operation: ").lower()
        if should_carry_the_result == 'n':
            should_accumulate = False
            print("\033c", end='')
            calculator()
        else:
            n1 = result

calculator()