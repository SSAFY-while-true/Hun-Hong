def calculate_road(N, L, matrix):
    h_info = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0:
                cur_h = matrix[i][j]
                count = 1
                continue

            if cur_h == matrix[i][j]:
                count += 1
            
            if  (cur_h != matrix[i][j]):
                h_info[i].append((cur_h, count))
                cur_h = matrix[i][j]
                count = 1
            
            if (j == N - 1):
                h_info[i].append((cur_h, count))
    
    road_count = 0
    for i in range(N):
        for idx, (cur_h, cur_count) in enumerate(h_info[i]):
            if idx == 0:
                continue            
            
            prev_h, prev_count = h_info[i][idx - 1]

            if 2 > cur_h - prev_h > 0:
                if prev_count >= L:
                    h_info[i][idx - 1] = (prev_h, prev_count - L)
                else:
                    break
            elif -2 < cur_h - prev_h < 0:
                if cur_count >= L:
                    h_info[i][idx] = (cur_h, cur_count - L)
                else:
                    break
            else:
                break
            
        else:
            road_count += 1
    
    return road_count

if __name__ == "__main__":
    import sys
    inpurt = sys.stdin.readline

    N, L = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    road_count = 0

    road_count += calculate_road(N, L, matrix)

    trans_matrix = list(map(list, zip(*matrix)))
    
    road_count += calculate_road(N, L, trans_matrix)

    print(road_count)