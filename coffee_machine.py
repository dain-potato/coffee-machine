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

def print_report():
    """ Prints the remaining resources, and the profit. """
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: ${resources["profit"]}")


def check_resources():
    """" Checks if there are enough resources to make the coffee. """
    for item in MENU[user_drink]["ingredients"]:
        if MENU[user_drink]["ingredients"][item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return  True


def process_coins():
    """ Asks the user for the number of quarters, dimes, nickles, and pennies to insert, returns the total coins inserted """
    print("Please insert coins.")
    no_of_quarters = int(input("How many quarters?: "))
    no_of_dimes = int(input("How many dimes?: "))
    no_of_nickles = int(input("How many nickles?: "))
    no_of_pennies = int(input("How many pennies?: "))
    inserted_coins = (0.25 * no_of_quarters) + (0.10 * no_of_dimes) + (0.05 * no_of_nickles) + (0.01 * no_of_pennies)
    return inserted_coins


def check_transaction(check_user_coins):
    """ Checks if the transaction is successful, by checking if users coins is enough to buy their drink of choice. """
    if check_user_coins < MENU[user_drink]["cost"]:
        print("Sorry that's not enough money. Money Refunded.")
        return False
    else:
        resources["profit"] += MENU[user_drink]["cost"]
        if check_user_coins > MENU[user_drink]["cost"]:
            print(f"Here is ${round(check_user_coins - MENU[user_drink]["cost"], 2)} dollars in change.")
        return True


def make_coffee():
    """ Reduces the resources based on the ingredients used. """
    if user_drink != "espresso":
        resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
    resources["water"] -= MENU[user_drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
    print(f"Here is your {user_drink}. Enjoy!")


is_machine_on = True
resources["profit"] = 0
while is_machine_on:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_drink == "off":
        is_machine_on = False
    elif user_drink == "report":
        print_report()
    elif user_drink == "espresso" or user_drink == "latte" or user_drink == "cappuccino":
        if check_resources():
            user_coins = process_coins()
            if check_transaction(user_coins):
                make_coffee()
    else:
        print("Sorry, we don't have that in our menu.")
