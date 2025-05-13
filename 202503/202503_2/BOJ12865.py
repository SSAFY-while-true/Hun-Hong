import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())

    stuff = []

    for _ in range(N):
        W_i, V_i = map(int, input().split())
        stuff.append((W_i, V_i))

    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        W_i, V_i = stuff[i - 1]
        for j in range(1, K + 1):
            if W_i > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W_i] + V_i)
        
    print(dp[N][K])