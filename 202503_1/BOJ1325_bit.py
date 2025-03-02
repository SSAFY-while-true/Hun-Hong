import sys
input = sys.stdin.readline

def dec_to_bin(input:int):
    return format(input, 'b')

def DFS(start_node:int, graph:list, visited=0):
    stack = [start_node]
    visited |= 1 << start_node

    while stack:
        cur_node = stack.pop()
        neighbors = graph[cur_node]
        next_node = (neighbors & -neighbors)
        while next_node != 0:
            neighbors -= next_node
            next_node_idx = next_node.bit_length() - 1
            if not ((visited >> next_node_idx) & 1): 
                stack.append(next_node_idx)
                visited |= 1 << next_node_idx

            next_node = (neighbors & -neighbors)

    return visited
        

N, M = map(int, input().split())

adj_bit = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    adj_bit[B] |= (1 << A)

visited = DFS(1, adj_bit)

max_count = 0
max_node = []

for start_node in range(1 , N + 1):
    if visited == 0:
        continue
    else:
        visited = DFS(start_node, adj_bit)
        count = visited.bit_count()
        if max_count < count:
            max_node = [start_node]
            max_count = count
        elif max_count == count:
            max_node.append(start_node)

print(*max_node)