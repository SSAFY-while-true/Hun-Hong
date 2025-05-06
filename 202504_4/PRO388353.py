
def solution(storage, requests):
    N, M = len(storage), len(storage[0])
    for i in range(N):
        storage[i] = list(storage[i])
    side = []
    
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                side.append((i, j))
    
    count = N * M
    move_type = [(0, 1),
                (1, 0),
                (0, -1),
                (-1, 0)]
    
    for request in requests:
        if len(request) == 1:
            available = []
            stack = side[:]
            visited = [[False] * M for _ in range(N)]
            while stack:
                curr_i, curr_j = stack.pop()
                if storage[curr_i][curr_j] == 0:
                    for m_i, m_j in move_type:
                        next_i, next_j = curr_i + m_i, curr_j + m_j
                        if 0 <= next_i < N and 0 <= next_j < M:
                            if not visited[next_i][next_j]:
                                stack.append((next_i, next_j))
                                visited[next_i][next_j] = True
                                
                else:
                    available.append((curr_i, curr_j))
            

            for a_i, a_j in available:
                if storage[a_i][a_j] == request:
                    storage[a_i][a_j] = 0
                    count -= 1

        else:  # 2개
            for i in range(N):
                for j in range(M):
                    if storage[i][j] == request[0]:
                        storage[i][j] = 0
                        count -= 1

    return count