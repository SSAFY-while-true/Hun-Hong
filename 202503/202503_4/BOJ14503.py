def dfs_robot(start, room):
    stack = [start]
    count = 0

    while stack:
        cur_i, cur_j, cur_dir = stack.pop()
        if room[cur_i][cur_j] == 0:
            room[cur_i][cur_j] = 2
            count += 1

        for i in range(1, 5):
            next_dir = (cur_dir - i) % 4
            m_i, m_j, m_dir = move_type[next_dir]
            next_i, next_j = cur_i + m_i, cur_j + m_j
            if 0 <= next_i < N and 0 <= next_j < M:
                if room[next_i][next_j] == 0:
                    stack.append((next_i, next_j, m_dir))
                    break
        
        else:
            next_i, next_j = cur_i - m_i, cur_j - m_j
            if 0 <= next_i < N and 0 <= next_j < M:
                if room[next_i][next_j] != 1:
                    stack.append((next_i, next_j, m_dir))
                    continue

                return count


if __name__ == "__main__":
    N, M = map(int, input().split())

    move_type = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]

    start = list(map(int,input().split()))

    room = [list(map(int, input().split())) for _ in range(N)]

    count = dfs_robot(start, room)

    print(count)