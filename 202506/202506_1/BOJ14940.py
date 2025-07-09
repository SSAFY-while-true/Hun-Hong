# import pprint
import sys
from collections import deque


def find_start(n, m, matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                return (i, j)

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                visited[i][j] = 0

    s_i, s_j = find_start(n, m, matrix)

    queue = deque()
    move_type = [(0, 1),
                 (1, 0),
                 (0, -1),
                 (-1, 0)]

    queue.append((s_i, s_j))
    visited[s_i][s_j] = 0

    while queue:
        cur_i, cur_j = queue.popleft()
        for m_i, m_j in move_type:
            next_i, next_j = cur_i + m_i, cur_j + m_j
            if 0 <= next_i < n and 0 <= next_j < m:
                if visited[next_i][next_j] == -1:
                    queue.append((next_i, next_j))
                    visited[next_i][next_j] = visited[cur_i][cur_j] + 1

    for row in visited:
        print(" ".join(map(str, row)))