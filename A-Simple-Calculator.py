# In this project, I am building a simple calculator that can do calculations with two numbers.

# First, I create four functions that do four types of calculation:

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y


# Here, the calculator shows the prompts for the four types of calcutations:
print("Enter 'A' for addition.")
print("Enter 'S' for subtraction.")
print("Enter 'M' for multiplication.")
print("Enter 'D' for division.")


# "while True" keeps the calculator running as long as there is something running in this while loop
while True:
    
    # Here, the user specify their type of calculation of choice
    choice = input('Enter choice (A, S, M, D): ')

    # Here, the calculator checks what type of calculation the user wants it to do.
    if choice.upper() in ('A', 'ADD', 'ADDITION', 'S', 'SUBTRACT', 'SUBTRACTION', 'M', 'MULTIPLY', 'MULTIPLICATION', 'D', 'DIVIDE', 'DIVISION'):
        # Here, the user enters the first number
        # The data type must be converted to "float" because the data type of the output of the input function is "string"
        num1 = float(input('Enter the first number: '))
        # Here, the user enters the second number
        num2 = float(input('Enter the second number: '))
    
        # Here, the calculator prints out the result if the type of calculation of choice is addtion
        if choice.upper() in ('A', 'ADD', 'ADDITION'):
            print('Result:', num1, '+', num2, '=', add(num1, num2))
    
        # Here, the calculator prints out the result if the type of calculation of choice is subtraction
        elif choice.upper() in ('S', 'SUBTRACT', 'SUBTRACTION'):
            print('Result:', num1, '-', num2, '=', subtract(num1, num2))
    
        # Here, the calculator prints out the result if the type of calculation of choice is multiplication
        elif choice.upper() in ('M', 'MULTIPLY', 'MULTIPLICATION'):
            print('Result:', num1, '*', num2, '=', multiply(num1, num2))
    
        # Here, the calculator prints out the result if the type of calculation of choice is division:
        elif choice.upper() in ('D', 'DIVIDE', 'DIVISION'):
            print('Result:', num1, '/', num2, '=', divide(num1, num2))

    # Here, the calculator shows this prompt if the user's answer is not applicable.
    else:
        print('Please input a correct choice.')

    # Here, the calculator asks the user if they want to do another calculation after one.
    next_calculation = input('Want to do another calculation? (yes/no): ')

    # Here, this if statement stops the calculator if the user's answer to the last question is "no".
    if next_calculation.upper() in ('N', 'NO', 'NOPE'):
        break
