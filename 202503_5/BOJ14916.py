if __name__ == "__main__":
    n = int(input())
    max_length = 1000000
    dp = [float("Inf")] * (max_length + 1)

    dp[2] = dp[5] = 1
    dp[4] = 2
                                               
    for i in range(6, n + 1):
        dp[i] = min(dp[i], dp[i - 2] + 1, dp[i - 5] + 1)
    
    if dp[n] == float("Inf"):
        print(-1)
    else:
        print(dp[n])