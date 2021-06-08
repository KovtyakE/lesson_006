from random import randint

initiated_number = []
size_of_number = 4


def initial_of_number():
    # global initiated_number
    # global size_of_number
    while len(initiated_number) < size_of_number:
        number = randint(0, 9)
        for element in initiated_number:
            if number != element:
                continue
            else:
                number = None
                break
        if number is not None:
            initiated_number.append(number)


def user_input_check(user_input):
    user_number = []
    if len(user_input) == size_of_number and user_input.isnumeric():
        for element in user_input:
            user_number.append(int(element))
        return user_number
    else:
        return None


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
