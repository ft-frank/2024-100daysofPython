from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    decision = input(f"What would you like to do?({menu.get_items()})").lower()
    if decision == "latte" or decision == "cappuccino" or decision == "espresso":
        drink = menu.find_drink(decision)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            enough_money = money_machine.make_payment(drink.cost)
            if enough_money:
                coffee_maker.make_coffee(drink)
    elif decision == "report":
        coffee_maker.report()
        money_machine.report()
    elif decision == "off":
        exit()
    else:
        print("TYPE ERROR")







