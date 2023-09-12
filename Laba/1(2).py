from random import randrange

# Создаем массивы
A = []
B = []
C = []

# Вводим размеры массивов
M = int(input('Введите размер массива A:'))
N = int(input('Введите размер массива B:'))

# Альтернатива с random
for i in range(M):
    elem = int(randrange(0, 100))
    A.append(elem)

print(*A)

for i in range(N):
    elem = int(randrange(0, 100))
    B.append(elem)

print(*B)
# Просматриваем состоят ли элементы из массива A в массиве B и добавляем в  массив C
for elem in A:
    if elem in B:
        C.append(elem)

# Вывод массива С
print(list(set(C)))
