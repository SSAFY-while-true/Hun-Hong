def dfs_land(land, s_i, s_j):
    global fuel_idx, fuel_dict

    n, m = len(land), len(land[0])
    move_type = [(0, 1),
                 (1, 0),
                 (0, -1),
                 (-1, 0)]
    # matrix = deepcopy(land)

    stack = [(s_i, s_j)]
    land[s_i][s_j] = 0
    count = 1
    
    while stack:
        c_i, c_j = stack.pop()
        
        for m_i, m_j in move_type:
            n_i, n_j = c_i + m_i, c_j + m_j

            if 0 <= n_i < n and 0 <= n_j < m:
                if land[n_i][n_j] == 1:
                    stack.append((n_i, n_j))
                    land[n_i][n_j] = fuel_idx
                    count += 1
    
    fuel_dict[fuel_idx] = count
    return


def solution(land):
    global fuel_idx, cur_land, fuel_dict

    fuel_idx = 2
    fuel_dict = dict()
    cur_land = land
    max_count = 0
    n, m = len(land), len(land[0])

    for j in range(m):
        count = 0
        visited = set()

        for i in range(n):
            if cur_land[i][j] > 1:
                if cur_land[i][j] not in visited: 
                    count += fuel_dict[cur_land[i][j]]
                    visited.add(cur_land[i][j])

            elif cur_land[i][j] == 1:
                dfs_land(cur_land, i, j)
                count += fuel_dict[fuel_idx]
                visited.add(fuel_idx)
                fuel_idx += 1
                
        # print(count)
        max_count = max(max_count, count)
    # print(fuel_dict)
    return max_count