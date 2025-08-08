if __name__ == "__main__":
    from collections import deque

    N = int(input())

    number_of_boom = []
    i = 1
    boom = 0
    max_N = N
    while boom < max_N:
        boom = i * (i + 1) * (i + 2) // 6
        number_of_boom.append(boom)
        i += 1

    
    # print(number_of_boom)

    init_state = (0, 0)

    min_counts = [float("Inf")] * (max_N + 1)
    queue = deque([])
    queue.append(init_state)

    while queue:
        cur_count, cur_pos = queue.popleft()
        

        for number in number_of_boom:
            if cur_pos + number > max_N:
                break
            next_pos = cur_pos + number
            next_count = cur_count + 1
            if next_count >= min_counts[next_pos]:
                continue
            else:
                min_counts[next_pos] = next_count
            
            if next_pos == N:
                break
            
            queue.append((cur_count + 1, cur_pos + number))

    print(min_counts[N])