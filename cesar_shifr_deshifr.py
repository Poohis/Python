# Программа шифрует/дешифрует введенную строку на английском или русском языках шифром Цезаря заданным ключом
def shifr_en(text, poz):
    en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    en_low = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    new_ind = 0
    for i in text:
        if i in en_up:
            new_ind = (en_up.find(i) + poz) % 26
            s+= en_up[new_ind]
        elif i in en_low:
            new_ind = (en_low.find(i) + poz) %26
            s+= en_low[new_ind]
        else: s += i
    return s

def deshifr_en(text, poz):
    en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    en_low = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    new_ind = 0
    for i in text:
        if i in en_up:
            new_ind = (en_up.find(i) - poz) % 26
            s+= en_up[new_ind]
        elif i in en_low:
            new_ind = (en_low.find(i) - poz) %26
            s+= en_low[new_ind]
        else: s += i
    return s

def shifr_ru(text, poz):
    en_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    s = ''
    new_ind = 0
    for i in text:
        if i in en_up:
            new_ind = (en_up.find(i) + poz) % 32
            s += en_up[new_ind]
        elif i in en_low:
            new_ind = (en_low.find(i) + poz) % 32
            s += en_low[new_ind]
        else: s += i
    return s
def deshifr_ru(text, poz):
    en_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    s = ''
    new_ind = 0
    for i in text:
        if i in en_up:
            new_ind = (en_up.find(i) - poz) % 32
            s += en_up[new_ind]
        elif i in en_low:
            new_ind = (en_low.find(i) - poz) % 32
            s += en_low[new_ind]
        else: s += i
    return s

lang = input('Какой язык(en или ru)?: ')
text = input('Введи строку: ')
todo = input('Что сделать(шифровать(shifr) или дешифровать(deshifr))?: ')
key = int(input('Введи ключ(величина сдвига): '))
if lang == 'en':
    if todo == 'deshifr':
        l = deshifr_en(text, key)
    else:
        l = shifr_en(text, key)
else:
    if todo == 'deshifr':
        l = deshifr_ru(text, key)
    else:
        l = shifr_ru(text, key)
print(l)