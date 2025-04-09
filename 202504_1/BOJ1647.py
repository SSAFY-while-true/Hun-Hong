import sys
input = sys.stdin.readline


def union(represent, x, y):
    root_x = find(represent, x)
    root_y = find(represent, y)

    if root_x == root_y:
        return True
    
    if rank[root_x] > rank[root_y]:
        represent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        represent[root_x] = root_y
    else:
        represent[root_y] = root_x
        rank[root_x] += 1


def find(represent, x):
    root = x
    while represent[x] != x:
        x = represent[x]
    root_x = x

    while represent[root] != root:
        x = represent[root]
        represent[root] = root_x
        root = represent[x]

    return root_x


if __name__ == "__main__":
    N, M = map(int, input().split())

    roads = [tuple(map(int, input().split())) for _ in range(M)]
    roads.sort(key=lambda x:x[2])
    edges = 0
    represent = [i for i in range(N + 1)]
    rank = [0 for _ in range(N + 1)]

    total_cost = 0
    for left, right, cost in roads:
        if edges == N - 2:
            break
        if union(represent, left, right):
            continue
        else:
            total_cost += cost
            edges += 1
    
    print(total_cost)