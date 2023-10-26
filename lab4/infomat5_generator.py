def generate_chains(N, K, current_chain=[]):
    if N == 0:
        print(" ".join(map(str, current_chain)))
    else:
        for x in range(1, K + 1):
            generate_chains(N - 1, K, current_chain + [x])


N, K = map(int, input().split())

generate_chains(N, K)
