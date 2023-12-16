# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    from Calculator_art import logo
    print(logo)
    num1 = float(input("What's the first number? "))
    for operand in operations:
        print(operand)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number? "))

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
    while cont == "y":
        num1 = answer
        for operand in operations:
            print(operand)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if cont == "n":
            x = False
            calculator()


x = True
while x:
    calculator()
