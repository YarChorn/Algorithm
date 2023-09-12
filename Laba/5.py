def add_in_center(a, b, k):
    return a[:k] + b + a[k:]


# a = list(map(int,input().split()))
# Проверка
a = []
b = []
# Вводим размеры массивов
M = int(input('Введите размер массива A:'))
N = int(input('Введите размер массива B:'))

# Добавляем значения в мвссив A
for i in range(M):
    elem = int(input())
    a.append(elem)

# Добавляем значения в мвссив B
for i in range(N):
    elem = int(input())
    b.append(elem)

k = int(input('Введите K:'))
print(add_in_center(a, b, k))
