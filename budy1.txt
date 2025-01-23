import matplotlib.pyplot as plt
import codecs

def func1(text1):
    layout_zubachev = {
        'Левый мезинец': {'ё', '1', 'ф', 'г', 'ш'},
        'Левый безымянный': {'2', 'ы', 'и', 'ь', 'ъ'},
        'Левый средний': {'3', 'а', 'е', 'ю'},
        'Левый указательный': {'4', '5', 'я', ',', 'о', 'у', '.', 'э'},
        'Большой палец': {' '},
        'Правый указательный': {'6', '7', 'й', 'м', 'л', 'т', 'б', 'д'},
        'Правый средний': {'8', 'р', 'с', 'в'},
        'Правый безымянный': {'9', 'п', 'н', 'к'},
        'Правый мезинец': {'0', ')', '_', '-', '=', '+', 'х', 'ц', 'щ', '/', 'з', 'ж', 'ч'},
    }

    layout_dictor = {
        'Левый мезинец': {'ё', 'ц', '1', 'у', 'ф'},
        'Левый безымянный': {'2', 'ь', 'ъ', 'и', 'э'},
        'Левый средний': {'3', '№', 'я', 'е', 'х'},
        'Левый указательный': {'4', '%', ',', '?', 'о', 'ы', '5', ':', '.', '!', 'а', 'ю'},
        'Большой палец': {' '},
        'Правый указательный': {'6', ';', '7', '-', 'з', 'в', 'л', 'н', 'б', 'м'},
        'Правый средний': {'8', '"', 'к', 'т', 'п'},
        'Правый безымянный': {'9', '(', 'д', 'с', 'г'},
        'Правый мезинец': {'0', ')', '*', '_', '=', '+', 'ч', 'ш', 'щ', 'р', 'й', 'ж'},
    }
    layout_qwerty = {
        'Левый мезинец': {'ё', '`', '!', '1', 'й', 'ф', 'я'},
        'Левый безымянный': {'"', '@', '2', 'ц', 'ы', 'ч'},
        'Левый средний': {'№', '#', '3', 'у', 'в', 'с'},
        'Левый указательный': {';', '$', '4', 'к', 'а', 'м', '%', '5', 'е', 'п', 'и'},
        'Большой палец': {' '},
        'Правый указательный': {':', '^', '6', 'н', 'р', 'т', '?', '&', '7', 'г', 'о', 'ь'},
        'Правый средний': {'*', '8', 'ш', 'л', 'б'},
        'Правый безымянный': {'(', '9', 'щ', 'д', 'ю'},
        'Правый мезинец': {')', '0', '_', '-', '+', '=', 'з', '[', '{', 'х', ']', '}', 'ъ', ':', 'Ж', ';', '"', 'э',
                           ',', '.', '?'},
    }
    layout_call = {
        'Левый мезинец': {'ю', 'ё', '%', '&', '$', 'б', 'ч', 'щ', 'ц'},
        'Левый безымянный': {'7', '[', 'ы', '<', ',', 'и', 'х'},
        'Левый средний': {'5', '{', 'о', '.', '>', 'е', 'э', 'й'},
        'Левый указательный': {'3', '}', '1', '(', 'у', 'ю', 'а', 'к', '<', '.', 'ь', ',', ';', '_'},
        'Большой палец': {' '},
        'Правый указательный': {'9', '=', '0', '*', '>', 'ё', '"', '^', '.', ':', 'н', 'щ', '?', 'э', 'р', 'ц'},
        'Правый средний': {'2', ')', 'д', 'т', 'м'},
        'Правый безымянный': {'4', '+', 'я', 'с', 'ф'},
        'Правый мезинец': {'6', ']', '8', '!', '#', 'щ', '№', 'г', 'ж', 'ц', '@', 'ъ', '|', 'в', '№', 'з', '-', 'п'},
    }
    layout_skoropis = {
        'Левый мезинец': {'*', '.', 'ц', 'у', 'ф'},
        'Левый безымянный': {'ё', 'ь', 'и', 'э'},
        'Левый средний': {'ъ', 'я', 'е', 'х'},
        'Левый указательный': {'?', '!', ',', '.', 'о', 'а', 'ы', 'ю'},
        'Большой палец': {' '},
        'Правый указательный': {'-', 'з', 'в', 'л', 'н', 'б', 'м'},
        'Правый средний': {'к', 'т', 'п'},
        'Правый безымянный': {'(', 'д', 'с', 'г'},
        'Правый мезинец': {'_', ')', '<', 'ч', 'ш', 'щ', '"', 'р', 'й', 'ж'},
    }
    presses_zubachev_1 = {key: 0 for key in layout_zubachev.keys()}
    presses_dictor_1 = {key: 0 for key in layout_dictor.keys()}
    presses_qwerty_1 = {key: 0 for key in layout_qwerty.keys()}
    presses_call_1 = {key: 0 for key in layout_call.keys()}
    presses_skoropis_1 = {key: 0 for key in layout_skoropis.keys()}
    for i in text1:
        i = i.lower()
        for finger, chars in layout_zubachev.items():
            if i in chars:
                presses_zubachev_1[finger] += 1
        for finger, chars in layout_dictor.items():
            if i in chars:
                presses_dictor_1[finger] += 1
        for finger, chars in layout_qwerty.items():
            if i in chars:
                presses_qwerty_1[finger] += 1
        for finger, chars in layout_call.items():
            if i in chars:
                presses_call_1[finger] += 1
        for finger, chars in layout_skoropis.items():
            if i in chars:
                presses_skoropis_1[finger] += 1
    max_zubachev_1 = max(presses_zubachev_1, key=presses_zubachev_1.get)
    max_dictor_1 = max(presses_dictor_1, key=presses_dictor_1.get)
    max_qwerty_1 = max(presses_qwerty_1, key=presses_qwerty_1.get)
    max_call_1 = max(presses_call_1, key=presses_call_1.get)
    max_skoropis_1 = max(presses_skoropis_1, key=presses_skoropis_1.get)
    print(
        f"Наибольшее нажатие в раскладке 'зубачев' произведении война и мир: {max_zubachev_1} - {presses_zubachev_1[max_zubachev_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'dictor' произведении война и мир: {max_dictor_1} - {presses_dictor_1[max_dictor_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'qwerty' произведении война и мир: {max_qwerty_1} - {presses_qwerty_1[max_qwerty_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'вызов' произведении война и мир: {max_call_1} - {presses_call_1[max_call_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'skoropis' произведении война и мир: {max_skoropis_1} - {presses_skoropis_1[max_skoropis_1]}")


def func2(text2):
    layout_zubachev = {
        'Левый мезинец': {'ё', '1', 'ф', 'г', 'ш'},
        'Левый безымянный': {'2', 'ы', 'и', 'ь', 'ъ'},
        'Левый средний': {'3', 'а', 'е', 'ю'},
        'Левый указательный': {'4', '5', 'я', ',', 'о', 'у', '.', 'э'},
        'Большой палец': {' '},
        'Правый указательный': {'6', '7', 'й', 'м', 'л', 'т', 'б', 'д'},
        'Правый средний': {'8', 'р', 'с', 'в'},
        'Правый безымянный': {'9', 'п', 'н', 'к'},
        'Правый мезинец': {'0', ')', '_', '-', '=', '+', 'х', 'ц', 'щ', '/', 'з', 'ж', 'ч'},
    }

    layout_dictor = {
        'Левый мезинец': {'ё', 'ц', '1', 'у', 'ф'},
        'Левый безымянный': {'2', 'ь', 'ъ', 'и', 'э'},
        'Левый средний': {'3', '№', 'я', 'е', 'х'},
        'Левый указательный': {'4', '%', ',', '?', 'о', 'ы', '5', ':', '.', '!', 'а', 'ю'},
        'Большой палец': {' '},
        'Правый указательный': {'6', ';', '7', '-', 'з', 'в', 'л', 'н', 'б', 'м'},
        'Правый средний': {'8', '"', 'к', 'т', 'п'},
        'Правый безымянный': {'9', '(', 'д', 'с', 'г'},
        'Правый мезинец': {'0', ')', '*', '_', '=', '+', 'ч', 'ш', 'щ', 'р', 'й', 'ж'},
    }
    layout_qwerty = {
        'Левый мезинец': {'ё', '`', '!', '1', 'й', 'ф', 'я'},
        'Левый безымянный': {'"', '@', '2', 'ц', 'ы', 'ч'},
        'Левый средний': {'№', '#', '3', 'у', 'в', 'с'},
        'Левый указательный': {';', '$', '4', 'к', 'а', 'м', '%', '5', 'е', 'п', 'и'},
        'Большой палец': {' '},
        'Правый указательный': {':', '^', '6', 'н', 'р', 'т', '?', '&', '7', 'г', 'о', 'ь'},
        'Правый средний': {'*', '8', 'ш', 'л', 'б'},
        'Правый безымянный': {'(', '9', 'щ', 'д', 'ю'},
        'Правый мезинец': {')', '0', '_', '-', '+', '=', 'з', '[', '{', 'х', ']', '}', 'ъ', ':', 'Ж', ';', '"', 'э',
                           ',', '.', '?'},
    }
    layout_call = {
        'Левый мезинец': {'ю', 'ё', '%', '&', '$', 'б', 'ч', 'щ', 'ц'},
        'Левый безымянный': {'7', '[', 'ы', '<', ',', 'и', 'х'},
        'Левый средний': {'5', '{', 'о', '.', '>', 'е', 'э', 'й'},
        'Левый указательный': {'3', '}', '1', '(', 'у', 'ю', 'а', 'к', '<', '.', 'ь', ',', ';', '_'},
        'Большой палец': {' '},
        'Правый указательный': {'9', '=', '0', '*', '>', 'ё', '"', '^', '.', ':', 'н', 'щ', '?', 'э', 'р', 'ц'},
        'Правый средний': {'2', ')', 'д', 'т', 'м'},
        'Правый безымянный': {'4', '+', 'я', 'с', 'ф'},
        'Правый мезинец': {'6', ']', '8', '!', '#', 'щ', '№', 'г', 'ж', 'ц', '@', 'ъ', '|', 'в', '№', 'з', '-', 'п'},
    }
    layout_skoropis = {
        'Левый мезинец': {'*', '.', 'ц', 'у', 'ф'},
        'Левый безымянный': {'ё', 'ь', 'и', 'э'},
        'Левый средний': {'ъ', 'я', 'е', 'х'},
        'Левый указательный': {'?', '!', ',', '.', 'о', 'а', 'ы', 'ю'},
        'Большой палец': {' '},
        'Правый указательный': {'-', 'з', 'в', 'л', 'н', 'б', 'м'},
        'Правый средний': {'к', 'т', 'п'},
        'Правый безымянный': {'(', 'д', 'с', 'г'},
        'Правый мезинец': {'_', ')', '<', 'ч', 'ш', 'щ', '"', 'р', 'й', 'ж'},
    }
    presses_zubachev_2 = {key: 0 for key in layout_zubachev.keys()}
    presses_dictor_2 = {key: 0 for key in layout_dictor.keys()}
    presses_qwerty_2 = {key: 0 for key in layout_qwerty.keys()}
    presses_call_2 = {key: 0 for key in layout_call.keys()}
    presses_skoropis_2 = {key: 0 for key in layout_skoropis.keys()}
    for i in text2:
        i = i.lower()
        for finger, chars in layout_zubachev.items():
            if i in chars:
                presses_zubachev_2[finger] += 1
        for finger, chars in layout_dictor.items():
            if i in chars:
                presses_dictor_2[finger] += 1
        for finger, chars in layout_qwerty.items():
            if i in chars:
                presses_qwerty_2[finger] += 1
        for finger, chars in layout_call.items():
            if i in chars:
                presses_call_2[finger] += 1
        for finger, chars in layout_skoropis.items():
            if i in chars:
                presses_skoropis_2[finger] += 1
    max_zubachev_2 = max(presses_zubachev_2, key=presses_zubachev_2.get)
    max_dictor_2 = max(presses_dictor_2, key=presses_dictor_2.get)
    max_qwerty_2 = max(presses_qwerty_2, key=presses_qwerty_2.get)
    max_call_2 = max(presses_call_2, key=presses_call_2.get)
    max_skoropis_2 = max(presses_skoropis_2, key=presses_skoropis_2.get)
    print(f"Наибольшее нажатие в раскладке 'зубачев' в 1grams: {max_zubachev_2} - {presses_zubachev_2[max_zubachev_2]}")
    print(f"Наибольшее нажатие в раскладке 'dictor' в 1grams: {max_dictor_2} - {presses_dictor_2[max_dictor_2]}")
    print(f"Наибольшее нажатие в раскладке 'qwerty' в 1grams: {max_qwerty_2} - {presses_qwerty_2[max_qwerty_2]}")
    print(f"Наибольшее нажатие в раскладке 'вызов' в 1grams: {max_call_2} - {presses_call_2[max_call_2]}")
    print(f"Наибольшее нажатие в раскладке 'skoropis' в 1grams: {max_skoropis_2} - {presses_skoropis_2[max_skoropis_2]}")

def func3(text1, text2):
    layout_zubachev = {
        'Левый мезинец': {'ё', '1', 'ф', 'г', 'ш'},
        'Левый безымянный': {'2', 'ы', 'и', 'ь', 'ъ'},
        'Левый средний': {'3', 'а', 'е', 'ю'},
        'Левый указательный': {'4', '5', 'я', ',', 'о', 'у', '.', 'э'},
        'Большой палец': {' '},
        'Правый указательный': {'6', '7', 'й', 'м', 'л', 'т', 'б', 'д'},
        'Правый средний': {'8', 'р', 'с', 'в'},
        'Правый безымянный': {'9', 'п', 'н', 'к'},
        'Правый мезинец': {'0', ')', '_', '-', '=', '+', 'х', 'ц', 'щ', '/', 'з', 'ж', 'ч'},
    }

    layout_dictor = {
        'Левый мезинец': {'ё', 'ц', '1', 'у', 'ф'},
        'Левый безымянный': {'2', 'ь', 'ъ', 'и', 'э'},
        'Левый средний': {'3', '№', 'я', 'е', 'х'},
        'Левый указательный': {'4', '%', ',', '?', 'о', 'ы', '5', ':', '.', '!', 'а', 'ю'},
        'Большой палец': {' '},
        'Правый указательный': {'6', ';', '7', '-', 'з', 'в', 'л', 'н', 'б', 'м'},
        'Правый средний': {'8', '"', 'к', 'т', 'п'},
        'Правый безымянный': {'9', '(', 'д', 'с', 'г'},
        'Правый мезинец': {'0', ')', '*', '_', '=', '+', 'ч', 'ш', 'щ', 'р', 'й', 'ж'},
    }
    layout_qwerty = {
        'Левый мезинец': {'ё', '`', '!', '1', 'й', 'ф', 'я'},
        'Левый безымянный': {'"', '@', '2', 'ц', 'ы', 'ч'},
        'Левый средний': {'№', '#', '3', 'у', 'в', 'с'},
        'Левый указательный': {';', '$', '4', 'к', 'а', 'м', '%', '5', 'е', 'п', 'и'},
        'Большой палец': {' '},
        'Правый указательный': {':', '^', '6', 'н', 'р', 'т', '?', '&', '7', 'г', 'о', 'ь'},
        'Правый средний': {'*', '8', 'ш', 'л', 'б'},
        'Правый безымянный': {'(', '9', 'щ', 'д', 'ю'},
        'Правый мезинец': {')', '0', '_', '-', '+', '=', 'з', '[', '{', 'х', ']', '}', 'ъ', ':', 'Ж', ';', '"', 'э',
                           ',', '.', '?'},
    }
    layout_call = {
        'Левый мезинец': {'ю', 'ё', '%', '&', '$', 'б', 'ч', 'щ', 'ц'},
        'Левый безымянный': {'7', '[', 'ы', '<', ',', 'и', 'х'},
        'Левый средний': {'5', '{', 'о', '.', '>', 'е', 'э', 'й'},
        'Левый указательный': {'3', '}', '1', '(', 'у', 'ю', 'а', 'к', '<', '.', 'ь', ',', ';', '_'},
        'Большой палец': {' '},
        'Правый указательный': {'9', '=', '0', '*', '>', 'ё', '"', '^', '.', ':', 'н', 'щ', '?', 'э', 'р', 'ц'},
        'Правый средний': {'2', ')', 'д', 'т', 'м'},
        'Правый безымянный': {'4', '+', 'я', 'с', 'ф'},
        'Правый мезинец': {'6', ']', '8', '!', '#', 'щ', '№', 'г', 'ж', 'ц', '@', 'ъ', '|', 'в', '№', 'з', '-', 'п'},
    }
    layout_skoropis = {
        'Левый мезинец': {'*', '.', 'ц', 'у', 'ф'},
        'Левый безымянный': {'ё', 'ь', 'и', 'э'},
        'Левый средний': {'ъ', 'я', 'е', 'х'},
        'Левый указательный': {'?', '!', ',', '.', 'о', 'а', 'ы', 'ю'},
        'Большой палец': {' '},
        'Правый указательный': {'-', 'з', 'в', 'л', 'н', 'б', 'м'},
        'Правый средний': {'к', 'т', 'п'},
        'Правый безымянный': {'(', 'д', 'с', 'г'},
        'Правый мезинец': {'_', ')', '<', 'ч', 'ш', 'щ', '"', 'р', 'й', 'ж'},
    }


    presses_zubachev_1 = {key: 0 for key in layout_zubachev.keys()}
    presses_dictor_1 = {key: 0 for key in layout_dictor.keys()}
    presses_qwerty_1 = {key: 0 for key in layout_qwerty.keys()}
    presses_call_1 = {key: 0 for key in layout_call.keys()}
    presses_skoropis_1 = {key: 0 for key in layout_skoropis.keys()}
    for i in text1:
        i = i.lower()
        for finger, chars in layout_zubachev.items():
            if i in chars:
                presses_zubachev_1[finger] += 1
        for finger, chars in layout_dictor.items():
            if i in chars:
                presses_dictor_1[finger] += 1
        for finger, chars in layout_qwerty.items():
            if i in chars:
                presses_qwerty_1[finger] += 1
        for finger, chars in layout_call.items():
            if i in chars:
                presses_call_1[finger] += 1
        for finger, chars in layout_skoropis.items():
            if i in chars:
                presses_skoropis_1[finger] += 1

    presses_zubachev_2 = {key: 0 for key in layout_zubachev.keys()}
    presses_dictor_2 = {key: 0 for key in layout_dictor.keys()}
    presses_qwerty_2 = {key: 0 for key in layout_qwerty.keys()}
    presses_call_2 = {key: 0 for key in layout_call.keys()}
    presses_skoropis_2 = {key: 0 for key in layout_skoropis.keys()}
    for i in text2:
        i = i.lower()
        for finger, chars in layout_zubachev.items():
            if i in chars:
                presses_zubachev_2[finger] += 1
        for finger, chars in layout_dictor.items():
            if i in chars:
                presses_dictor_2[finger] += 1
        for finger, chars in layout_qwerty.items():
            if i in chars:
                presses_qwerty_2[finger] += 1
        for finger, chars in layout_call.items():
            if i in chars:
                presses_call_2[finger] += 1
        for finger, chars in layout_skoropis.items():
            if i in chars:
                presses_skoropis_2[finger] += 1

    max_zubachev_1 = max(presses_zubachev_1, key=presses_zubachev_1.get)
    max_dictor_1 = max(presses_dictor_1, key=presses_dictor_1.get)
    max_qwerty_1 = max(presses_qwerty_1, key=presses_qwerty_1.get)
    max_call_1 = max(presses_call_1, key=presses_call_1.get)
    max_skoropis_1 = max(presses_skoropis_1, key=presses_skoropis_1.get)
    max_zubachev_2 = max(presses_zubachev_1, key=presses_zubachev_1.get)
    max_dictor_2 = max(presses_dictor_2, key=presses_dictor_2.get)
    max_qwerty_2 = max(presses_qwerty_2, key=presses_qwerty_2.get)
    max_call_2 = max(presses_call_2, key=presses_call_2.get)
    max_skoropis_2 = max(presses_skoropis_2, key=presses_skoropis_2.get)

    print(
        f"Наибольшее нажатие в раскладке 'зубачев' произведении война и мир: {max_zubachev_1} - {presses_zubachev_1[max_zubachev_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'dictor' произведении война и мир: {max_dictor_1} - {presses_dictor_1[max_dictor_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'qwerty' произведении война и мир: {max_qwerty_1} - {presses_qwerty_1[max_qwerty_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'вызов' произведении война и мир: {max_call_1} - {presses_call_1[max_call_1]}")
    print(
        f"Наибольшее нажатие в раскладке 'skoropis' произведении война и мир: {max_skoropis_1} - {presses_skoropis_1[max_skoropis_1]}")
    print()
    print(f"Наибольшее нажатие в раскладке 'зубачев' в 1grams: {max_zubachev_2} - {presses_zubachev_2[max_zubachev_2]}")
    print(f"Наибольшее нажатие в раскладке 'dictor' в 1grams: {max_dictor_2} - {presses_dictor_2[max_dictor_2]}")
    print(f"Наибольшее нажатие в раскладке 'qwerty' в 1grams: {max_qwerty_2} - {presses_qwerty_2[max_qwerty_2]}")
    print(f"Наибольшее нажатие в раскладке 'вызов' в 1grams: {max_call_2} - {presses_call_2[max_call_2]}")
    print(
        f"Наибольшее нажатие в раскладке 'skoropis' в 1grams: {max_skoropis_2} - {presses_skoropis_2[max_skoropis_2]}")

    total_presses_zubachev = {finger: presses_zubachev_1[finger] + presses_zubachev_2[finger] for finger in
                              layout_zubachev.keys()}
    total_presses_dictor = {finger: presses_dictor_1[finger] + presses_dictor_2[finger] for finger in
                            layout_dictor.keys()}
    total_presses_qwerty = {finger: presses_qwerty_1[finger] + presses_qwerty_2[finger] for finger in
                            layout_qwerty.keys()}
    total_presses_call = {finger: presses_call_1[finger] + presses_call_2[finger] for finger in layout_call.keys()}
    total_presses_skoropis = {finger: presses_skoropis_1[finger] + presses_skoropis_2[finger] for finger in
                              layout_skoropis.keys()}

    plt.figure(figsize=(12, 8))
    keys = list(presses_zubachev_1.keys())
    values_zubachev = list(total_presses_zubachev.values())
    values_dictor = list(total_presses_dictor.values())
    values_qwerty = list(total_presses_qwerty.values())
    values_call = list(total_presses_call.values())
    values_skoropis = list(total_presses_skoropis.values())

    bar_width = 0.15
    index = range(len(keys))

    plt.barh(index, values_zubachev, bar_width, color='skyblue', label='Зубачев - Война и мир')
    plt.barh([i + bar_width for i in index], values_dictor, bar_width, color='lightgreen', label='Dictor - Война и мир')
    plt.barh([i + 2 * bar_width for i in index], values_qwerty, bar_width, color='salmon', label='qwerty - Война и мир')
    plt.barh([i + 3 * bar_width for i in index], values_call, bar_width, color='black', label='вызов - Война и мир')
    plt.barh([i + 4 * bar_width for i in index], values_skoropis, bar_width, color='blue',
             label='skoropis - Война и мир')

    plt.yticks([i + bar_width / 2 for i in index], keys)
    plt.xlabel('Количество нажатий')
    plt.title('Количество нажатий по пальцам для текстов "20Мб" и "6Мб"')
    plt.legend()
    plt.tight_layout()

    plt.show()
