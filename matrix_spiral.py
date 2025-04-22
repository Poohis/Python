# На вход программе подаются два натуральных числа n и m.
# Программа создает матрицу размером n×m, заполняя ее "спиралью"
vvod = input('Введи количество строк(n) и столбцов(m) через пробел: ').split()
n =int(vvod[0])
m = int(vvod[1])
numbers=[i for i in range(1,n*m+1)]
matrix=[]
for i in range(n):
    matrix.append([0 for i in range(m)])
k = 0   # коэффициент уменьшения квадрата
while len(numbers)>0:
    for j in range(k,m-k):
        if len(numbers)>0:
            matrix[k][j]=numbers.pop(0)
    for j in range(1+k,n-k):
        if len(numbers)>0:
            matrix[j][m-k-1]=numbers.pop(0)
    for j in range(m-2-k,k-1,-1):
        if len(numbers)>0:
            matrix[n-k-1][j]=numbers.pop(0)
    for j in range(n-k-2,k,-1):
        if len(numbers)>0:
            matrix[j][k]=numbers.pop(0)
    k+=1
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).rjust(3),end=' ')
    print()