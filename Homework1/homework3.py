#1
menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}
#2
def sort_menu():
    for x in sorted(menu.keys()):
        print(x, menu[x])
    for x in sorted(menu.items(), key=lambda item: item[1]):
        print(x)
# sort_menu()
#3
def average_price():
    a_price=sum(map(lambda x: float(x), menu.values())) / len(menu)
    print(a_price)
# average_price()
#4
def add_menu():
    menu.update({input('Введите название нового блюда: '): int(input('Введите цену нового блюда: '))})
    print(menu)
# add_menu()
#5
def delet_dish_menu():
    delet_dish = input('Введите блюдо для удаления: ')
    menu.pop(delet_dish) if delet_dish in menu else menu
    print(menu)
# delet_dish_menu()
#6
def filter_price_menu():
    N = int(input('Введите нужную цену: '))
    filter_dish= list(filter(lambda dish: menu[dish] <= N, menu.keys()))
    print(filter_dish)
# filter_price_menu()
#7
def min_max_dish_menu():
    min_dish = min(menu.items(), key=lambda x: x[1])
    max_dish = max(menu.items(), key=lambda x: x[1])
    print(min_dish)
    print(max_dish)
# min_max_dish_menu()
#8
def sorted_drinks_menu():
    drinks = ["coffee", "tea", "juice"]
    filtered_drinks = list(filter(lambda x: x[0] in drinks, menu.items()))
    sorted_drinks = sorted(filtered_drinks, key=lambda x: x[1])
    print(sorted_drinks)
# sorted_drinks_menu()


#9
order_input = input("Введите ваш заказ (через запятую): ")
items_list = order_input.split(',')
valid_order = dict(filter(lambda dish: dish[0] in menu.keys(), [(dish, menu[dish]) for dish in items_list]))
print(valid_order)
#10
from functools import reduce
total_cost = reduce(lambda total,new_cost :total+new_cost, valid_order.values())
#11
print("Ваш заказ:")
for idx, (item, price) in enumerate(valid_order.items(), start=1):
    print(f"{idx}. {item} — {price} руб.")
print(f"Итого: {total_cost} руб.")
#12
if not any(valid_order):
    print("Вы ничего не выбрали.")
elif total_cost > 500:
    print("Поздравляем, у вас скидка 10%!")

