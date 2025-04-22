# На вход программе подаются два натуральных числа a и b (a< b)
# находит натуральное число из отрезка [a,b] включительно с максимальной суммой делителей
a, b = int(input('Введи начало отрезка: ')), int(input('Введи конец отрезка: '))
mx = 0
num = 0
for i in range(a, b + 1):
    su = 0
    for j in range(1, i+1):
        if i % j == 0:
            su += j      
    if su > mx:
        mx = su
        num = i
    elif su == mx and i > num:
        num = i
print('Число: ', num, '  Сумма делителей числа: ', mx)