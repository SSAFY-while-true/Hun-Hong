def dfs_backtrack(s_set, se_dict):
    global START, END, DICE

    min_cost = [float("Inf")] * (END + 1)
    
    stack = [(START, 0)]
    min_cost[START] = 0

    while stack:
        # print(stack)
        cur_pos, cur_cost = stack.pop()

        if cur_cost < min_cost[END]:
            for next_pos in range(cur_pos + 1, min(cur_pos + DICE + 1, END + 1)):
                if next_pos == END:
                    min_cost[END] = min(min_cost[END], cur_cost + 1)
                
                if min_cost[next_pos] > cur_cost + 1:
                    if next_pos in s_set:
                        stack.append((se_dict[next_pos], cur_cost + 1))
                        min_cost[se_dict[next_pos]] = cur_cost + 1
                    else:
                        stack.append((next_pos, cur_cost + 1))
                    min_cost[next_pos] = cur_cost + 1

    return min_cost[END]

if __name__ == "__main__":
    START = 1
    END = 100
    DICE = 6

    N, M = map(int, input().split())
    s_set = set()
    se_dict = dict()

    for _ in range(N + M):
        s, e = map(int, input().split())
        s_set.add(s)
        se_dict[s] = e
    
    result = dfs_backtrack(s_set, se_dict)

    print(result)
