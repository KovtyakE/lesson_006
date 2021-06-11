from random import randint

initiated_number = []
size_of_number = 4


def initial_of_number():
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


def check_of_number(user_number, counter):
    bulls = 0
    cows = 0
    for count in range(size_of_number):
        if user_number[count] == initiated_number[count]:
            bulls += 1
        else:
            for init_num in initiated_number:
                if user_number[count] == init_num:
                    cows += 1
    return bulls, cows

