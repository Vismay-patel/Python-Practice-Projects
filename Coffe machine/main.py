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
    "money": 0
}

def resource_checker(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def money_calculate(coffee_price):

    quarters = float(input("How many quareters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickels: "))
    pennies = float(input("How many nickles: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    difference = total - coffee_price

    if difference < 0:
        print("Not enough money")
    else:
        print(f"Here is your change $ {difference:.2f}.")

def resource_calculator(coffee_type):
    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    resources['money'] += MENU[coffee_type]['cost']

def coffee_machine(coffee_type):
    print(f"Price is ${MENU[coffee_type]['cost']}")
    money_calculate(MENU[coffee_type]['cost'])
    resource_calculator(coffee_type) 

turned_on = True
while turned_on:
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_input = input("What would you like? (espresson/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} gm")
        print(f"Money: ${resources['money']}")
    elif user_input == "off":
        print("Machine has been turned off.")
        turned_on = False
    elif user_input == "espresso":
        coffee_machine(user_input)
    elif user_input == "latte":
        coffee_machine(user_input)
    elif user_input == "cappuccino":
        coffee_machine(user_input)
    else:
        print("Please enter a correct command!!!!")

