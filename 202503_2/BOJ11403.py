import sys
input = sys.stdin.readline


def DFS(start, graph, length):
    visited = [False] * (length + 1)

    stack = [start]

    while stack:
        curr_node = stack.pop()
        for next_node in range(1, length + 1):
            if graph[curr_node][next_node] == 1 and not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True

    return list(map(int, visited[1:]))


if __name__ == "__main__":

    N = int(input())

    adj_matrix = [[0] * (N + 1)]
    for _ in range(N):
        adj_matrix.append([0] + list(map(int, input().split())))

    for start in range(1, N + 1):
        print(*DFS(start, adj_matrix, N))