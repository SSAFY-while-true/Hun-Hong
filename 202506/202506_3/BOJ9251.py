if __name__ == "__main__":
    left_str = input()
    right_str = input()

    dp = [[0] * (len(right_str) + 1) for _ in range(len(left_str) + 1)]

    for i in range(1, len(left_str) + 1):
        for j in range(1, len(right_str) + 1):
            if left_str[i - 1] == right_str[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # print(dp)
    print(dp[len(left_str)][len(right_str)])