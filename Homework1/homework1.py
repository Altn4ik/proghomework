# 1 ЗАДАНИЕ
# def convert_temperature(value, from_scale, to_scale):
#     try:
#         temp_value = float(value)
#         if from_scale == 'C':
#             if temp_value < -273.15:
#                 raise ValueError("Температура ниже абсолютного нуля!")
#             if to_scale == 'F':
#                 result = temp_value * 9 / 5 + 32
#             elif to_scale == 'K':
#                 result = temp_value + 273.15
#             else:
#                 result = temp_value
#         elif from_scale == 'F':
#             if temp_value < -459.67:
#                 raise ValueError("Температура ниже абсолютного нуля!")
#             if to_scale == 'C':
#                 result = (temp_value - 32) * 5 / 9
#             elif to_scale == 'K':
#                 result = (temp_value + 459.67) * 5 / 9
#             else:
#                 result = temp_value
#         elif from_scale == 'K':
#             if temp_value < 0:
#                 raise ValueError("Температура ниже абсолютного нуля!")
#             if to_scale == 'C':
#                 result = temp_value - 273.15
#             elif to_scale == 'F':
#                 result = temp_value * 9 / 5 - 459.67
#             else:
#                 result = temp_value
#         else:
#             raise ValueError("Некорректная шкала измерения!")
#         return round(result, 2)
#     except ValueError as err:
#         print(err)
#         return None
#
# initial_temp = input("Введите начальное значение температуры: ")
# from_scale = input("Из какой шкалы перевести (C/F/K)? ").upper()
# to_scale = input("В какую шкалу перевести (C/F/K)? ").upper()
#
# converted_temp = convert_temperature(initial_temp, from_scale, to_scale)
# if converted_temp is not None:
#     print(f"Преобразованная температура: {converted_temp}{to_scale}")
# else:
#     print('Ошибка')

#2 ЗАДАНИЕ
