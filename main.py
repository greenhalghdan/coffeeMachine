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

PAYMENT = {
    "pennies": {"value": 0.01, "amount": 0},
    "twopennie": {"value": 0.02, "amount": 0},
    "fivepennie": {"value": 0.05, "amount": 0},
    "tenpence": {"value": 0.10, "amount": 0},
    "twentypence": {"value": 0.20, "amount": 0},
    "fiftypence": {"value": 0.50, "amount": 0},
    "pound": {"value": 1, "amount": 0},
    "twopound": {"value": 2, "amount": 0}
}

takings = 0.00
power = True
needed_water = 0
needed_milk = 0
needed_coffee = 0


# TODO: 1. print a report of resources, water, milk, coffee, money
def printreport():
    for resource in resources:
        r = str(resources[resource])
        print(resource + " " + r)
    print(f"Money: {takings}")


# TODO: 2. check sufficent resources when user orders a drink
# TODO: 3. if not enought say sorry not enought of desired recource
def choosedrink():
    global needed_water, needed_milk, needed_coffee
    choice = str.lower(input("What would you like to drink?[espresso/latte/cappuccino] "))
    if choice == "report":
        printreport()
    elif choice == "off":
        print("Powering off machine")
    elif choice == "espresso":
        drink = {}
        drink = MENU[choice]

        needed_water = drink["ingredients"]["water"]
        needed_coffee = drink["ingredients"]["coffee"]

        if needed_water > resources["water"] and needed_milk > resources["milk"] and needed_coffee > resources[
            "coffee"]:
            print("Sorry we don't have enough resources")
        return choice
    else:
        drink = {}
        drink = MENU[choice]
        needed_water = drink["ingredients"]["water"]
        needed_milk = drink["ingredients"]["milk"]
        needed_coffee = drink["ingredients"]["coffee"]

        if needed_water > resources["water"] and needed_milk > resources["milk"] and needed_coffee > resources[
            "coffee"]:
            print("Sorry we don't have enough resources")
        return choice
    return choice


def makedrink(needed_water, needed_milk, needed_coffee):
    resources["water"] -= needed_water
    resources["milk"] -= needed_milk
    resources["coffee"] -= needed_coffee


# TODO: 4. proccess coins, how many quaters, nickelrs, dimes, penies
# TODO: 5. calc what each coin is worth

totalpaied = 0.00


def takepayment():
    totalpaied = 0.00
    for coin in PAYMENT:
        print(f"So far you have paid {totalpaied}")
        PAYMENT[coin]["amount"] = int(input(f"How many of {coin} do you have? "))
        print(PAYMENT[coin])
        totalpaied += (PAYMENT[coin]["amount"] * PAYMENT[coin]["value"])
        print(f"added {totalpaied} to your total")
    return totalpaied


# TODO: 6.clac chnage
def workoutchange(payment, choice):
    change = payment - MENU[choice]["cost"]
    print(f"your change is £{change}")
    return change


# TODO: 7.check transaction is sucessfull and been paid the right amount
def istransctionsucesfull(payment, choice):
    inttakings = 0.00
    print(choice)
    print(MENU[choice])
    if payment < MENU[choice]["cost"]:
        print("Your money has been refunded")
    else:
        print("Transaction sucesfull")
        inttakings += MENU[choice]["cost"]
        success = True
        return inttakings, success


while power:
    choice = choosedrink()
    if choice != "off" and choice != "report":
        payment = takepayment()
        a, b = istransctionsucesfull(payment, choice)
        takings += a
        if b:
            makedrink(needed_water, needed_milk, needed_coffee)
        change = workoutchange(payment, choice)
    elif choice == "off":
        power = False
    else:
        print("invalid command")
