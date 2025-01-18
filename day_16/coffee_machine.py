from coffee_maker import *
from menu import *
from money_machine import *

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
turn_off = False

while not turn_off:
    try:
        operation = int(input(f"Please choose the menu.\n1. Report status\n2. Espresso\n3. Latte\n4. Cappuccino\n5. Exit\n"))
        order = ""
        if operation == 1:
            coffee_maker.report()
            money_machine.report()
        elif operation == 2:
            order = "espresso"
        elif operation == 3:
            order = "latte"
        elif operation == 4:
            order = "cappuccino"
        elif operation == 5:
            turn_off = True
            print("Thanks")
        else:
            print("Please choose the correct operation.")

        if order != "":
            drink = menu.find_drink(order)
            is_drink_available = coffee_maker.is_resource_sufficient(drink)

            if is_drink_available:
                is_transaction_successful = money_machine.make_payment(drink.cost)
                if is_transaction_successful:
                    coffee_maker.make_coffee(drink)

    except ValueError:
        print("Please choose the correct operation.")
