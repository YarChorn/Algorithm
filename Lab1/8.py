def sort(i):
    if i > 0: return 0
    if i < 0:
        return 1
    else:
        return 2


l = list(map(int, input().split()))

poloz = []
otriz = []
null = []

for i in l:
    match sort(i):
        case 0:
            poloz.append(i)
        case 1:
            otriz.append(i)
        case 2:
            null.append(i)

print("Положительные:", poloz)
print("Отрицательные:", otriz)
print("Нули:", null)
