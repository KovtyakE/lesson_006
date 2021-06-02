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
    global initiated_number
    global size_of_number
    while len(initiated_number) < size_of_number:
        number = get_number()

        initiated_number.append(number)

    for num in initiated_number:
        print(num, end="")
    print("")


def user_input_check():
    while True:
        print("Введите ", size_of_number, "-значное число: ", sep="")
        user_input = input()
        if len(user_input) == size_of_number:
            try:
                user_input = int(user_input)
            except:
                print("Введите корректное значение!")
            return user_input
        else:
            print("Введите корректное значение!")


def check_of_number():
    pass

#TODO посимвольно аппенд значений юзер инпута в список для сравнения


initial_of_number()
user_input_check()
