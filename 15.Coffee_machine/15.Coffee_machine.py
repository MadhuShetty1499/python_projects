from Coffee_machine_menu import MENU, resources

money = 0


def resource_check(drink, resources):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if ingredient in resources and amount > resources[ingredient]:
            print(f"🔴Sorry, there is not enough {ingredient}.")
            return False
    return True


def make_coffee(drink, resources, money):
    if resource_check(drink, resources):
        print("Please insert coins")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        advance = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
        if advance < MENU[ask]["cost"]:
            print("🔴Sorry that's not enough money. Money refunded.")
        else:
            change = round(advance - MENU[ask]["cost"], 2)
            print(f"You have paid ${advance}")
            print(f"Here is ${change} in change.")
            print(f"Here is your {ask}☕ Enjoy!")
            money += MENU[ask]["cost"]

            for item, value in MENU[ask]["ingredients"].items():
                if item in resources:
                    if resources[item] >= value:
                        resources[item] -= value
                    else:
                        print(f"🔴Sorry, not enough {item}.")
                        break
    return resources, money


while True:
    ask = input("What would you like? (espresso/latte/cappuccino): ")

    if ask == "off":
        print("Machine turned off")
        break

    if ask == "report":
        for key, value in resources.items():
            if key in ["water", "milk"]:
                print(f"{key}: {value}ml")
            elif key == "coffee":
                print(f"{key}: {value}g")
        print(f"money: ${money}")

    if ask not in ["off", "report"]:
        resources, money = make_coffee(ask, resources, money)
