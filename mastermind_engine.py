from random import randint

initiated_number = []

size_of_number = 4


def get_number():
    number = randint(0, 9)
    for element in initiated_number:
        if number != element:
            continue
        else:
            number = get_number()
    return number


def initial_of_number():
    # global initiated_number
    # global size_of_number
    while len(initiated_number) < size_of_number:
        number = get_number()
        initiated_number.append(number)

    # for num in initiated_number:
    #     print(num, end="")
    # print("")

from termcolor import cprint

def user_input_check():
    while True:
        user_number = []
        print("Введите ", size_of_number, "-значное число: ", sep="")
        user_input = input()
        if len(user_input) == size_of_number and user_input.isnumeric():
            for element in user_input:
                user_number.append(int(element))
            return user_number
        else:
            cprint("Введите корректное значение!", color='red')


def check_of_number():
    counter = 0
    while True:
        bulls = 0
        cows = 0
        user_number = user_input_check()
        for count in range(size_of_number):

            if user_number[count] == initiated_number[count]:
                bulls += 1
            else:
                for init_num in initiated_number:
                    if user_number[count] == init_num:
                        cows += 1
        counter += 1
        bulls_str = 'Быки: ' + str(bulls)
        cows_str = 'Коровы: ' + str(cows)
        cprint(bulls_str, color='yellow')
        cprint(cows_str, color='yellow')

        if bulls == size_of_number:
            cprint("Вы победили!", color='green')
            print("Это заняло", counter, "ходов, желаете сыграть ещё игру? y/n: ")
            asking = input()
            if asking == "y":
                initiated_number.clear()
                initial_of_number()
                check_of_number()
                break
            else:
                break




