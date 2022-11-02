#Даны два числа n и m. Создай двумерный массив размером n×m
# и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.

n = int(input())
m = int(input())
a = []
for x in range(n):
    a.append(['.' * m])
    for w in range(n):
        if (((x == 0) or (x%2 == 0)) and w%2 == 0) or ((x % 2 != 0) and (w%2 == 0)):
            a[x][w] = '*'
for e in a:
    print((' '.join(e)))
