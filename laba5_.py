import matplotlib.pyplot as plt
def isint(a):
    try:
        for i in a:
            if int(i) or int(i) ==0:
                return True
    except ValueError:
        return False

def funcc(a,b):
    for k, v in a.items():
        if b in a[k]:
            return k
def fun(a,b):
    x = list(a.values())
    for i in x:
        if b in i:
            return True

def funcc1(s):
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
    sss = s
    sss1 = set(sss)
    # зубачев

    zc_l1 = 0
    zc_r1 = 0
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_zubachev_l, i[0].lower()) and fun(layout_zubachev_l, i[1].lower()):
                    if funcc(layout_zubachev_l, i[0].lower()) > funcc(layout_zubachev_l, i[1].lower()):
                        zc_l1 += 1
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_zubachev_r, i[0].lower()) and fun(layout_zubachev_r, i[1].lower()):
                    if funcc(layout_zubachev_r, i[0].lower()) > funcc(layout_zubachev_r, i[1].lower()):
                        zc_r1 += 1
    print(f"Зубачев: 2сочетание для левой руки {zc_l1}")
    print(f"Зубачев: 2сочетание для правой руки {zc_r1}")

    zc_l2 = 0
    zc_r2 = 0
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_zubachev_l, i[0].lower()) and fun(layout_zubachev_l, i[1].lower()) and fun(
                        layout_zubachev_l, i[2].lower()):
                    if funcc(layout_zubachev_l, i[0].lower()) > funcc(layout_zubachev_l, i[1].lower()) and funcc(
                            layout_zubachev_l, i[0].lower()) > funcc(layout_zubachev_l, i[2].lower()) and funcc(
                            layout_zubachev_l, i[1].lower()) > funcc(layout_zubachev_l, i[2].lower()):
                        zc_l2 += 1
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_zubachev_r, i[0].lower()) and fun(layout_zubachev_r, i[1].lower()) and fun(
                        layout_zubachev_r, i[2].lower()):
                    if (funcc(layout_zubachev_r, i[0].lower()) > funcc(layout_zubachev_r, i[1].lower())) and (
                            funcc(layout_zubachev_r, i[0].lower()) > funcc(layout_zubachev_r, i[2].lower())) and (
                            funcc(layout_zubachev_r, i[1].lower()) > funcc(layout_zubachev_r, i[2].lower())):
                        zc_r2 += 1
    print(f"Зубачев: 3сочетание для левой руки {zc_l2}")
    print(f"Зубачев: 3сочетание для правой руки {zc_r2}")

    # dictor

    dc_l1 = 0
    dc_r1 = 0
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_dictor_l, i[0].lower()) and fun(layout_dictor_l, i[1].lower()):
                    if funcc(layout_dictor_l, i[0].lower()) > funcc(layout_dictor_l, i[1].lower()):
                        dc_l1 += 1
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_dictor_r, i[0].lower()) and fun(layout_dictor_r, i[1].lower()):
                    if funcc(layout_dictor_r, i[0].lower()) > funcc(layout_dictor_r, i[1].lower()):
                        dc_r1 += 1
    print(f"Диктор: 2сочетание для левой руки {dc_l1}")
    print(f"Диктор: 2сочетание для правой руки {dc_r1}")

    dc_l2 = 0
    dc_r2 = 0
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_dictor_l, i[0].lower()) and fun(layout_dictor_l, i[1].lower()) and fun(layout_dictor_l,
                                                                                                     i[2].lower()):
                    if funcc(layout_dictor_l, i[0].lower()) > funcc(layout_dictor_l, i[1].lower()) and funcc(
                            layout_dictor_l, i[0].lower()) > funcc(layout_dictor_l, i[2].lower()) and funcc(
                            layout_dictor_l, i[1].lower()) > funcc(layout_dictor_l, i[2].lower()):
                        dc_l2 += 1
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_dictor_r, i[0].lower()) and fun(layout_dictor_r, i[1].lower()) and fun(layout_dictor_r,
                                                                                                     i[2].lower()):
                    if (funcc(layout_dictor_r, i[0].lower()) > funcc(layout_dictor_r, i[1].lower())) and (
                            funcc(layout_dictor_r, i[0].lower()) > funcc(layout_dictor_r, i[2].lower())) and (
                            funcc(layout_dictor_r, i[1].lower()) > funcc(layout_dictor_r, i[2].lower())):
                        dc_r2 += 1
    print(f"Диктор: 3сочетание для левой руки {dc_l2}")
    print(f"Диктор: 3сочетание для правой руки {dc_r2}")

    # йцукен

    qc_l1 = 0
    qc_r1 = 0
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_qwerty_l, i[0].lower()) and fun(layout_qwerty_l, i[1].lower()):
                    if funcc(layout_qwerty_l, i[0].lower()) > funcc(layout_qwerty_l, i[1].lower()):
                        qc_l1 += 1
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_qwerty_r, i[0].lower()) and fun(layout_qwerty_r, i[1].lower()):
                    if funcc(layout_qwerty_r, i[0].lower()) > funcc(layout_qwerty_r, i[1].lower()):
                        qc_r1 += 1
    print(f"Йцукен: 2сочетание для левой руки {qc_l1}")
    print(f"Йцукен: 2сочетание для правой руки {qc_r1}")

    qc_l2 = 0
    qc_r2 = 0
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_qwerty_l, i[0].lower()) and fun(layout_qwerty_l, i[1].lower()) and fun(layout_qwerty_l,
                                                                                                     i[2].lower()):
                    if funcc(layout_qwerty_l, i[0].lower()) > funcc(layout_qwerty_l, i[1].lower()) and funcc(
                            layout_qwerty_l, i[0].lower()) > funcc(layout_qwerty_l, i[2].lower()) and funcc(
                            layout_qwerty_l, i[1].lower()) > funcc(layout_qwerty_l, i[2].lower()):
                        qc_l2 += 1
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_qwerty_r, i[0].lower()) and fun(layout_qwerty_r, i[1].lower()) and fun(layout_qwerty_r,
                                                                                                     i[2].lower()):
                    if (funcc(layout_qwerty_r, i[0].lower()) > funcc(layout_qwerty_r, i[1].lower())) and (
                            funcc(layout_qwerty_r, i[0].lower()) > funcc(layout_qwerty_r, i[2].lower())) and (
                            funcc(layout_qwerty_r, i[1].lower()) > funcc(layout_qwerty_r, i[2].lower())):
                        qc_r2 += 1
    print(f"Йцукен: 3сочетание для левой руки {qc_l2}")
    print(f"Йцукен: 3сочетание для правой руки {qc_r2}")
    # вызов

    vc_l1 = 0
    vc_r1 = 0
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_call_l, i[0].lower()) and fun(layout_call_l, i[1].lower()):
                    if funcc(layout_call_l, i[0].lower()) > funcc(layout_call_l, i[1].lower()):
                        vc_l1 += 1
    for i in sss1:
        if len(i[:-1]) == 2:
            if not (isint(i)):
                if fun(layout_call_r, i[0].lower()) and fun(layout_call_r, i[1].lower()):
                    if funcc(layout_call_r, i[0].lower()) > funcc(layout_call_r, i[1].lower()):
                        vc_r1 += 1
    print(f"Вызов: 2сочетание для левой руки {vc_l1}")
    print(f"Вызов: 2сочетание для правой руки {vc_r1}")

    vc_l2 = 0
    vc_r2 = 0
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_call_l, i[0].lower()) and fun(layout_call_l, i[1].lower()) and fun(layout_call_l,
                                                                                                 i[2].lower()):
                    if funcc(layout_call_l, i[0].lower()) > funcc(layout_call_l, i[1].lower()) and funcc(layout_call_l,
                                                                                                         i[
                                                                                                             0].lower()) > funcc(
                            layout_call_l, i[2].lower()) and funcc(layout_call_l, i[1].lower()) > funcc(layout_call_l,
                                                                                                        i[2].lower()):
                        vc_l2 += 1
    for i in sss1:
        if len(i[:-1]) == 3:
            if not (isint(i)):
                if fun(layout_call_r, i[0].lower()) and fun(layout_call_r, i[1].lower()) and fun(layout_call_r,
                                                                                                 i[2].lower()):
                    if (funcc(layout_call_r, i[0].lower()) > funcc(layout_call_r, i[1].lower())) and (
                            funcc(layout_call_r, i[0].lower()) > funcc(layout_call_r, i[2].lower())) and (
                            funcc(layout_call_r, i[1].lower()) > funcc(layout_call_r, i[2].lower())):
                        vc_r2 += 1
    print(f"Вызов: 3сочетание для левой руки {vc_l2}")
    print(f"Вызов: 3сочетание для правой руки {vc_r2}")
    labels = [
        '3 Сочетания (Правая) вызов', '3 Сочетания (Левая) вызов',
        '2 Сочетания (Правая вызов', '2 Сочетания (Левая) вызов',
        '3 Сочетания (Правая) йцукен', '3 Сочетания (Левая) йцукен',
        '2 Сочетания (Правая) йцукен', '2 Сочетания (Левая) йцукен',
        '3 Сочетания (Правая) Диктор', '3 Сочетания (Левая) Диктор',
        '2 Сочетания (Правая) Диктор', '2 Сочетания (Левая) Диктор',
        '3 Сочетания (Правая) Зубачев', '3 Сочетания (Левая) Зубачев',
        '2 Сочетания (Правая) Зубачев', '2 Сочетания (Левая) Зубачев',
    ]
    convenient_counts = [zc_l1, zc_r1, zc_l2, zc_r2, dc_l1, dc_r1, dc_l2, dc_r2, qc_l1, qc_r1, qc_l2, qc_r2, vc_l1,
                         vc_r1, vc_l2, vc_r2]
    # total_counts будет содержать одинаковые значения в этом случае

    x = range(len(labels))

    plt.barh(x, convenient_counts,
             color=['blue', 'blue', 'salmon', 'salmon', 'blue', 'blue', 'salmon', 'salmon', 'blue', 'blue', 'salmon',
                    'salmon', 'blue', 'blue', 'salmon', 'salmon'], label='Удобные сочетания')
    plt.yticks(x, labels)
    plt.xlabel('Количество сочетаний')
    plt.title('Триграммы и Диграммы')
    plt.legend()

    # Добавление числовых значений справа от каждого столбца
    for i, convenient in enumerate(convenient_counts):
        plt.text(convenient + 0.5, i, str(convenient), va='center', color='blue')

    plt.show()