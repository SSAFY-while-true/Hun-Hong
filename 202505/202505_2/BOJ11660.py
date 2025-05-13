if __name__ == "__main__": # 리본
    N, M = map(int, input().split())

    table = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    acc_sum = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            acc_sum[i][j] = table[i][j] + acc_sum[i-1][j] + acc_sum[i][j-1] - acc_sum[i-1][j-1]
                    

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        result = acc_sum[x2][y2] - acc_sum[x1-1][y2] - acc_sum[x2][y1-1] + acc_sum[x1-1][y1-1]
        print(result)
        