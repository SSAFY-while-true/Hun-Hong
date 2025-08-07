if __name__ == "__main__":
    N, M, X = map(int, input().split())

    min_dist = [[float("Inf")] * (N+1) for _ in range(N+1)]

    adj_list = []

    for _ in range(M):
        start, end, Ti = map(int, input().split())
        min_dist[start][end] = Ti
    
    from pprint import pprint
    pprint(min_dist)

    