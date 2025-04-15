# dp  1 2 3 4 5 6 7 8 9
# dp [2 0 2 3 0 0 0 0 0]
# dp[node][0] : node가 얼리어답터가 아닌경우
# dp[node][1] : node가 얼리어답터인 경우
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs_tree(node, parent):
    global tree, dp
    dp[node][0] = 0
    dp[node][1] = 1
    sum_dp1 = 0
    sum_dp0 = 0
    for child in tree[node]:
        if child == parent:
            continue
        dfs_tree(child, node)
        dp[node][0] += dp[child][1]
        dp[node][1] += min(dp[child][0],dp[child][1])


N = int(input())


tree = [[] for _ in range(N + 1)]
dp = [[0] * 2 for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# print(root)
# print(child_list)
dfs_tree(1, 0)
# print(dp)
print(min(dp[1]))