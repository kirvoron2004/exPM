import matplotlib.pyplot as plt
import codecs
import itertools
import re


layout_zubachev = {
    'Левый мизинец': {'ё', '1', 'ф', 'г', 'ш'},
    'Левый безымянный': {'2', 'ы', 'и', 'ь', 'ъ'},
    'Левый средний': {'3', 'а', 'е', 'ю'},
    'Левый указательный': {'4', '5', 'я', ',', 'о', 'у', '.', 'э'},
    'Большой палец': {' '},
    'Правый указательный': {'6', '7', 'й', 'м', 'л', 'т', 'б', 'д'},
    'Правый средний': {'8', 'р', 'с', 'в'},
    'Правый безымянный': {'9', 'п', 'н', 'к'},
    'Правый мизинец': {'0', ')', '_', '-', '=', '+', 'х', 'ц', 'щ', '/', 'з', 'ж', 'ч'},
}

layout_dictor = {
    'Левый мизинец': {'ё', 'ц', '1', 'у', 'ф'},
    'Левый безымянный': {'2', 'ь', 'ъ', 'и', 'э'},
    'Левый средний': {'3', '№', 'я', 'е', 'х'},
    'Левый указательный': {'4', '%', ',', '?', 'о', 'ы', '5', ':', '.', '!', 'а', 'ю'},
    'Большой палец': {' '},
    'Правый указательный': {'6', ';', '7', '-', 'з', 'в', 'л', 'н', 'б', 'м'},
    'Правый средний': {'8', '"', 'к', 'т', 'п'},
    'Правый безымянный': {'9', '(', 'д', 'с', 'г'},
    'Правый мизинец': {'0', ')', '*', '_', '=', '+' , 'ч', 'ш', 'щ', 'р', 'й', 'ж'},
}
layout_qwerty = {
    'Левый мизинец': {'ё', '`', '!', '1', 'й', 'ф', 'я'},
    'Левый безымянный': {'"', '@', '2', 'ц', 'ы', 'ч'},
    'Левый средний': {'№', '#', '3', 'у', 'в', 'с'},
    'Левый указательный': {';', '$', '4', 'к', 'а', 'м', '%', '5', 'е', 'п', 'и'},
    'Большой палец': {' '},
    'Правый указательный': {':', '^', '6', 'н', 'р', 'т', '?', '&', '7', 'г', 'о', 'ь'},
    'Правый средний': {'*', '8', 'ш', 'л', 'б'},
    'Правый безымянный': {'(', '9', 'щ', 'д', 'ю'},
    'Правый мизинец': {')', '0', '_', '-', '+', '=' , 'з', '[', '{', 'х', ']', '}','ъ',':' ,'Ж' ,';','"','э',',','.','?'},
}
layout_call = {
    'Левый мизинец': {'ю', 'ё', '%', '&', '$', 'б','ч' ,'щ', 'ц'},
    'Левый безымянный': {'7', '[', 'ы', '<', ',', 'и', 'х'},
    'Левый средний': {'5', '{', 'о', '.','>','е','э','й'},
    'Левый указательный': {'3', '}', '1', '(', 'у', 'ю', 'а', 'к', '<', '.','ь',',',';','_'},
    'Большой палец': {' '},
    'Правый указательный': {'9', '=', '0', '*', '>', 'ё', '"', '^', '.', ':','н','щ','?','э','р','ц'},
    'Правый средний': {'2', ')', 'д', 'т', 'м'},
    'Правый безымянный': {'4', '+', 'я', 'с', 'ф'},
    'Правый мизинец': {'6', ']', '8', '!', '#', 'щ' , '№', 'г', 'ж', 'ц', '@', 'ъ','|', 'в','№','з','-','п'},
}

def calculate_penalty_for_text(text, layout):
    penalties = {key: 0 for key in layout.keys()}
    for char in text.lower():
        for finger, chars in layout.items():
            if char in chars:
                index = list(chars).index(char)
                if finger in ['Левый мизинец', 'Правый мизинец']:
                    penalties[finger] += abs(index - 2)
                elif finger in ['Левый безымянный', 'Левый средний', 'Правый средний', 'Правый безымянный']:
                    penalties[finger] += abs(index - 2)
                elif finger in ['Левый указательный', 'Правый указательный']:
                    penalties[finger] += abs(index - 2 - 4 * (index // 4)) + (index // 4)


    return penalties

# Чтение файлов
fileObj1 = codecs.open("C:/Users/makar/Desktop/travov/pythonProject/voina_i_mir.txt", "r", "utf_8_sig")
text1 = fileObj1.read()
fileObj1.close()
fileObj2 = codecs.open("C:/Users/makar/Desktop/travov/pythonProject/1grams.txt", "r", "utf_8_sig")
text2 = fileObj2.read()
fileObj2.close()

# Подсчет нажатий
presses_zubachev_1 = {key: 0 for key in layout_zubachev.keys()}
presses_dictor_1 = {key: 0 for key in layout_dictor.keys()}
presses_qwerty_1 = {key: 0 for key in layout_qwerty.keys()}
presses_call_1 = {key: 0 for key in layout_call.keys()}


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


presses_zubachev_2 = {key: 0 for key in layout_zubachev.keys()}
presses_dictor_2 = {key: 0 for key in layout_dictor.keys()}
presses_qwerty_2 = {key: 0 for key in layout_qwerty.keys()}
presses_call_2 = {key: 0 for key in layout_call.keys()}

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


# Вычисление штрафов
penalties_zubachev_1 = calculate_penalty_for_text(text1, layout_zubachev)
penalties_dictor_1 = calculate_penalty_for_text(text1, layout_dictor)
penalties_qwerty_1 = calculate_penalty_for_text(text1, layout_qwerty)
penalties_call_1 = calculate_penalty_for_text(text1, layout_call)


penalties_zubachev_2 = calculate_penalty_for_text(text2, layout_zubachev)
penalties_dictor_2 = calculate_penalty_for_text(text2, layout_dictor)
penalties_qwerty_2 = calculate_penalty_for_text(text2, layout_qwerty)
penalties_call_2 = calculate_penalty_for_text(text2, layout_call)


# Суммарные нажатия
total_presses_zubachev = {finger: presses_zubachev_1[finger] + presses_zubachev_2[finger] for finger in layout_zubachev.keys()}
total_presses_dictor = {finger: presses_dictor_1[finger] + presses_dictor_2[finger] for finger in layout_dictor.keys()}
total_presses_qwerty = {finger: presses_qwerty_1[finger] + presses_qwerty_2[finger] for finger in layout_qwerty.keys()}
total_presses_call = {finger: presses_call_1[finger] + presses_call_2[finger] for finger in layout_call.keys()}


# Вывод нажатий и штрафов

print("Штрафы для текст 1 (Зубачев):", penalties_zubachev_1)
print("Штрафы для текст 1 (Dictor):", penalties_dictor_1)
print("Штрафы для текст 1 (qwerty):", penalties_qwerty_1)
print("Штрафы для текст 1 (call):", penalties_call_1)

print()
print("Штрафы для текст 2 (Зубачев):", penalties_zubachev_2)
print("Штрафы для текст 2 (Dictor):", penalties_dictor_2)
print("Штрафы для текст 2 (qwerty):", penalties_qwerty_2)
print("Штрафы для текст 2 (call):", penalties_call_2)

print()
print("Нажатия для текст 1 (Зубачев):", presses_zubachev_1)
print("Нажатия для текст 1 (Dictor):", presses_dictor_1)
print("Нажатия для текст 1 (qwerty):", presses_qwerty_1)
print("Нажатия для текст 1 (call):", presses_call_1)

print()
print("Нажатия для текст 2 (Зубачев):", presses_zubachev_2)
print("Нажатия для текст 2 (Dictor):", presses_dictor_2)
print("Нажатия для текст 2 (qwerty):", presses_qwerty_2)
print("Нажатия для текст 2 (call):", presses_call_2)

def funcc(a, b):
    for k, v in a.items():
        if b in a[k]:
            return k

def fun(a, b):
    x = list(a.values())
    for i in x:
        if b in i:
            return True

# Чтение файла и определение букв
x = open('44.txt', 'r', encoding='utf-8')
sss = str(x.readlines())
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

rs_qwerty = ['н', 'р', 'т', 'г', 'о', 'ь', 'ш', 'л', 'б', 'щ', 'д', 'ю', 'з', 'х','ъ','Ж' ,'э']
ls_qwerty = ['ё', 'й', 'ф', 'я', 'ц', 'ы', 'ч', 'у', 'в', 'с','к', 'а', 'м', 'е', 'п', 'и']
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

rs_call = ['ё','н','щ','э','р','ц', 'д', 'т', 'м', 'я', 'с', 'ф', 'щ' , 'г', 'ж', 'ц', 'ъ', 'в','з','п']
ls_call = ['ю', 'ё', 'б','ч' ,'щ', 'ц', 'ы', 'и', 'х', 'о','е','э','й', 'у', 'ю', 'а', 'к','ь']
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
############################
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
x = open('1grams-3.txt','r', encoding='utf-8')
sss=x.readlines()
sss1 = set(sss)
#зубачев

zc_l1=0
zc_r1=0
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_zubachev_l,i[0].lower()) and fun(layout_zubachev_l,i[1].lower()):
                if funcc(layout_zubachev_l, i[0].lower()) > funcc(layout_zubachev_l, i[1].lower()):
                    zc_l1+=1
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_zubachev_r,i[0].lower()) and fun(layout_zubachev_r,i[1].lower()):
                if funcc(layout_zubachev_r, i[0].lower()) > funcc(layout_zubachev_r, i[1].lower()):
                    zc_r1+=1
print(f"Зубачев: 2сочетание для левой руки {zc_l1}")
print(f"Зубачев: 2сочетание для правой руки {zc_r1}")

zc_l2=0
zc_r2 = 0
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_zubachev_l,i[0].lower()) and fun(layout_zubachev_l,i[1].lower()) and fun(layout_zubachev_l,i[2].lower()):
                if funcc(layout_zubachev_l, i[0].lower()) > funcc(layout_zubachev_l, i[1].lower()) and funcc(layout_zubachev_l, i[0].lower()) > funcc(layout_zubachev_l, i[2].lower()) and funcc(layout_zubachev_l, i[1].lower()) > funcc(layout_zubachev_l, i[2].lower()):
                    zc_l2+=1
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_zubachev_r,i[0].lower()) and fun(layout_zubachev_r,i[1].lower()) and fun(layout_zubachev_r,i[2].lower()):
                if (funcc(layout_zubachev_r, i[0].lower()) > funcc(layout_zubachev_r, i[1].lower())) and (funcc(layout_zubachev_r, i[0].lower()) > funcc(layout_zubachev_r, i[2].lower())) and (funcc(layout_zubachev_r, i[1].lower()) > funcc(layout_zubachev_r, i[2].lower())):
                    zc_r2+=1
print(f"Зубачев: 3сочетание для левой руки {zc_l2}")
print(f"Зубачев: 3сочетание для правой руки {zc_r2}")

#dictor

dc_l1=0
dc_r1=0
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_dictor_l,i[0].lower()) and fun(layout_dictor_l,i[1].lower()):
                if funcc(layout_dictor_l, i[0].lower()) > funcc(layout_dictor_l, i[1].lower()):
                    dc_l1+=1
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_dictor_r,i[0].lower()) and fun(layout_dictor_r,i[1].lower()):
                if funcc(layout_dictor_r, i[0].lower()) > funcc(layout_dictor_r, i[1].lower()):
                    dc_r1+=1
print(f"Диктор: 2сочетание для левой руки {dc_l1}")
print(f"Диктор: 2сочетание для правой руки {dc_r1}")

dc_l2=0
dc_r2 = 0
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_dictor_l,i[0].lower()) and fun(layout_dictor_l,i[1].lower()) and fun(layout_dictor_l,i[2].lower()):
                if funcc(layout_dictor_l, i[0].lower()) > funcc(layout_dictor_l, i[1].lower()) and funcc(layout_dictor_l, i[0].lower()) > funcc(layout_dictor_l, i[2].lower()) and funcc(layout_dictor_l, i[1].lower()) > funcc(layout_dictor_l, i[2].lower()):
                    dc_l2+=1
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_dictor_r,i[0].lower()) and fun(layout_dictor_r,i[1].lower()) and fun(layout_dictor_r,i[2].lower()):
                if (funcc(layout_dictor_r, i[0].lower()) > funcc(layout_dictor_r, i[1].lower())) and (funcc(layout_dictor_r, i[0].lower()) > funcc(layout_dictor_r, i[2].lower())) and (funcc(layout_dictor_r, i[1].lower()) > funcc(layout_dictor_r, i[2].lower())):
                    dc_r2+=1
print(f"Диктор: 3сочетание для левой руки {dc_l2}")
print(f"Диктор: 3сочетание для правой руки {dc_r2}")

#йцукен

qc_l1=0
qc_r1=0
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_qwerty_l,i[0].lower()) and fun(layout_qwerty_l,i[1].lower()):
                if funcc(layout_qwerty_l, i[0].lower()) > funcc(layout_qwerty_l, i[1].lower()):
                    qc_l1+=1
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_qwerty_r,i[0].lower()) and fun(layout_qwerty_r,i[1].lower()):
                if funcc(layout_qwerty_r, i[0].lower()) > funcc(layout_qwerty_r, i[1].lower()):
                    qc_r1+=1
print(f"Йцукен: 2сочетание для левой руки {qc_l1}")
print(f"Йцукен: 2сочетание для правой руки {qc_r1}")

qc_l2=0
qc_r2 = 0
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_qwerty_l,i[0].lower()) and fun(layout_qwerty_l,i[1].lower()) and fun(layout_qwerty_l,i[2].lower()):
                if funcc(layout_qwerty_l, i[0].lower()) > funcc(layout_qwerty_l, i[1].lower()) and funcc(layout_qwerty_l, i[0].lower()) > funcc(layout_qwerty_l, i[2].lower()) and funcc(layout_qwerty_l, i[1].lower()) > funcc(layout_qwerty_l, i[2].lower()):
                    qc_l2+=1
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_qwerty_r,i[0].lower()) and fun(layout_qwerty_r,i[1].lower()) and fun(layout_qwerty_r,i[2].lower()):
                if (funcc(layout_qwerty_r, i[0].lower()) > funcc(layout_qwerty_r, i[1].lower())) and (funcc(layout_qwerty_r, i[0].lower()) > funcc(layout_qwerty_r, i[2].lower())) and (funcc(layout_qwerty_r, i[1].lower()) > funcc(layout_qwerty_r, i[2].lower())):
                    qc_r2+=1
print(f"Йцукен: 3сочетание для левой руки {qc_l2}")
print(f"Йцукен: 3сочетание для правой руки {qc_r2}")
#вызов

vc_l1=0
vc_r1=0
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_call_l,i[0].lower()) and fun(layout_call_l,i[1].lower()):
                if funcc(layout_call_l, i[0].lower()) > funcc(layout_call_l, i[1].lower()):
                    vc_l1+=1
for i in sss1:
    if len(i[:-1])==2:
        if not(isint(i)):
            if fun(layout_call_r,i[0].lower()) and fun(layout_call_r,i[1].lower()):
                if funcc(layout_call_r, i[0].lower()) > funcc(layout_call_r, i[1].lower()):
                    vc_r1+=1
print(f"Вызов: 2сочетание для левой руки {vc_l1}")
print(f"Вызов: 2сочетание для правой руки {vc_r1}")

vc_l2=0
vc_r2 = 0
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_call_l,i[0].lower()) and fun(layout_call_l,i[1].lower()) and fun(layout_call_l,i[2].lower()):
                if funcc(layout_call_l, i[0].lower()) > funcc(layout_call_l, i[1].lower()) and funcc(layout_call_l, i[0].lower()) > funcc(layout_call_l, i[2].lower()) and funcc(layout_call_l, i[1].lower()) > funcc(layout_call_l, i[2].lower()):
                    vc_l2+=1
for i in sss1:
    if len(i[:-1])==3:
        if not(isint(i)):
            if fun(layout_call_r,i[0].lower()) and fun(layout_call_r,i[1].lower()) and fun(layout_call_r,i[2].lower()):
                if (funcc(layout_call_r, i[0].lower()) > funcc(layout_call_r, i[1].lower())) and (funcc(layout_call_r, i[0].lower()) > funcc(layout_call_r, i[2].lower())) and (funcc(layout_call_r, i[1].lower()) > funcc(layout_call_r, i[2].lower())):
                    vc_r2+=1
print(f"Вызов: 3сочетание для левой руки {vc_l2}")
print(f"Вызов: 3сочетание для правой руки {vc_r2}")


# Построение гистограммы 1 лаба (подсчет нажатий)
plt.figure(figsize=(12, 8))
keys = list(presses_zubachev_1.keys())
values_zubachev = list(total_presses_zubachev.values())
values_dictor = list(total_presses_dictor.values())
values_qwerty = list(total_presses_qwerty.values())
values_call = list(total_presses_call.values())


bar_width = 0.15
index = range(len(keys))

plt.barh(index, values_zubachev, bar_width, color='skyblue', label='Зубачев - Война и мир')
plt.barh([i + bar_width for i in index], values_dictor, bar_width, color='lightgreen', label='Dictor - Война и мир')
plt.barh([i + 2 * bar_width for i in index], values_qwerty, bar_width, color='salmon', label='qwerty - Война и мир')
plt.barh([i + 3 * bar_width for i in index], values_call, bar_width, color='black', label='вызов - Война и мир')


plt.yticks([i + bar_width / 2 for i in index], keys)
plt.xlabel('Количество нажатий')
plt.title('Количество нажатий по пальцам для текстов "20Мб" и "6Мб"')
plt.legend()
plt.tight_layout()
#отображение первого графика
plt.show()

# Построение гистограммы 3 лаба (штрафы)
plt.figure(figsize=(12, 8))
penalties_values_zubachev = [penalties_zubachev_1[finger] + penalties_zubachev_2[finger] for finger in keys]
penalties_values_dictor = [penalties_dictor_1[finger] + penalties_dictor_2[finger] for finger in keys]
penalties_values_qwerty = [penalties_qwerty_1[finger] + penalties_qwerty_2[finger] for finger in keys]
penalties_values_call = [penalties_call_1[finger] + penalties_call_2[finger] for finger in keys]


plt.barh(index, penalties_values_zubachev, bar_width, color='skyblue', label='Зубачев - Штрафы')
plt.barh([i + bar_width for i in index], penalties_values_dictor, bar_width, color='lightgreen', label='Dictor - Штрафы')
plt.barh([i + 2 * bar_width for i in index], penalties_values_qwerty, bar_width, color='salmon', label='qwerty - Штрафы')
plt.barh([i + 3 * bar_width for i in index], penalties_values_call, bar_width, color='black', label='вызов - Штрафы')

plt.yticks([i for i in index], keys)
plt.xlabel('Суммарный штраф')
plt.title('Суммарные штрафы по пальцам')
plt.legend()
plt.tight_layout()

# Отображение второго графика
plt.show()

# Построение гистограммы 4 лаба
labels = ['call (Правая)', 'call (Левая)', 'qwerty (Правая)', 'qwerty (Левая)','Dictor (Правая)', 'Dictor (Левая)','Зубачев (Правая)' ,'Зубачев (Левая)' ]
convenient_counts = [c_l_zubachev, c_r_zubachev, c_l_dictor, c_r_dictor, c_l_qwerty, c_r_qwerty, c_l_call, c_r_call]
total_counts = [total_l_zubachev, total_r_zubachev, total_l_dictor, total_r_dictor, total_l_qwerty, total_r_qwerty, total_l_call, total_r_call]

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

# Построение гистограммы 5 лаба
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
convenient_counts = [zc_l1, zc_r1, zc_l2, zc_r2, dc_l1, dc_r1, dc_l2, dc_r2, qc_l1, qc_r1,qc_l2,qc_r2,vc_l1,vc_r1,vc_l2,vc_r2]
# total_counts будет содержать одинаковые значения в этом случае


x = range(len(labels))

plt.barh(x, convenient_counts, color=['blue', 'blue', 'salmon', 'salmon','blue', 'blue','salmon', 'salmon','blue', 'blue','salmon', 'salmon','blue', 'blue','salmon', 'salmon'],label='Удобные сочетания')
plt.yticks(x, labels)
plt.xlabel('Количество сочетаний')
plt.title('Триграммы и Диграммы')
plt.legend()

# Добавление числовых значений справа от каждого столбца
for i, convenient in enumerate(convenient_counts):
    plt.text(convenient + 0.5, i, str(convenient), va='center', color='blue')

plt.show()