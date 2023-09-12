# Создание массивов
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

# Перебор на значения
for i in A:
    if i not in B:
        C.append(i)

for i in B:
    if i not in A:
        C.append(i)


print(list(set(C)))
