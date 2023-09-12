# Создаем массивы
A = []
B = []
C = []
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# Вводим размеры массивов
M = int(input('Введите размер массива A:'))
N = int(input('Введите размер массива B:'))

# Добавляем значения в мвссив A
for i in range(M):
    elem = int(input())
    A.append(elem)

# Добавляем значения в мвссив B
for i in range(N):
    elem = int(input())
    B.append(elem)

# Просматриваем состоят ли элементы из массива A в массиве B и добавляем в  массив C
for elem in A:
    if elem in B:
        C.append(elem)

# Вывод массива С
print(list(set(C)))
