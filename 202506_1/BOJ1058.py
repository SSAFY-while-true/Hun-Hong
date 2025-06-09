import pprint
import copy

def matrix_squre(N, matrix):
    out_matrix = copy.deepcopy(matrix)

    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(N):
                    out_matrix[i][j] += matrix[i][k] * matrix[k][j]

    return out_matrix


if __name__ == "__main__":

    str_to_int = {
        "N": 0,
        "Y": 1,
    }
    N = int(input())

    matrix = [list(map(lambda x: str_to_int[x], input())) for _ in range(N)]

    result = matrix_squre(N, matrix)

    print(max([sum([i != 0 for i in row]) for row in result]))
