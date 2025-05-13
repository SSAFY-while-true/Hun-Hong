import sys
input = sys.stdin.readline


if __name__ == "__main__":
    # 사자를 배치하지 않음  :0
    # 왼쪽에 사자를 배치    :1
    # 오른쪽에 사자를 배치  :2
    # 상태는 총 3개
    N = int(input())
    dp = [[1] * 2 for _ in range(3)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[2][0] = 1
    for _ in range(0, N - 1):
        dp[0][1] = dp[0][0] + dp[1][0] + dp[2][0]
        dp[1][1] = dp[0][0] + dp[2][0]
        dp[2][1] = dp[0][0] + dp[1][0]

        dp[0][0] = dp[0][1]
        dp[1][0] = dp[1][1]
        dp[2][0] = dp[2][1]

    print(sum([dp[i][1] for i in range(3)]) % 9901)