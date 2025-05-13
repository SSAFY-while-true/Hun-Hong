def union(represent, rank, x, y):
    
    anc_x = find(represent, x)
    anc_y = find(represent, y)

    if anc_x == anc_y:
        return True
    
    if rank[anc_x] > rank[anc_y]:
        represent[anc_y] = anc_x

    elif rank[anc_x] < rank[anc_y]:
        represent[anc_x] = anc_y
    
    else:
        represent[anc_y] = anc_x
        rank[anc_x] += 1


def find(represent, x):

    root = x
    while root != represent[root]:
        root = represent[root]

    while root != represent[x]:
        parent = represent[x]
        represent[x] = root
        x = parent

    return root

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    represent = [i for i in range(n)]
    rank = [0] * (n + 1)
    end = 0

    for _ in range(m):
        x, y = map(int, input().split())
        end += 1
        if union(represent, rank, x, y):
            break
    else:
        end = 0
        
    print(end)