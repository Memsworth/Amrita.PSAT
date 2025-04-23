import math
import stat


def Q3_7():
    def CalculateBacteria(hour):
        return int(200*math.pow(2,hour))

    print(f"{'Hour':>4} {'Number of Bacteria':>20}")
    for i in range(0, 16, 5):
        print(f"{i:>4} {CalculateBacteria(i):>20}")

def Q3_8():
    def GetPositiveNumber(message):
        while True:
            user_input = int(input(f'{message}'))
            if user_input > -1:
                return user_input

    def PrintData(infection_data):
        print(f'min infection: {min(infection_data)} on day {infection_data.index(min(infection_data))+1}')
        print(f'large infection: {max(infection_data)} on day {infection_data.index(max(infection_data))+1}')
        print(f'avg infection rate: {round(sum(infection_data)/len(infection_data),2)} for about {len(infection_data)} days')
        print(f'total infected: {sum(infection_data)}')
    
    #program starts here
    infection_data = []
    for i in range(7):
        message = f'Enter number of infections for day {i+1}: '
        infection_data.append(GetPositiveNumber(message))

    PrintData(infection_data)
def Q3_11():
    rabbit = []
    doe = []
    num_of_does = int(input('Enter the number of does in the rabbit colony (-1 to end): '))
    while num_of_does != -1:
        doe.append(num_of_does)
        rabbit_born = int(input('Number of baby rabbits born in the past month: '))
        rabbit.append(rabbit_born)
        print(f'On average {round((rabbit_born/num_of_does), 2)} baby rabbits were born for each doe')
        num_of_does = int(input('Enter the number of does in the rabbit colony (-1 to end): '))

    print(f'Total number of baby rabbits for each doe so far: {round(sum(rabbit)/sum(doe), 2)}')

def Q3_12():
    def is_equilateral(a, b, c):
        return a == b == c
    try:
        a, b, c = map (int, input('Triangle: ').split(','))
        if a <= 0 or b <= 0 or c <= 0:
            print("Side lengths must be positive numbers.")
        elif is_equilateral(a, b, c):
            print("This is an equilateral triangle.")
        else:
            print("This is NOT an equilateral triangle.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def Q3_13():
    def is_perfect(number):
        divisors = []
        for i in range(1, number):
            if number % i == 0:
                divisors.append(i)
        return sum(divisors) == number

    user_input = int(input('>'))
    if is_perfect(user_input):
        print('perfect number')
    else:
        print('not perfect number')

def Q3_14():

    total_count = 0
    number = 4
    state = 'min'
    n = 3
    while abs(number - 3.1415) >= 0.00001:
        if state == 'min':
            number -= (4 / n)
            n += 2
            total_count += 1
            state = 'add'
        elif state == 'add': 
            number += (4 / n)
            n += 2
            total_count += 1
            state = 'min'
    print(total_count)
    print(number)
    
def Q3_15():

    def get_febo(n):
        if n == 0:
            return [0];
        elif n == 1:
            return [0,1];

        fib = [0,1]

        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    n_term = int(input('>'))
    febo = get_febo(n_term)
    print(febo[-1])

Q3_15()