# Создаем массивы
A = []
B = []
C = []
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# Вводим размеры массивов
M = int(input('Введите размер массива A:'))
N = int(input('Введите размер массива B:'))

# Добавляем значения в массив A
for i in range(M):
    elem = int(input())
    A.append(elem)

# Добавляем значения в мвссив B
for i in range(N):
    elem = int(input())
    B.append(elem)

# Просматриваем состоят ли элементы из массива A в массиве B и добавляем в  массив C
for elem in A:
    if elem in B and elem not in C:
        C.append(elem)

for elem in B:
    if elem in A and elem not in C:
        C.append(elem)
# not in C помогает проверить значения в массиве С на повторяющиеся элементы

# Вывод массива С
# Преобразование исходного списка в множество (set) автоматически удаляет все дубликаты элементов, так как множество не может содержать повторяющиеся элементы.
print(list(set(C)))
