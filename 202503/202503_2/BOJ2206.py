import sys
from collections import deque
input = sys.stdin.readline


def BFS(N, M, start, map):
    visited = [[0] * M for _ in range(N)]
    move_type = [(0, 1),
                 (0, -1),
                 (1, 0),
                 (-1, 0)]
    
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        curr_i, curr_j = queue.popleft()
        for move_i, move_j in move_type:
            next_i = curr_i + move_i
            next_j = curr_j + move_j
            if 0 <= next_i < N and 0 <= next_j < M:
                if map[next_i][next_j] == 0 and visited[next_i][next_j] == 0:
                    queue.append((next_i, next_j))
                    visited[next_i][next_j] = visited[curr_i][curr_j] + 1
    
    return visited


def break_wall(map, start_visited, end_visited):
    move_type = [(0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)]
    minimum_value = float("Inf")

    if start_visited[N - 1][M - 1]:
        minimum_value = start_visited[N - 1][M - 1]

    for i in range(N):
        for j in range(M):
            if map[i][j] == 1:
                for move_i, move_j in move_type:
                    ni = i + move_i
                    nj = j + move_j
                    if 0 <= ni < N and 0 <= nj < M:
                        if start_visited[ni][nj] != 0:
                            for move_i2, move_j2 in move_type:
                                ni_2 = i + move_i2
                                nj_2 = j + move_j2
                                if 0 <= ni_2 < N and 0 <= nj_2 < M:
                                    if end_visited[ni_2][nj_2] != 0:
                                        if (ni, nj) != (ni_2, nj_2):
                                            minimum_value = min(minimum_value, start_visited[ni][nj] + end_visited[ni_2][nj_2] + 1)
                


    if minimum_value > N * M:
        return -1
    else:
        return minimum_value


if __name__ == "__main__":
    N, M = map(int, input().split())

    map = [list(map(int, input().strip())) for _ in range(N)]

    start_visited = BFS(N, M, (0, 0), map)
    end_visited = BFS(N, M, (N - 1, M - 1), map)

    # pprint(start_visited)
    # pprint(end_visited)

    print(break_wall(map, start_visited, end_visited))
   