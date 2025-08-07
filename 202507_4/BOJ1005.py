if __name__ == "__main__":
    from collections import deque
    import sys
    input = sys.stdin.readline
    T = int(input())

    for i in range(1, T + 1):
        N, K = map(int, input().split())
        D = [0] + list(map(int, input().split()))
        dp = [0] * (N + 1)
        indegree = [0] * (N + 1)
        adj_list = [[] for _ in range(N + 1)]

        for _ in range(K):
            X, Y = map(int, input().split())
            indegree[Y] += 1
            adj_list[X].append(Y)
        
        W = int(input())

        queue = deque([])
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = D[i]
        
        while queue:
            cur_node = queue.popleft()
            if cur_node == W:
                break

            for next_node in adj_list[cur_node]:
                next_time = dp[cur_node] + D[next_node]
                dp[next_node] = max(dp[next_node], next_time)

                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append((next_node))
                        
        print(dp[W])