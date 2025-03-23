def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                return (i, j)


def dfs(start, matrix, color):
    stack = [start]

    while stack:
        curr_i, curr_j = stack.pop()
        matrix[curr_i][curr_j] = 0
        for d_i, d_j in move_type:
            next_i, next_j = curr_i + d_i, curr_j + d_j
            if matrix[next_i][next_j] in color:
                stack.append((next_i, next_j))


N = int(input())

move_type = [(0, 1), (1, 0), (0, -1), (-1, 0)]
art = [list(input()) for _ in range(N)]

while True:
    start = find_start(art)
    color = art[start[0]][start[1]]

    