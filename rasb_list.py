# Программа принимает на вход список и число, задающее размер куска, а возвращает список из кусков указанной длины.
s = input('Введи список через пробел: ').split()
n = int(input('Введи размер куска: '))
def chunked(s, n):
    l, j, k = [[s[0]]], 0, 1
    for i in range(1,len(s)):
        if k < n:
            l[j].append(s[i])
            k += 1
        else:
            l.append([s[i]])
            j += 1
            k = 1
    return l
print(*chunked(s, n))