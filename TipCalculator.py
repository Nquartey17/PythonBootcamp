print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much are you going to tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip /= 100
total_bill = bill + (bill * tip)
payment_per_person = round((total_bill / people), 2)
print("Each person should pay $" + str(payment_per_person))
