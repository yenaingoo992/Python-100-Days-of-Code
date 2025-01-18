from data_source import coffee_types, coins

ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
WATER = "water"
COFFEE = "coffee"
MILK = "milk"
PRICE = "price"

QUARTERS = "quarters"
DIMES = "dimes"
NIKLES = "nikles"
PENNIES = "pennies"
    
def prettyPrint(water, milk, coffee, money):
    print("************ Status ************")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")
    
def reduce(total, current):
    return total - current


def has_sufficient_resources(coffee, water_resource, milk_resource, coffee_resource):
    if coffee[WATER] > water_resource:
        print("Sorry there is not enough water.")
        return False
    elif coffee[MILK] > milk_resource:
        print("Sorry there is not enough milk.")
        return False
    elif coffee[COFFEE] > coffee_resource:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True

def request_payment():
    quarters = int(input(f"How many quarters(${coins[QUARTERS]})?: "))
    dimes = int(input(f"How many dimes(${coins[DIMES]})?: "))
    nikles = int(input(f"How many nikles(${coins[NIKLES]})?: "))
    pennies = int(input(f"How many pennis(${coins[PENNIES]})?: "))

    return (
        (coins[QUARTERS] * quarters)
        + (coins[DIMES] * dimes)
        + (coins[NIKLES] * nikles)
        + (coins[PENNIES] * pennies)
    )

def start_machine():
    exit_the_machine = False
    total_water_amount = 500
    total_milk_amount = 300
    total_coffee_amount = 150
    total_money = 0
    while not exit_the_machine:
        try:
            operation = int(
                input(
                    f"Please choose the menu.\n1. Report status\n2. Espresso (${coffee_types[ESPRESSO][PRICE]})\n3. Latte (${coffee_types[LATTE][PRICE]})\n4. Cappuccino (${coffee_types[CAPPUCCINO][PRICE]})\n5. Exit\n"
                )
            )
            type = ""
            if operation == 1:
                prettyPrint(
                    total_water_amount, total_milk_amount, total_coffee_amount, total_money
                )
            elif operation == 2:
                type = ESPRESSO
            elif operation == 3:
                type = LATTE
            elif operation == 4:
                type = CAPPUCCINO
            else:
                exit_the_machine = True

            if not exit_the_machine and operation != 1:
                coffee = coffee_types[type]
                is_sufficient = has_sufficient_resources(
                    coffee=coffee,
                    water_resource=total_water_amount,
                    milk_resource=total_milk_amount,
                    coffee_resource=total_coffee_amount,
                )
                if is_sufficient:
                    inserted_amount = request_payment()
                    if inserted_amount >= coffee[PRICE]:
                        change = round(inserted_amount - coffee[PRICE], 2)
                        if change > 0:
                            print(f"Here is ${change} in change.")
                        total_water_amount = reduce(total_water_amount, coffee[WATER])
                        total_milk_amount = reduce(total_milk_amount, coffee[MILK])
                        total_coffee_amount = reduce(total_coffee_amount, coffee[COFFEE])
                        print(f"Here is your {type}, Enjoy it!")
                    else:
                        print("Sorry that's not enough money. Money refunded")
        except ValueError:
            print("Invalid! Please choose the correct operation.")
        print("********************************")

start_machine()