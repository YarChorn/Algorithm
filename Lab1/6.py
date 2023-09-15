# Срез
def delete(a: list, k):
    return a[:k]


# Вызов финкции и создание массивов
a = list(map(int, input().split()))
k = int(input())
print(delete(a, k))
