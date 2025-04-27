if __name__ == "__main__":
    cost = input()

    dp = [0] * (100000 + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[5] = 1
    dp[7] = 1
    for i in range(1, len(dp)):
        if dp[i] == 0:
            if i > 7:
                dp[i] = min(dp[i-1] + 1, dp[i-2] + 1, dp[i-5] + 1, dp[i-7] + 1)
            elif i > 5:
                dp[i] = min(dp[i-1] + 1, dp[i-2] + 1, dp[i-5] + 1)
            elif i > 2:
                dp[i] = min(dp[i-1] + 1, dp[i-2] + 1)
    
    print(dp[int(cost)])