# -*- coding: utf-8 -*-
import snowfall as sf
import simple_draw as sd

sd.set_screen_size(1500, 750)
N = 20

snow_parameters = {}
missing_snowflakes_list = []

red = sd.COLOR_RED
orange = sd.COLOR_ORANGE
yellow = sd.COLOR_YELLOW
green = sd.COLOR_GREEN
cyan = sd.COLOR_CYAN
blue = sd.COLOR_BLUE
purple = sd.COLOR_PURPLE

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
# создать_снежинки(N) - создает N снежинок
# нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
# сдвинуть_снежинки() - сдвигает снежинки на один шаг
# номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
# удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
sf.snowflakes_get_start_parameters(N)
while True:
    # нарисовать_снежинки_цветом(color=sd.background_color)
    sf.snowfall_paint_background_color(N)
    # сдвинуть_снежинки()
    sf.randomize_move(N)
    # нарисовать_снежинки_цветом(color)
    sf.snowfall_paint_by_color(red)
    # если есть номера_достигших_низа_экрана() то
    missing_snowflakes_list = sf.number_of_missing_snowflakes(N)
    if len(missing_snowflakes_list) != 0:
        print(missing_snowflakes_list)
        # удалить_снежинки(номера)
        sf.deleting_snowflakes(missing_snowflakes_list)
        # создать_снежинки(count)
        sf.create_new_snowflake(missing_snowflakes_list)
        missing_snowflakes_list.clear()
    sd.sleep(0.035)
    if sd.user_want_exit():
        break

sd.pause()
