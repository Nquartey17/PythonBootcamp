from Tools.scripts.fixdiv import report

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()



while machine_on:
    items = menu.get_items()
    drink = input(f"Select your drink ({items}) ")

    if drink == "off":
        machine_on = False

    elif drink == "report":
        print(coffee_machine.report())

    else:
        drink = menu.find_drink(drink)

        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)