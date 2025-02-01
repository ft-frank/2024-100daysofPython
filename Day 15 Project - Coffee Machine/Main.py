MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def ask():
    choice: str = input("  What would you like? (espresso/latte/cappuccino): ")
    return choice


def off():
    exit()


def report():
    print("Current resource values:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Milk: {resources['coffee']}g")
    if money > 0:
        print(f"Money: ${money}")


def coins(drink):
    cost = float(MENU[drink]["cost"])
    penny = float(input("how many pennies?")) * 0.01
    nickel = float(input("how many nickels?")) * 0.05
    dime = float(input("how many dimes?")) * 0.1
    quarter = float(input("how many quarters?")) * 0.25
    total = round(float((penny + nickel + dime + quarter - cost)), 2)
    if (penny + nickel + dime + quarter) < cost:
        print("Sorry you don't have enough money.  Money Refunded. ")
        return 0
    elif (penny + nickel + dime + quarter) > cost:
        print(f"Here is ${total} in change")
        print(f"Here is your {decision}, enjoy!")
        return total
    else:
        return 0


def minus(type_drink):
    if type_drink == "latte" or type_drink == "cappuccino":
        resources["milk"] -= MENU[type_drink]["ingredients"]["milk"]
        resources["water"] -= MENU[type_drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[type_drink]["ingredients"]["coffee"]
    if type_drink == "espresso":
        resources["water"] -= MENU[type_drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[type_drink]["ingredients"]["coffee"]




while True:
    sufficient: bool = True
    decision = str(ask().lower())
    if decision == "latte" or decision == "cappuccino" or decision == "espresso":
        if int(MENU[decision]["ingredients"]["water"]) > resources["water"]:
            print(" Sorry there is not enough water")
            sufficient = False

        if decision == "latte" or decision == "cappuccino":
            if int(MENU[decision]["ingredients"]["milk"]) > resources["milk"]:
                print(" Sorry there is not enough milk")
                sufficient = False

        if int(MENU[decision]["ingredients"]["coffee"]) > resources["coffee"]:
            print(" Sorry there is not enough coffee")
            sufficient = False

        if sufficient:
            payment = int(coins(decision))
            money += payment
            minus(decision)


    elif decision == "report":
        report()

    elif decision == "off":
        off()

    else:
        print("TYPE ERROR, TRY AGAIN")
