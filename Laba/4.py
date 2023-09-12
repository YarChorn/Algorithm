def dobyavka_v_konec_massiva(n: list, k: list):
    return n + k


# создание массивов и вызов функции
n = list(map(int, input().split()))
k = list(map(int, input().split()))
print(dobyavka_v_konec_massiva(n, k))
