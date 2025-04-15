import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())

    min_queue = []
    max_queue = []
    removed = [False] * k

    for idx in range(k):
        cmd, value = input().split()
        value = int(value)
        if cmd == "I":
            heapq.heappush(min_queue, (value, idx))
            heapq.heappush(max_queue, (-1 * value, idx))
        elif cmd == "D":
            if value == -1:
                while min_queue:
                    q_value, idx = heapq.heappop(min_queue)
                    if not removed[idx]:
                        removed[idx] = True
                        break
            else:
                while max_queue:
                    q_value, idx = heapq.heappop(max_queue)
                    if not removed[idx]:
                        removed[idx] = True
                        break

    min_value = max_value = None

    while min_queue:
        q_value, idx = heapq.heappop(min_queue)
        if not removed[idx]:
            min_value = q_value
            break

    while max_queue:
        q_value, idx = heapq.heappop(max_queue)
        if not removed[idx]:
            max_value = -1 * q_value
            break

    if min_value is not None and max_value is not None:
        print(max_value, min_value)
    else:
        print("EMPTY")
