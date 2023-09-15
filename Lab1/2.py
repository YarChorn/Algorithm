# Создаем массивы
A = []
B = []
C = []

# Вводим размеры массивов
M = int(input('Введите размер массива A:'))
N = int(input('Введите размер массива B:'))

# Добавляем значения в массив A
for i in range(M):
    elem = int(input())
    A.append(elem)

# Добавляем значения в массив B
for i in range(N):
    elem = int(input())
    B.append(elem)

for elem in A:
    if elem in  B and elem not in C:
        C.append(elem)

set_A = set(A)
set_B = set(B)

C = list(set_A - set_B)

print(list(set(C)))

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# l = []
# for i in a:
#     if i not in b:
#         l.append(i)
# print(list(set(C)))
