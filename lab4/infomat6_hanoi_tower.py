def hanoi_tower(n, source, auxiliary, target):
    if n == 1:
        print(f"{n} {source} {target}")
    else:
        hanoi_tower(n - 1, source, target, auxiliary)
        print(f"{n} {source} {target}")
        hanoi_tower(n - 1, auxiliary, source, target)


n = int(input())

hanoi_tower(n, 1, 2, 3)
