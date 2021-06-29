# -*- coding: utf-8 -*-
from random import randint
import simple_draw as sd

snow_parameters = {}
missing_snowflakes_list = []


def snowflakes_get_start_parameters(N):
    # создание списка из N точек координат х с интервалом в 30 пикселей
    snowflakes_list = {(n + 1) for n in range(N)}
    # создание словаря координат с параметрами факторов формы снежинок, объявление переменных для внесения изменений
    # в словарь в будущем, таких как изменение координаты у в меньшую сторону, значение самой координаты у, значение
    # смещения координаты х, непосредственные значения координаты х

    for number in snowflakes_list:
        factor_a = randint(4, 8) / 10
        factor_b = randint(25, 45) / 100
        factor_c = randint(50, 70)
        coord_y = randint(750, 950)  # значение у по умолчанию, будет изменено
        coord_x = randint(100, 1400)  # начальные координаты х, равные значению из списка. В цикле изменяется
        size = randint(15, 30)
        snow_parameters[number] = [factor_a, factor_b, factor_c, coord_y, coord_x, size]


def randomize_move(N):
    for number in snow_parameters:
        # цикл для создания рандомных переменных для каждого number (в каждой итерации разные)
        snow_parameters[number][3] -= randint(2, 4)
        snow_parameters[number][4] += randint(-1, 1)

def snowfall_paint_background_color(N):
    sd.start_drawing()
    for number in snow_parameters:
        factor_a = snow_parameters[number][0]
        factor_b = snow_parameters[number][1]
        factor_c = snow_parameters[number][2]
        coord_y = snow_parameters[number][3]
        coord_x = snow_parameters[number][4]
        size = snow_parameters[number][5]
        start_point = sd.get_point(coord_x, coord_y)
        sd.snowflake(start_point, length=size, color=sd.background_color, factor_a=factor_a,
                     factor_b=factor_b, factor_c=factor_c)
        # snow_parameters[number] = factor_a, factor_b, factor_c, coord_y, coord_x, size
    sd.finish_drawing()


def snowfall_paint_by_color(color):
    sd.start_drawing()
    for number in snow_parameters:
        # цикл отрисовывания всех N снежинок по координатам из словаря с учетом смещений
        factor_a = snow_parameters[number][0]
        factor_b = snow_parameters[number][1]
        factor_c = snow_parameters[number][2]
        coord_y = snow_parameters[number][3]
        coord_x = snow_parameters[number][4]
        size = snow_parameters[number][5]
        start_point = sd.get_point(coord_x, coord_y)
        sd.snowflake(start_point, length=size, color=color, factor_a=factor_a, factor_b=factor_b,
                     factor_c=factor_c)
    sd.finish_drawing()


def number_of_missing_snowflakes(N):
    # missing_snowflakes_list.clear()
    for number in snow_parameters:
        coord_y = snow_parameters[number][3]
        if coord_y < -30:
            missing_snowflakes_list.append(number)
    missing_snowflakes_list.sort()
    return missing_snowflakes_list


def deleting_snowflakes(list_which_snowflake_to_delete):
    sd.start_drawing()
    for number in list_which_snowflake_to_delete:
        factor_a = snow_parameters[number][0]
        factor_b = snow_parameters[number][1]
        factor_c = snow_parameters[number][2]
        coord_y = snow_parameters[number][3]
        coord_x = snow_parameters[number][4]
        size = snow_parameters[number][5]
        start_point = sd.get_point(coord_x, coord_y)
        sd.snowflake(start_point, length=size, color=sd.background_color, factor_a=factor_a,
                     factor_b=factor_b, factor_c=factor_c)
        snow_parameters[number] = factor_a, factor_b, factor_c, coord_y, coord_x, size
    sd.finish_drawing()


def create_new_snowflake(number_list):
    for number in number_list:
        coord_x = randint(100, 1400)
        coord_y = randint(750, 950)
        factor_a = randint(4, 8) / 10
        factor_b = randint(25, 45) / 100
        factor_c = randint(50, 70)
        size = randint(20, 30)
        snow_parameters[number] = [factor_a, factor_b, factor_c, coord_y, coord_x, size]
