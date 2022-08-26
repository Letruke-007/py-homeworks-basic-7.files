def open_file():
    with open('cook_book.txt') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line: []})
            k = int(file.readline().strip())
            for _ in range(k):
                lst = file.readline().strip().split(' | ')
                dict = {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}
                cook_book[line].append(dict)
            file.readline()
    return cook_book

def view_cook_book():
    for key, value in open_file().items():
        print(f'\n {key}')
        for dct in value:
            print(f"    {dct['ingredient_name'] + ' - ' + dct['quantity'] + ' ' + dct['measure']}")

def view_shopping_list(s_l):
    print('\nДля приготовления блюд понадобятся следующие ингредиенты:\n')
    index = 1
    for key, values in s_l.items():
        print(f"   {index}. {key} {values['quantity']} {values['measure']}")
        index += 1

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for ingred in dishes:
        for ingr in open_file()[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
            shopping_list.update({name_ingr: ingr})
    view_shopping_list(shopping_list)

def input_ingredients():
    try:
        lst = list(input('Введите интересующие блюда через запятую: ').split(', '))
        persons = int(input('Введите количество персон: '))
        get_shop_list_by_dishes(lst, persons)
    except Exception:
        print('Вы ошиблись. Попробуйте еще раз')

def main():
    print('\n\nВас приветствует кулинарная книга!'.upper())
    while True:
        print('\n\nВыберите нужное действие: '
              '\n   1. Показать список рецептов.'
              '\n   2. Узнать, сколько ингредиентов нужно для выбранных Вами блюд и количества персон.'
              '\n   3. Выйти из программы.')
        prog = str(input('\n=========================================================================================='
                         '\n\n  Выберите нужный вариант: '.upper()))
        if prog == '1':
            view_cook_book()
        elif prog == '2':
            input_ingredients()
        elif prog == '3':
            print('\n Спасибо, что воспользовались нашей программой! До свидания!'.upper())
            break

if __name__ == '__main__':
    main()