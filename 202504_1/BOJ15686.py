import sys
input = sys.stdin.readline
from itertools import combinations


def calc_distance(n_chicken, n_home, chickens, homes):

    distance = [[0] * n_home for _ in range(n_chicken)]
    for c_idx, chicken in enumerate(chickens):
        for h_idx, home in enumerate(homes):
            distance[c_idx][h_idx] = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
    
    return distance


def calc_cost(distance):
    trans_dist = [min(distances) for distances in zip(*distance)]
    return sum(trans_dist)



if __name__ == "__main__":
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    move_type = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    chickens = []
    n_chicken = 0
    homes = []
    n_home = 0

    min_distance = float("Inf")

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                homes.append((i, j))
                n_home += 1
            if matrix[i][j] == 2:
                matrix[i][j] = 0
                chickens.append((i, j))
                n_chicken += 1

    distances = calc_distance(n_chicken, n_home, chickens, homes)

    for chicken_comb in combinations(range(n_chicken), M):
        selected_distance = [distance for idx, distance in enumerate(distances) if idx in chicken_comb]
        chicken_dist = calc_cost(selected_distance)
        min_distance = min(chicken_dist, min_distance)

    print(min_distance)