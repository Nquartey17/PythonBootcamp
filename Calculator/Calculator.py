import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


print(art.logo)
game_over = True
first_num = float(input("Enter the first number: "))

while game_over:
    operation = input("Enter an operation: ")
    second_num = int(input("Enter a second number: "))
    answer = operations[operation](first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {answer}")

    cnt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if cnt == "y":
        first_num = answer

    else:
        game_over = False
        print("\n" * 20)




