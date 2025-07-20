def calc_str(curr, next):
    if curr == next:
        return 1

    if curr == 0:
        return 2

    if (curr - next) % 2 == 1:
        return 3
    else:
        return 4

if __name__ == "__main__":
    orders = list(map(int, input().split()))

    dp = [[[float("Inf")] * 5 for _ in range(5)] for _ in range(len(orders))]

    dp[0][0][0] = 0

    for i in range(len(orders) - 1):
        for left in range(5):
            for right in range(5):
                if left != right or (left == right == 0):
                    # print(left, right, dp[i][left][right], calc_str(left, orders[i]))
                    dp[i + 1][orders[i]][right] = min(dp[i + 1][orders[i]][right], dp[i][left][right] + calc_str(left, orders[i]))
                    dp[i + 1][left][orders[i]] = min(dp[i + 1][left][orders[i]], dp[i][left][right] + calc_str(right, orders[i]))
    
    # print(dp)
    print(min(min(dp[len(orders)-1])))
    # from pprint import pprint
    # pprint(dp)