import sys
input = sys.stdin.readline

def DFS(N, start_node, graph):
    visited = [False] * (N + 1)
    
    stack = [start_node]
    visited[start_node] = True

    while stack:
        curr_node = stack.pop()
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True
    
    return visited



N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[B].append(A)

max_count = 0
max_list = []

for start in range(1, N + 1):
    visited = DFS(N, start, adj_list)

    if sum(visited) > max_count:
        max_list = [start]
        max_count = sum(visited)
    elif sum(visited) == max_count:
        max_list.append(start)

print(*max_list)