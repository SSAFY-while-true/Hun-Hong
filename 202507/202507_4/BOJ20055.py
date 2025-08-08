from collections import deque
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())

    A_list = list(map(int, input().split()))
    belt = deque(A_list)
    robots = deque([False] * N)
    zero_count = sum([1 for number in A_list if number == 0])
    stage_count = 0
    
    while zero_count < K:
        stage_count += 1
        #1
        belt.rotate(1)
        robots.rotate(1)
        robots[N-1] = False

        #2
        for idx in range(N-2,-1,-1):
            if robots[idx] and not robots[idx + 1] and belt[idx + 1] >= 1:
                robots[idx] = False
                robots[idx + 1] = True
                belt[idx + 1] -= 1
                if belt[idx + 1] == 0:
                    zero_count += 1
        robots[N-1] = False
        
        #3.
        if belt[0] >= 1:
            robots[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                zero_count += 1
        # print(belt)
    print(stage_count)