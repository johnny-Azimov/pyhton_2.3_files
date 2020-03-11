def cook_book(book):
    cooking_book = {}
    for dish in book:
        key = dish.strip()
        count = int(book.readline())
        values = list()
        for _ in range(count):
            value = book.readline().strip()
            value = value.split(' | ')
            value_dict = {'ingridient_name': value[0], 'quantity': int(value[1]), 'measure': value[2]}
            values.append(value_dict)
        book.readline()
        cooking_book[key] = values
    return cooking_book



def get_shop_list_by_dishes(dishes, person_count, list):
    order_list = {}
    information = cook_book(list)
    for dish in dishes:
        if dish in information:
            for recipe  in information[dish]:
                key = recipe['ingridient_name']
                if recipe['ingridient_name'] not in order_list:
                    key = recipe['ingridient_name']
                    value = {'measure': recipe['measure'], 'quantity': recipe['quantity'] * person_count}
                    order_list.update({key : value})
                else:
                    count = order_list[recipe['ingridient_name']]['quantity'] + recipe['quantity'] * person_count
                    value = {'measure': recipe['measure'], 'quantity': count}
                    order_list.update({key : value})
        else:
            print(f'Ошибка! Данного блюда {dish} нету в меню')
    return order_list

with open('recipes.txt', encoding='utf8') as list_dishes:
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, list_dishes))