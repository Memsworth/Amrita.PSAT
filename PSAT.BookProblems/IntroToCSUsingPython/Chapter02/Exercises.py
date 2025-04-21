def P1():
    print('Enter value: ')
    numberOne = int(input('>'))
    print('Enter value: ')
    numberTwo = int(input('>'))
    print(f'result: {round((numberOne/numberTwo),2)}')

def P2():
    print('Enter value: ')
    numberOne = float(input('>'))
    print('Enter value: ')
    numberTwo = float(input('>'))
    print(f'result: {round((numberOne/numberTwo),6)}')

def P3():
    print('Enter value: ')
    numberOne = float(input('>'))
    print('Enter value: ')
    numberTwo = float(input('>'))
    result = round((numberOne/numberTwo),6)
    print(f'result: {result:.6e}')

def P4():
    char = input("Enter a single uppercase or lowercase letter: ")
    if len(char) == 1 and char.isalpha():
        unicode_value = ord(char)
        print(f"The Unicode encoding for '{char}' is: {unicode_value}")
    else:
        print("Invalid input. Please enter a single alphabet letter (A-Z or a-z).")

def P5():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    print(f"{num1:,} + {num2:,} = {num1 + num2:,}")
    print(f"{num1:,} - {num2:,} = {num1 - num2:,}")
    print(f"{num1:,} * {num2:,} = {num1 * num2:,}")
    print(f"{num1:,} / {num2:,} = {num1 / num2:,.2f}")
    print(f"{num1:,} // {num2:,} = {num1 // num2:,}")
    print(f"{num1:,} % {num2:,} = {num1 % num2:,}")
    print(f"{num1:,} ** {num2:,} = {num1 ** num2:,}")

P5()