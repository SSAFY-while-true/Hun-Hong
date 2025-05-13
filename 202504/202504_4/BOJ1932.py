if __name__ == "__main__":
    N = int(input())

    dp = [[0] * i for i in range(1, N + 1)]
    triangle = [list(map(int,input().split())) for _ in range(N)]
    
    dp[0][0] = triangle[0][0]

    for row in range(1, N):
        for i in range(row + 1):
            if i == 0:
                dp[row][i] = dp[row - 1][0] + triangle[row][i]
            elif i == row:
                dp[row][i] = dp[row - 1][row - 1] + triangle[row][i]
            else:
                dp[row][i] = max(dp[row - 1][i - 1], dp[row - 1][i]) + triangle[row][i]
    
    print(max(dp[N - 1]))
