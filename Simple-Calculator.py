# Task 2 - Simple Calculator
def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide a number with zero")
    return n1/n2


def exponent(n1, n2):
    return n1 ** n2


def modulus(n1, n2):
    if n2 == 0:
        print("Modulus division by zero is undefined")
    return n1 % n2


operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'exponent': exponent,
    'modulus': modulus,
}


def calculate_result():
    while True:
        operation = input("\nEnter operation (Add/Subtract/Multiply/Divide/Exponent/Modulus/Exit): ").lower()

        if operation == 'exit':
            return 0

        else:
            if operation in operations:
                n1 = float(input("Enter number 1: "))
                n2 = float(input("Enter number 2: "))

                result = operations[operation](n1, n2)

                print(f"Result = {result}")

            else:
                print("Invalid operation")


calculate_result()
