if __name__ == "__main__":
    N = int(input())

    dp = [([0] + [1] * 9) for _ in range(N)]

    for digit in range(1, N):
        for number in range(10):
            if number == 0:
                dp[digit][number] = dp[digit - 1][number + 1]
            elif number == 9:
                dp[digit][number] = dp[digit - 1][number - 1]
            else:
                dp[digit][number] = dp[digit - 1][number - 1] + dp[digit - 1][number + 1]
    
    print(sum(dp[N - 1]) % 1000000000)
