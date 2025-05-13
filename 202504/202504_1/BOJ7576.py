import sys
input = sys.stdin.readline
from collections import deque


def find_max(visited, matrix):
    max_value = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and matrix[i][j] != -1:
                return -1
            max_value = max(max_value, visited[i][j])
    
    return max_value - 1


if __name__ == "__main__":
    M, N = map(int, input().split())

    move_type = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = 1
    
    while queue:
        curr_i, curr_j = queue.popleft()
        for m_i, m_j in move_type:
            next_i, next_j = curr_i + m_i, curr_j + m_j
            if 0 <= next_i < N and 0 <= next_j < M:
                if matrix[next_i][next_j] != -1 and visited[next_i][next_j] == 0:
                    queue.append((next_i, next_j))
                    visited[next_i][next_j] = visited[curr_i][curr_j] + 1
    
    print(find_max(visited, matrix))