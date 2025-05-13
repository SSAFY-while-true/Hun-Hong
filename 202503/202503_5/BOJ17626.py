import math

if __name__ == "__main__":
    max_length = 50000
    n = int(input())
    dp = [float("Inf")] * (n + 1)

    for i in range(n + 1):
        if int(math.sqrt(i)) == math.sqrt(i):
            dp[i] = 1
        else:
            max_root = int(math.sqrt(i))
            j = 1
            while j ** 2 <= i // 2:
                if dp[i] == 2:
                    break
                dp[i] = min(dp[i], dp[i - j ** 2] + dp[j ** 2])
                j += 1

    print(dp[n])