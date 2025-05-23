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

#Coin values
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

machine_money = 0

def value_check(word, value):
    if resources[word] < value:
        print(f"Sorry, there is not enough {word}")
        return False
    return True

def resource_check(water, milk, coffee, drink_name):

    if value_check("water", water) and value_check("milk",milk) and value_check("coffee",coffee):
        # Deplete resources
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee

        print("Please enter coins")
        quarters = int(input("Number of quarters: "))
        dimes = int(input("Number of dimes: "))
        nickels = int(input("Number of nickels: "))
        pennies = int(input("Number of pennies: "))

        money = (quarters * quarter) + (dimes * dime) + (nickels * nickel) + (pennies * penny)
        if money < MENU[drink_name]["cost"]:
            print(f"${money} isn't enough for {drink_name}. ${MENU[drink_name]['cost']} is needed")
            resources["water"] += water
            resources["milk"] += milk
            resources["coffee"] += coffee
        else:
            change = money - MENU[drink_name]['cost']
            print("Change: $", round(change,2))
            print(f"Here is your {drink_name}, enjoy!")
            

end_program = True
while end_program:
    drink = input("Select your drink: espresso/latte/cappuccino ")
    if drink == "espresso":
        #Opting for just typing values to read code easily
        resource_check(50, 0, 18, "espresso")
        machine_money += MENU["espresso"]['cost']
    elif drink == "latte":
        resource_check(200, 150, 24, "latte")
        machine_money += MENU["latte"]['cost']
    elif drink == "cappuccino":
        resource_check(250, 100, 24, "cappuccino")
        machine_money += MENU["cappuccino"]['cost']
    elif drink == "report":
        for key in resources:
            print(key, ":", resources[key])
        print(f"money : ${machine_money}")
    #Bonus to restock the machine
    elif drink == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Machine restocked")
    elif drink == "off":
        end_program = False
    else:
        print("Invalid input")