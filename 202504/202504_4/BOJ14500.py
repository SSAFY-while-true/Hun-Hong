if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    tetro_type = [[(-1, 0),
                  (-1, 1),
                  (-1, 2),
                  (0, 3),
                  (1, 0),
                  (1, 1),
                  (1, 2)],
                 [[(-1, 1), (-1, 2)],
                  [(1, 1), (1, 2)],
                  [(1, 0), (1, 1)]],
                 [(0, -1),
                  (1, -1),
                  (2, -1),
                  (3, 0),
                  (0, 1),
                  (1, 1),
                  (2, 1)],
                 [[(1, -1), (2, -1)],
                  [(1, 1), (2, 1)]]]
    
    max_total = 0

    for i in range(N):
        for j in range(M):
            if j < M - 2:
                total = sum(matrix[i][j:j+3])
                max_total = max(total + max([matrix[i + t_i][j + t_j] for t_i, t_j in tetro_type[0] 
                                     if 0 <= i + t_i < N and 0 <= j + t_j < M]), max_total)
            if j < M - 1:
                total = sum(matrix[i][j:j+2])
                max_total = max(total + max([sum([matrix[i + t_i][j + t_j] for t_i, t_j in tetro 
                    if 0 <= i + t_i < N and 0 <= j + t_j < M]) for tetro in tetro_type[1]]), max_total)
            
            if i < N - 2:
                total = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j]
                max_total = max(total + max([matrix[i + t_i][j + t_j] for t_i, t_j in tetro_type[2] 
                                     if 0 <= i + t_i < N and 0 <= j + t_j < M]), max_total)
            
            if i < N - 1:
                total = matrix[i][j] + matrix[i + 1][j]
                max_total = max(total + max([sum([matrix[i + t_i][j + t_j] for t_i, t_j in tetro 
                    if 0 <= i + t_i < N and 0 <= j + t_j < M]) for tetro in tetro_type[3]]), max_total)
            
    
    print(max_total)