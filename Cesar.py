# На вход программе подаётся строка текста на английском языке
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова)
# Строчные буквы при этом остаются строчными, а прописные – прописными.
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
text=input('Введи строку: ').split()
s=[]
for i in text:
    m = ''
    for k in i:
        if k.isalpha():
            m += k 
    s.append(shifr_en(i, len(m)))
l=' '.join(s)
print(l)
