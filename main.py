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
        "cost": 3,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """ Returns True When Order Can Be Made, False If Ingredients Are Insufficient. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry There In Not Enough {item}.")
            return False
    return True


def process_coins():
    """ Returns The Total Calculated From Coins Inserted."""
    print("Please Insert Coins.")
    total = int(input("How Many quarters?:")) * 0.25
    total += int(input("How Many dimes?:")) * 0.1
    total += int(input("How Many nickels?:")) * 0.05
    total += int(input("How Many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """ Returns The Total When Payment Is Accepted, Or False If Money Is Insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here Is Change: INR. {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry Money Is Not Enough, Money Returned...")
    return False


def make_coffee(drink_name, order_ingredients):
    """ Deducts The Ingredients From The Resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here Is Your {drink_name} And Have It...")


is_on = True

while is_on:
    choice = input("Select Your Option? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}gr")
        print(f"money: INR. {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
