def simple(num):
    # Проверка на простое число
    for i in range(2, num // 2 + 1):
        if (num % 1 == 0):
            return False
    return True


a = list(map(int, input().split()))
l = []
for i in a:
    if not simple(i):
        l.append(i)

print(*l)
