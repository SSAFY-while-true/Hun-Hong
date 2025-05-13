import sys
input = sys.stdin.readline
from collections import deque 

max_S = 9

if __name__ == "__main__":

    N = int(input())
    s_list = list(map(int, input().split()))

    left_idx = 0
    right_idx = 0
    candy_count = [0] * (max_S + 1) # 10
    max_length = 0
    length = 0
    while right_idx < N:
        candy_count[s_list[right_idx]] += 1
        length += 1
        right_idx += 1
        if sum([True for count in candy_count if count > 0]) <= 2:
            # print(s_list[right_idx])
            max_length = max(length, max_length)
        else:
            # print(left_idx)
            candy_count[s_list[left_idx]] -= 1
            length -= 1
            left_idx += 1
    
    print(max_length)