import sys
from collections import deque
from itertools import islice
input = sys.stdin.readline


def ac_function(cmd: str, int_list: deque):
    reverse_flag = False
    for char in cmd:
        if char == "R":
            reverse_flag = not reverse_flag
        else:
            if not int_list:
                return "error"
            else:
                if reverse_flag:
                    int_list.pop()
                else:
                    int_list.popleft()
    if reverse_flag:
        int_list.reverse()
        
    return int_list

T = int(input())
for test_case in range(1, T + 1):
    p = input().strip('\n')
    n = int(input())

    input_xi = input()
    if input_xi != '[]\n':
        xi = deque(map(int, input_xi.strip('[').strip(']\n').split(',')))
    else:
        xi = []

    result = ac_function(p, xi)
    if result == "error":
        print(result)
    else:
        print(f"[{','.join(map(str, result))}]")