from copy import deepcopy

def solution(info, edges):
    adj_set = [set() for _ in range(len(info))]
    
    for s, e in edges:
        adj_set[s].add(e)
        adj_set[e].add(s)
    
    
    visited = set([0])
    available = adj_set[0]
    
    stack  = [(available, 1, 0, visited)]
    max_sheep = 1
    
    while stack:
        curr_available, curr_sheep, curr_wolf, curr_visited = stack.pop()
        
        if curr_sheep > max_sheep:
            max_sheep = curr_sheep
        
        for next_node in curr_available:
            if next_node not in curr_visited:
                next_visited = deepcopy(curr_visited)
                next_visited.add(next_node)
                next_available = deepcopy(curr_available)
                next_available.update(adj_set[next_node])
                if info[next_node] == 1:
                    next_sheep, next_wolf = curr_sheep, curr_wolf + 1
                else:
                    next_sheep, next_wolf = curr_sheep + 1, curr_wolf
                
                if next_sheep > next_wolf:
                    stack.append((next_available, next_sheep, next_wolf, next_visited))
                
    answer = max_sheep
    return answer