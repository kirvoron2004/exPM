import matplotlib.pyplot as plt
import codecs
import itertools
import re
def funcc(a, b):
    for k, v in a.items():
        if b in a[k]:
            return k

def fun(a, b):
    x = list(a.values())
    for i in x:
        if b in i:
            return True
def func1(s):
    sss = s
    letters = re.findall(r'[а-яА-ЯёЁa-zA-Z]+', sss)

    # Определение символов и раскладок для Zubachev
    rs_zubachev = ['й', 'м', 'л', 'т', 'б', 'д', 'р', 'с', 'в', 'п', 'н', 'к', 'х', 'ц', 'щ', 'з', 'ж', 'ч']
    ls_zubachev = ['ё', 'ф', 'г', 'ш', 'ы', 'и', 'ь', 'ъ', 'а', 'е', 'ю', 'я', 'о', 'у', 'э']
    layout_zubachev_l = {
        4: {'ё', '1', 'ф', 'г', 'ш'},
        3: {'2', 'ы', 'и', 'ь', 'ъ'},
        2: {'3', 'а', 'е', 'ю'},
        1: {'4', '5', 'я', ',', 'о', 'у', '.', 'э'}
    }
    layout_zubachev_r = {
        1: {'6', '7', 'й', 'м', 'л', 'т', 'б', 'д'},
        2: {'8', 'р', 'с', 'в'},
        3: {'9', 'п', 'н', 'к'},
        4: {'0', ')', '_', '-', '=', '+', 'х', 'ц', 'щ', '/', 'з', 'ж', 'ч'}
    }

    # Подсчет удобных сочетаний для Zubachev
    c_l_zubachev = 0
    c_r_zubachev = 0
    for i in letters:
        if i == 'n':
            pass
        elif fun(layout_zubachev_l, i[0]) and fun(layout_zubachev_l, i[1]):
            if funcc(layout_zubachev_l, i[0]) > funcc(layout_zubachev_l, i[1]):
                c_l_zubachev += 1
        elif fun(layout_zubachev_r, i[0]) and fun(layout_zubachev_r, i[1]):
            if funcc(layout_zubachev_r, i[0]) > funcc(layout_zubachev_r, i[1]):
                c_r_zubachev += 1

    # Общее количество сочетаний для Zubachev
    total_l_zubachev = len(list(itertools.product(ls_zubachev, repeat=2)))
    total_r_zubachev = len(list(itertools.product(rs_zubachev, repeat=2)))

    print(f'Зубачев: Всего возможных сочетаний для левой руки: {total_l_zubachev}')
    print(f'Зубачев: Всего возможных сочетаний для правой руки: {total_r_zubachev}')
    print()
    print(f'Зубачев: для левой руки {c_l_zubachev} удобных сочетаний')
    print(f'Зубачев: для правой руки {c_r_zubachev} удобных сочетаний')
    print()
    # Определение символов и раскладок для Dictor
    rs_dictor = ['з', 'в', 'л', 'н', 'б', 'м', 'к', 'т', 'п', 'д', 'с', 'г', 'ч', 'ш', 'щ', 'р', 'й', 'ж']
    ls_dictor = ['ё', 'ц', 'у', 'ф', 'ь', 'ъ', 'и', 'э', 'я', 'е', 'х', 'о', 'ы', 'а', 'ю']
    layout_dictor_l = {
        4: {'ё', 'ц', '1', 'у', 'ф'},
        3: {'2', 'ь', 'ъ', 'и', 'э'},
        2: {'3', '№', 'я', 'е', 'х'},
        1: {'4', '%', ',', '?', 'о', 'ы', '5', ':', '.', '!', 'а', 'ю'}
    }
    layout_dictor_r = {
        1: {'6', ';', '7', '-', 'з', 'в', 'л', 'н', 'б', 'м'},
        2: {'8', '"', 'к', 'т', 'п'},
        3: {'9', '(', 'д', 'с', 'г'},
        4: {'0', ')', '*', '_', '=', '+', 'ч', 'ш', 'щ', 'р', 'й', 'ж'}
    }

    # Подсчет удобных сочетаний для Dictor
    c_l_dictor = 0
    c_r_dictor = 0
    for i in letters:
        if i == 'n':
            pass
        elif fun(layout_dictor_l, i[0]) and fun(layout_dictor_l, i[1]):
            if funcc(layout_dictor_l, i[0]) > funcc(layout_dictor_l, i[1]):
                c_l_dictor += 1
        elif fun(layout_dictor_r, i[0]) and fun(layout_dictor_r, i[1]):
            if funcc(layout_dictor_r, i[0]) > funcc(layout_dictor_r, i[1]):
                c_r_dictor += 1

    # Общее количество сочетаний для Dictor
    total_l_dictor = len(list(itertools.product(ls_dictor, repeat=2)))
    total_r_dictor = len(list(itertools.product(rs_dictor, repeat=2)))

    print(f'Dictor: Всего возможных сочетаний для левой руки: {total_l_dictor}')
    print(f'Dictor: Всего возможных сочетаний для правой руки: {total_r_dictor}')
    print()
    print(f'Dictor: для левой руки {c_l_dictor} удобных сочетаний')
    print(f'Dictor: для правой руки {c_r_dictor} удобных сочетаний')
    print()

    rs_qwerty = ['н', 'р', 'т', 'г', 'о', 'ь', 'ш', 'л', 'б', 'щ', 'д', 'ю', 'з', 'х', 'ъ', 'Ж', 'э']
    ls_qwerty = ['ё', 'й', 'ф', 'я', 'ц', 'ы', 'ч', 'у', 'в', 'с', 'к', 'а', 'м', 'е', 'п', 'и']
    layout_qwerty_l = {
        4: {'ё', '`', '!', '1', 'й', 'ф', 'я'},
        3: {'"', '@', '2', 'ц', 'ы', 'ч'},
        2: {'№', '#', '3', 'у', 'в', 'с'},
        1: {';', '$', '4', 'к', 'а', 'м', '%', '5', 'е', 'п', 'и'}
    }
    layout_qwerty_r = {
        1: {':', '^', '6', 'н', 'р', 'т', '?', '&', '7', 'г', 'о', 'ь'},
        2: {'*', '8', 'ш', 'л', 'б'},
        3: {'(', '9', 'щ', 'д', 'ю'},
        4: {')', '0', '_', '-', '+', '=', 'з', '[', '{', 'х', ']', '}', 'ъ', ':', 'Ж', ';', '"', 'э', ',',
            '.', '?'}
    }

    # Подсчет удобных сочетаний для qwerty
    c_l_qwerty = 0
    c_r_qwerty = 0
    for i in letters:
        if i == 'n':
            pass
        elif fun(layout_qwerty_l, i[0]) and fun(layout_qwerty_l, i[1]):
            if funcc(layout_qwerty_l, i[0]) > funcc(layout_qwerty_l, i[1]):
                c_l_qwerty += 1
        elif fun(layout_qwerty_r, i[0]) and fun(layout_qwerty_r, i[1]):
            if funcc(layout_qwerty_r, i[0]) > funcc(layout_qwerty_r, i[1]):
                c_r_qwerty += 1

    # Общее количество сочетаний для Zubachev
    total_l_qwerty = len(list(itertools.product(ls_qwerty, repeat=2)))
    total_r_qwerty = len(list(itertools.product(rs_qwerty, repeat=2)))

    print(f'йцукен: Всего возможных сочетаний для левой руки: {total_l_qwerty}')
    print(f'йцукен: Всего возможных сочетаний для правой руки: {total_r_qwerty}')
    print()
    print(f'йцукен: для левой руки {c_l_qwerty} удобных сочетаний')
    print(f'йцукен: для правой руки {c_r_qwerty} удобных сочетаний')
    print()

    rs_call = ['ё', 'н', 'щ', 'э', 'р', 'ц', 'д', 'т', 'м', 'я', 'с', 'ф', 'щ', 'г', 'ж', 'ц', 'ъ', 'в', 'з', 'п']
    ls_call = ['ю', 'ё', 'б', 'ч', 'щ', 'ц', 'ы', 'и', 'х', 'о', 'е', 'э', 'й', 'у', 'ю', 'а', 'к', 'ь']
    layout_call_l = {
        4: {'ю', 'ё', '%', '&', '$', 'б', 'ч', 'щ', 'ц'},
        3: {'7', '[', 'ы', '<', ',', 'и', 'х'},
        2: {'5', '{', 'о', '.', '>', 'е', 'э', 'й'},
        1: {'3', '}', '1', '(', 'у', 'ю', 'а', 'к', '<', '.', 'ь', ',', ';', '_'}
    }
    layout_call_r = {
        1: {'9', '=', '0', '*', '>', 'ё', '"', '^', '.', ':', 'н', 'щ', '?', 'э', 'р', 'ц'},
        2: {'2', ')', 'д', 'т', 'м'},
        3: {'4', '+', 'я', 'с', 'ф'},
        4: {'6', ']', '8', '!', '#', 'щ', '№', 'г', 'ж', 'ц', '@', 'ъ', '|', 'в', '№', 'з', '-', 'п'}
    }

    # Подсчет удобных сочетаний для qwerty
    c_l_call = 0
    c_r_call = 0
    for i in letters:
        if i == 'n':
            pass
        elif fun(layout_call_l, i[0]) and fun(layout_call_l, i[1]):
            if funcc(layout_call_l, i[0]) > funcc(layout_call_l, i[1]):
                c_l_call += 1
        elif fun(layout_call_r, i[0]) and fun(layout_call_r, i[1]):
            if funcc(layout_call_r, i[0]) > funcc(layout_call_r, i[1]):
                c_r_call += 1

    # Общее количество сочетаний для Zubachev
    total_l_call = len(list(itertools.product(ls_call, repeat=2)))
    total_r_call = len(list(itertools.product(rs_call, repeat=2)))

    print(f'вызов: Всего возможных сочетаний для левой руки: {total_l_call}')
    print(f'вызов: Всего возможных сочетаний для правой руки: {total_r_call}')
    print()
    print(f'вызов: для левой руки {c_l_call} удобных сочетаний')
    print(f'вызов: для правой руки {c_r_call} удобных сочетаний')
    labels = ['call (Правая)', 'call (Левая)', 'qwerty (Правая)', 'qwerty (Левая)', 'Dictor (Правая)', 'Dictor (Левая)',
              'Зубачев (Правая)', 'Зубачев (Левая)']
    convenient_counts = [c_l_zubachev, c_r_zubachev, c_l_dictor, c_r_dictor, c_l_qwerty, c_r_qwerty, c_l_call, c_r_call]
    total_counts = [total_l_zubachev, total_r_zubachev, total_l_dictor, total_r_dictor, total_l_qwerty, total_r_qwerty,
                    total_l_call, total_r_call]

    x = range(len(labels))

    plt.barh(x, total_counts, color='lightgrey', label='Все сочетания')
    plt.barh(x, convenient_counts, color='blue', label='Удобные сочетания')

    plt.yticks(x, labels)
    plt.xlabel('Количество сочетаний')
    plt.title('Диграммы')
    plt.legend()
    for i, (convenient, total) in enumerate(zip(convenient_counts, total_counts)):
        plt.text(total + 5, i, str(total), va='center', color='grey')  # Для всех сочетаний
        plt.text(convenient + 5, i, str(convenient), va='center', color='blue')  # Для удобных сочетаний

    plt.show()
