import sys
input = sys.stdin.readline

def paper_recursive(N, matrix):
    global counts
    element_dict = {
        -1: 0,
        0: 1,
        1: 2,
        }

    element = matrix[0][0]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != element:
                for i in range(0,N,N//3):
                    for j in range(0,N,N//3):
                        new_matrix = [matrix[k][j:j+N//3] for k in range(i,i+N//3)]
                        paper_recursive(N//3, new_matrix)
                
                return
    else:
        counts[element_dict[element]] += 1
        return
    

if __name__ == "__main__":
    counts = [0, 0, 0]

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    paper_recursive(N, matrix)

    for count in counts:
        print(count)