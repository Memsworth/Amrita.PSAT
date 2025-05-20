def P1():
    items = input().split(' ')
    for i in range(0, len(items)):
        if int(items[i]) >= 1 and int(items[i]) <= 100:
            print(f'{items[i]}')

def P3():
    items = input().split(' ')
    items2 = []
    for i in range(0, len(items)):
        if int(items[i]) > 100:
            items2.append('over')
        else:
            items2.append(int(items[i]))
        print(items2)

def P4():
    items = input().split(' ')
    count_a = sum(i.count('a') for i in items)
    print(count_a)

def P5():
    n = int(input('how many fruits: '))
    items = []
    for i in range(n):
        fruit = input(f"Enter name of fruit #{i + 1}: ").strip().capitalize()
        weight = int(input(f"Enter weight in pounds for {fruit}: "))
        items.append((fruit, weight))

    print("\nFruit Inventory:")
    for i, j in items:
        print(f'{i}, {j}')


P5();