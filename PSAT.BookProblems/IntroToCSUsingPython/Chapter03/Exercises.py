def P1_2():
    char_input = str(input('>'))

    if char_input.upper() == 'A':
        print('Apple')
    elif char_input.upper() == 'B':
        print('Banana')
    elif char_input.upper() == 'C':
        print('Coconut')
    else:
        print('Wrong')

def P3():
    credits_input = int(input('>'))
    
    if credits_input >= 90:
        print('Senior Status')
    elif credits_input < 90 and credits_input >=60:
        print('Junior Status')
    elif credits_input < 60 and credits_input >=30:
        print('Sophomore Status')
    else:
        print('Freshman Status')

def P4():
    inputs = []

    while True:
        user_input = int(input('>'))
        if user_input < 1:
            break
        elif user_input > 99:
            continue  
        else:
            inputs.append(user_input)

    print(f'{sum(inputs)}')

def P5():
    positive_count = 0
    negative_count = 0

    print("Enter integers (type 'done' to finish):")

    while True:
        user_input = input("Enter a number: ")
    
        if user_input.lower() == 'done':
            break
    
        try:
            number = int(user_input)
            if number > 0:
                positive_count += 1
            elif number < 0:
                negative_count += 1
        except ValueError:
            print("Invalid input. Please enter an integer or 'done' to finish.")

    print(f"\nNumber of positive values entered: {positive_count}")
    print(f"Number of negative values entered: {negative_count}")

def P6_7():
    i = 1
    while i < 101:
        print(f"{i:2}", end=" ")
        if i % 10 == 0:
            print()
        i+=1