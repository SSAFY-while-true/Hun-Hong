import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    metric = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] i에 j를 칠하는 비용의 최솟값
    dp = [[0] * 3 for _ in range (N)]

    dp[0] = metric[0]

    # print(dp)
    for i in range(1, N):
        for j in range(3):
            if j == 0:
                dp[i][j] = metric[i][j] + min(dp[i - 1][1], dp[i - 1][2])
            
            if j == 1:
                dp[i][j] = metric[i][j] + min(dp[i - 1][0], dp[i - 1][2])
            
            if j == 2:
                dp[i][j] = metric[i][j] + min(dp[i - 1][0], dp[i - 1][1])
    
    print(min(dp[N - 1]))
            