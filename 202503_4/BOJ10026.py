import copy

def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != '0':
                return (i, j)


def dfs(start, matrix, color):
    stack = [start]

    while stack:
        curr_i, curr_j = stack.pop()
        matrix[curr_i][curr_j] = '0'
        for d_i, d_j in move_type:
            next_i, next_j = curr_i + d_i, curr_j + d_j
            if 0 <= next_i < N and 0 <= next_j < N:
                if matrix[next_i][next_j] in color:
                    stack.append((next_i, next_j))
    return matrix

N = int(input())

move_type = [(0, 1), (1, 0), (0, -1), (-1, 0)]
art = [list(input()) for _ in range(N)]
n_count = rg_count = 0
n_art = copy.deepcopy(art)
rg_art = copy.deepcopy(art)

while find_start(n_art):
    start = find_start(n_art)
    color = n_art[start[0]][start[1]]
    n_count += 1
    n_art = dfs(start, n_art, [color])

while find_start(rg_art):
    start = find_start(rg_art)
    color = rg_art[start[0]][start[1]]
    rg_count += 1
    if color in ['R', 'G']:
        color = ['R', 'G']
    rg_art = dfs(start, rg_art, color)

print(n_count, rg_count)