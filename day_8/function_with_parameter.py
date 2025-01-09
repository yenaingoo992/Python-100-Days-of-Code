# functions that allow inputs

def greet(name):
    print(f"Hello {name}")

greet("Jack")
greet("Harry".lower())

# functions with more than one inputs
def greet(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet("Karina", "Nowhere")

# if we change arguments position, function will behave wrongly
greet("Nowhere", "Karina") # name and location positions are wrong

# to prevent, use positional argument
greet(location="Nowhere", name="Karina") # this will work correctly
