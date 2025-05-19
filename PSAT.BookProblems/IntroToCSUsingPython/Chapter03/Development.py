import calendar
import math
def D1():
    def pound_to_gm(val):
        return val * 453.6
    def gm_to_pound(val):
        return val / 453.6
    def km_to_mi(val):
        return val / 1.609
    def mi_to_km(val):
        return val * 1.609
    def in_to_cm(val):
        return val * 2.54
    def cm_to_in(val):
        return val / 2.54

    user_input = input('A value please: ')
    ['lb', 'gm', 'km', 'mi', 'in', 'cm']

    tokens = user_input.split()
    if tokens[1] in user_input:
        #start
        if (tokens[1] == 'lb'):
            print(str(pound_to_gm(float(tokens[0]))) + ' grams')
        if (tokens[1] == 'gm'):
            print(str(gm_to_pound(float(tokens[0]))) + ' pounds')
        if (tokens[1] == 'km'):
            print(str(km_to_mi(float(tokens[0]))) + ' miles')
        if (tokens[1] == 'mi'):
            print(str(mi_to_km(float(tokens[0]))) + ' kilometers')
        if (tokens[1] == 'in'):
            print(str(in_to_cm(float(tokens[0]))) + ' cm')
        if (tokens[1] == 'cm'):
            print(str(cm_to_in(float(tokens[0]))) + ' in')
    else:
        print("error")


def D2():
    dateOne, dateTwo = map(int, input('Enter dates: ').split(' '))
    for i in range(dateOne, dateTwo):
        if calendar.isleap(i):
            print(i)


def D3():
    house_payment = int(input('house cost: '))
    income = int(input('your income: '))
    previous_owned = input('did you own a home before this (yes or no): ')
    loan_acceptance = True
    if house_payment > 800000 or income > 225000 or previous_owned == 'yes':
        loan_acceptance = False
        
    if loan_acceptance:
        print('Here is some 8K USD for you')
    else:
        print('Rejected')

def D4():
    def calculate_monthly_payment(P, r, n):
        monthly_rate = r / 12 / 100
        total_payments = n * 12
        return P * (monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)

    def print_loan_schedule(loan_amount, terms):
        print(f"Loan Amount: ${loan_amount:,.2f} Term: {terms} years\n")
        print(f"{'Interest Rate':<15}{'Monthly Payment'}")
        for rate in range(3, 19):
            monthly_payment = calculate_monthly_payment(loan_amount, rate, terms)
            print(f"{rate:<15}{monthly_payment:,.2f}")

    loan_amount = int(input('Loan amount: '))
    n = int(input('Years: '))
    print_loan_schedule(loan_amount, n)


D4()