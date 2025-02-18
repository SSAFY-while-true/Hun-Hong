import sys
input = sys.stdin.readline

N, M = map(int, input().split())

capus_map = [list(input().strip()) for _ in range(N)]

for i, row in enumerate(capus_map):
    for j, item in enumerate(row):
        if item == 'I':
            start_i = i
            start_j = j
            break

stack = [(start_i, start_j)]
move_type = [[0, 1], [0, -1], [1, 0], [-1, 0]]
count = 0
# visited를 배열로 처리하면 확인마다 최대 O(NM)
# visited를 N*M bool 배열로 선언한다면 O(1)
# set으로 처리하면 O(1)
visited = set((start_i, start_j))
while stack:
    curr_i, curr_j = stack.pop()
    if capus_map[curr_i][curr_j] == 'P':
        count += 1
    
    for move in move_type:
        new_i = curr_i + move[0]
        new_j = curr_j + move[1]
        if 0 <= new_i < N and 0 <= new_j < M:
            if capus_map[new_i][new_j] != 'X':
                if (new_i, new_j) not in visited:
                    stack.append((new_i, new_j))
                    # 스택에 추가함과 동시에 방문처리를 하면
                    # 스택에 중복되는 좌표가 들어가지 않기 때문에
                    # 속도 향상됨
                    visited.add((new_i, new_j))
if count > 0:
    print(count)
else:
    print("TT")