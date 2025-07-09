if __name__ == "__main__":
    from collections import deque
    N, K = map(int, input().split())

    queue = deque([(N, 0)])
    
    min_time = [float("Inf")] * 100001
    min_time[N] = 0
    

    while queue:
        curr_pos, curr_time = queue.popleft()

        if curr_pos == K:
            min_time[K] = min(min_time[K], curr_time)
            continue

        for next_pos, next_time in [(curr_pos - 1, curr_time + 1), (curr_pos + 1, curr_time + 1), (curr_pos * 2, curr_time)]:
            if 0 <= next_pos <= 100000 and next_time < min_time[next_pos]:
                if next_pos > K:
                    if next_pos - K + next_time > min_time[K]:
                        continue
                if curr_time == next_time:
                    queue.appendleft((next_pos, next_time))
                    min_time[next_pos] = next_time
                else:
                    queue.append((next_pos, next_time))
                    min_time[next_pos] = next_time
    
    print(min_time[K])