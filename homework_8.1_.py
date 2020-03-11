def cook_book(book):
    cooking_book = {}
    for dish in book:
        key = dish.strip()
        count = int(book.readline())
        values = list()
        for _ in range (count):
            value = book.readline().strip()
            value = value.split(' | ')
            value_dict = {'ingridient_name': value[0], 'quantity': int(value[1]), 'measure': value[2]}
            values.append(value_dict)
        book.readline()
        cooking_book[key] = values
    return cooking_book

with open('recipes.txt', encoding='utf8') as list_dishes:
     print(cook_book(list_dishes))