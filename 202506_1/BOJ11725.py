import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    adj_list = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        l_node, r_node = map(int, input().split())

        adj_list[l_node].append(r_node)
        adj_list[r_node].append(l_node)

    parents = [0] * (N + 1)
    stack = [1]
    visited = set()

    while stack:
        cur_node = stack.pop()
        visited.add(cur_node)

        for child in adj_list[cur_node]:
            if child not in visited:
                parents[child] = cur_node
                stack.append(child)
    
    for parent in parents[2:]:
        print(parent)