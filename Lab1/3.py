# Создание массивов
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

for elem in A:
    if elem not in B and elem not in C:
        C.append(elem)

for elem in B:
    if elem not in A and elem not in C:
        C.append(elem)

# print(list(set(C)))
