def union(A, B):
    global parent
    Parent_A = find(A)
    Parent_B = find(B)
    
    if Parent_A == Parent_B:
        return False
    
    if rank[Parent_A] > rank[Parent_B]:
        parent[Parent_B] = Parent_A
    elif rank[Parent_A] < rank[Parent_B]:
        parent[Parent_A] = Parent_B
    else:
        parent[Parent_B] = Parent_A
        rank[Parent_A] += 1
        
    return True


def find(A):
    global parent

    if parent[A] == A:
        return A
    else:
        anc = find(parent[A])
        parent[A] = anc
        return anc


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    V, E = map(int, input().split())


    # adj_list = [[] for _ in range(V + 1)]
    edges = []
    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)

    for _ in range(E):
        A, B, C = map(int, input().split())

        edges.append((C, A, B))

    edges.sort()
    tot_cost = 0

    
    for cost, left, right in edges:
        if union(left, right):
            tot_cost += cost

    print(tot_cost)