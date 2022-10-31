#Даны два числа n и m. Создай двумерный массив размером n×m
# и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.

n = int(input())
m = int(input())
a = []
for x in range(m):
    a.append(['*']*n)
for w in a:
    for o in w:
        #if a.index(o)/2 == 0:
            print(w.index(o))
for e in a:
    print((' '.join(e)))
