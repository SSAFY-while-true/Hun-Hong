from collections import deque
n, m = map(int, input().split())

adj_list = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    adj_list[i].append(j)
    adj_list[j].append(i)

q = int(input())



for _ in range(q):
    i, j = map(int, input().split())
    adj_list[i].append(j)
    adj_list[j].append(i)
    count_list = [0]

    queue = deque()
    visited = [-1] * (n + 1)
    queue.append(1)
    visited[1] = 0
    while queue:
        curr = queue.popleft()

        for next in adj_list[curr]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[curr] + 1

    for i in range(2, n + 1):
        count_list.append(visited[i] - visited[1])

    print(" ".join(map(str, count_list)))