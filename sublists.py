# выводит список, содержащий все возможные подсписки списка, полученного из введенной строки
list= [[]]
s = input('Введи строку: ').split()
for i in range(1,len(s)+1):
    j=0
    while (j+i)<=len(s):
        list.append(s[j:j+i])
        j+=1
print(list)