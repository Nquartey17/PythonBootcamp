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

def elements():
    print()

end_program = True
# While end_program

drink = input("Select your drink: espresso/latte/cappuccino ")
if drink == "espresso":
    print(MENU["espresso"]["ingredients"]["water"])
elif drink == "latte":
    print()
elif drink == "cappuccino":
    print()
elif drink == "report":
    print()
elif drink == "off":
    end_program = False
else:
    print("Invalid input")