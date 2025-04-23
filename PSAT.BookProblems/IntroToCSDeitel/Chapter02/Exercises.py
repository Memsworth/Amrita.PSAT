import math


def Q2_5():
    EggsInOneBox = 6
    TotalEggs = 28
    print('28 eggs & 6 eggs per box is equal to: ')
    print(f'{TotalEggs}/{EggsInOneBox}' + f'= {TotalEggs//EggsInOneBox} in box')
    print(f'That is a total of {(TotalEggs//EggsInOneBox)*EggsInOneBox} eggs')
    print(f'Last box contains = {TotalEggs%EggsInOneBox} eggs')

def Q2_6():
    numInput = int(input('> '))
    if numInput % 2 == 0:
        print("even")
    else:
        print("odd")

def Q2_7():
    marbles = 22
    numOfFriends = 4
    print(f'Jonah has {marbles} marbles & {numOfFriends} friends')
    print(f'Jonah will give {marbles//numOfFriends} marbel per friend')
    print(f'While he will have {marbles%numOfFriends} remaining')

def Q2_8():
    startBacteria = 200
    time = 0
    print(f"{'Hour':>4} {'Number of Bacteria':>20}")
    print(f"{time:>4} {int(200*math.pow(2,time)):>20}")
    print(f"{time+5:>4} {int(200*math.pow(2,time+5)):>20}")
    print(f"{time+10:>4} {int(200*math.pow(2,time+10)):>20}")
    print(f"{time+15:>4} {int(200*math.pow(2,time+15)):>20}")

def Q2_10():
    course1Name = input("Enter the name of the first course: ")
    course1Grade = int(input(f"Enter the grade for {course1Name}: "))

    course2Name = input("Enter the name of the second course: ")
    course2Grade = int(input(f"Enter the grade for {course2Name}: "))

    course3Name = input("Enter the name of the third course: ")
    course3Grade = int(input(f"Enter the grade for {course3Name}: "))

    courses = [(course1Name, course1Grade), (course2Name, course2Grade),(course3Name, course3Grade)]

    average = sum([course1Grade, course2Grade, course3Grade])/3
    highest = max(courses, key=lambda x: x[1])
    lowest = min(courses, key=lambda x: x[1])

    #print area
    print("\n--- Grade Summary ---")
    print(f"{'Course':<15} {'Grade':>6}")
    print(f"{course1Name:<15} {course1Grade:>6}")
    print(f"{course2Name:<15} {course2Grade:>6}")
    print(f"{course3Name:<15} {course3Grade:>6}")

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Highest Grade: {highest[0]} ({highest[1]})")
    print(f"Lowest Grade : {lowest[0]} ({lowest[1]})")

def Q2_11():
    print('Enter number of seconds: ')
    numOfSeconds = int(input('>'))
    expressionBuilder = ""
    seperator = ' - '
    oneHour = 3600
    oneMin = 60

    if(numOfSeconds < 0):
        print('awful input')
    else:
        # hour
        if(numOfSeconds >= oneHour):
            expressionBuilder += f'{numOfSeconds//oneHour}' + seperator
            numOfSeconds -= (oneHour * (numOfSeconds//oneHour))
        else:
            expressionBuilder += '0' + seperator
        # min
        if(numOfSeconds >= oneMin):
            expressionBuilder += f'{numOfSeconds//oneMin}' + seperator
            numOfSeconds -= (oneMin * (numOfSeconds//oneMin))
        else:
            expressionBuilder += '0' + seperator
        # remaining seconds
        expressionBuilder += f'{numOfSeconds}'

    print(str(expressionBuilder))

