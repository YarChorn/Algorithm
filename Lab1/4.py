# При использовании + для сцепления 2х массивов,создается новый массив ,который содержит все элементы из первого массива
# ,за которыми следуют элементы из 2го массива.
def Sum_mass(n: list, k: list):
    return n + k


# Сцепление массивов  через for
def concatenate_arrays(arr1, arr2):
    result = []
    for element in arr1:
        result.append(element)
    for element in arr2:
        result.append(element)
    return result


# Метод extend изменяет исходный список, на котором он вызывается, и не возвращает новый список.
def sum_mass_2(n: list, k: list):
    n.extend(k)
    return n


# создание массивов и вызов функции
n = list(map(int, input().split()))
k = list(map(int, input().split()))
